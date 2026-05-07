from __future__ import annotations

import importlib.util
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
GENERATOR_PATH = ROOT / 'scripts' / 'generate_codex_parity_contract.py'


def load_module(name: str, path: Path):
    """Load the contract generator module from a file path."""
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:  # pragma: no cover - importlib guardrail
        raise RuntimeError(f'Unable to load module from {path}')
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


class GenerateCodexParityContractTests(unittest.TestCase):
    def test_build_contract_includes_hook_support_and_runtime_doctor(self) -> None:
        module = load_module('generate_codex_parity_contract_test', GENERATOR_PATH)
        contract = module.build_contract()

        runtime = contract['runtime']
        support_lookup = {
            item['event']: item
            for item in runtime['hookSupport']
        }

        self.assertEqual(runtime['readiness']['skill']['name'], 'codex-runtime-doctor')
        self.assertEqual(runtime['readiness']['role'], 'diagnosis_only')
        self.assertEqual(support_lookup['PreToolUse']['matcherBehavior'], 'bash_only')
        self.assertTrue(support_lookup['PreToolUse']['configured'])
        self.assertEqual(support_lookup['PostToolUse']['matcherBehavior'], 'bash_only')
        self.assertIn('authoritative_stop_gate', support_lookup['Stop']['supportTags'])
        self.assertFalse(support_lookup['UserPromptSubmit']['configured'])
        self.assertEqual(
            support_lookup['UserPromptSubmit']['matcherBehavior'],
            'matcher_ignored',
        )

    def test_build_contract_keeps_runtime_readiness_as_its_own_outcome(self) -> None:
        module = load_module('generate_codex_parity_contract_outcome_test', GENERATOR_PATH)
        contract = module.build_contract()

        outcomes = {item['id']: item for item in contract['outcomes']}
        runtime_readiness = outcomes['runtime-readiness']

        self.assertEqual(runtime_readiness['agents'], ['swift_quality'])
        self.assertEqual(
            [item['name'] for item in runtime_readiness['skills']],
            ['codex-operating-layer', 'codex-runtime-doctor'],
        )


if __name__ == '__main__':
    unittest.main()
