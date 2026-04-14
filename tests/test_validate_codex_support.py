from __future__ import annotations

import importlib.util
import json
import sys
import unittest
from pathlib import Path
from tempfile import TemporaryDirectory
from unittest import mock


ROOT = Path(__file__).resolve().parents[1]
VALIDATOR_PATH = ROOT / 'scripts' / 'validate-codex-support.py'


def load_module(name: str, path: Path):
    """Load the validator module from a file path."""
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:  # pragma: no cover - importlib guardrail
        raise RuntimeError(f'Unable to load module from {path}')
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


class ValidateCodexSupportTests(unittest.TestCase):
    def test_validate_document_truth_reports_missing_phrase(self) -> None:
        module = load_module('validate_codex_support_missing_phrase', VALIDATOR_PATH)
        with TemporaryDirectory() as temp_dir:
            doc_path = Path(temp_dir) / 'README.md'
            doc_path.write_text('Hooks are repo-scoped and experimental.\n')

            errors = module.validate_document_truth(
                doc_path,
                ('Hooks are repo-scoped and experimental.', '`Stop` remains the authoritative completion gate.'),
            )

        self.assertEqual(len(errors), 1)
        self.assertIn('required truth phrase', errors[0])

    def test_validate_unsupported_hook_claims_rejects_general_interception(self) -> None:
        module = load_module('validate_codex_support_hook_claims', VALIDATOR_PATH)
        with TemporaryDirectory() as temp_dir:
            doc_path = Path(temp_dir) / 'README.md'
            doc_path.write_text(
                '`PreToolUse` and `PostToolUse` are not just Bash-only; they also cover Edit.\n'
            )

            errors = module.validate_unsupported_hook_claims(doc_path)

        self.assertEqual(len(errors), 1)
        self.assertIn('unsupported non-Bash hook claim', errors[0])

    def test_validate_runtime_doctor_scope_rejects_fixer_language(self) -> None:
        module = load_module('validate_codex_support_doctor_scope', VALIDATOR_PATH)
        with TemporaryDirectory() as temp_dir:
            doc_path = Path(temp_dir) / 'README.md'
            doc_path.write_text(
                'codex-runtime-doctor does not install tools, but it can open Xcode.\n'
            )

            errors = module.validate_runtime_doctor_scope(doc_path)

        self.assertEqual(len(errors), 1)
        self.assertIn('diagnosis-only', errors[0])

    def test_validate_hooks_rejects_session_start_matcher_drift(self) -> None:
        module = load_module('validate_codex_support_session_start', VALIDATOR_PATH)
        with TemporaryDirectory() as temp_dir:
            hooks_path = Path(temp_dir) / 'hooks.json'
            hooks_path.write_text(
                json.dumps(
                    {
                        'hooks': {
                            'SessionStart': [
                                {
                                    'matcher': 'all',
                                    'hooks': [
                                        {
                                            'type': 'command',
                                            'command': '/usr/bin/python3 ".codex/hooks/session_context.py"',
                                        }
                                    ],
                                }
                            ],
                            'PreToolUse': [
                                {
                                    'matcher': 'Bash',
                                    'hooks': [
                                        {
                                            'type': 'command',
                                            'command': '/usr/bin/python3 ".codex/hooks/pre_tool_use_policy.py"',
                                        }
                                    ],
                                }
                            ],
                            'PostToolUse': [
                                {
                                    'matcher': 'Bash',
                                    'hooks': [
                                        {
                                            'type': 'command',
                                            'command': '/usr/bin/python3 ".codex/hooks/post_tool_use_policy.py"',
                                        }
                                    ],
                                }
                            ],
                            'Stop': [
                                {
                                    'hooks': [
                                        {
                                            'type': 'command',
                                            'command': '/usr/bin/python3 ".codex/hooks/stop_validate_codex_surface.py"',
                                        }
                                    ],
                                }
                            ],
                        }
                    }
                )
            )

            with mock.patch.object(module, 'HOOKS_PATH', hooks_path):
                errors = module.validate_hooks()

        self.assertIn('hooks.SessionStart matcher must be', errors[0])

    def test_validate_contract_truth_passes_for_current_repo_state(self) -> None:
        module = load_module('validate_codex_support_repo_truth', VALIDATOR_PATH)
        self.assertEqual(module.validate_contract_truth(), [])


if __name__ == '__main__':
    unittest.main()
