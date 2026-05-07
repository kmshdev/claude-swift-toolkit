from __future__ import annotations

import importlib.util
import io
import json
import unittest
from pathlib import Path
from unittest import mock


ROOT = Path(__file__).resolve().parents[1]
STOP_HOOK_PATH = ROOT / ".codex" / "hooks" / "stop_validate_codex_surface.py"


def load_module(name: str, path: Path):
    """Load a stop-hook module from a concrete file path."""
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:  # pragma: no cover - importlib guardrail
        raise RuntimeError(f"Unable to load module from {path}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


class StopValidateCodexSurfaceTests(unittest.TestCase):
    def test_main_blocks_when_generator_fails_after_target_changes(self) -> None:
        module = load_module("stop_validate_codex_surface_block", STOP_HOOK_PATH)
        stdout = io.StringIO()
        with mock.patch.object(module, "PARITY_SOURCE_PATH", ROOT / "AGENTS.md"), mock.patch.object(
            module, "load_validation_targets", return_value=[".codex"]
        ), mock.patch.object(module, "working_tree_touches_targets", return_value=True), mock.patch.object(
            module,
            "run_check",
            return_value=(False, "generator failed hard"),
        ), mock.patch("sys.stdout", stdout):
            result = module.main()

        self.assertEqual(result, 0)
        response = json.loads(stdout.getvalue())
        self.assertEqual(response["decision"], "block")
        self.assertIn("Canonical Codex files changed", response["reason"])
        self.assertIn("generator failed hard", response["reason"])

    def test_main_skips_when_canonical_targets_are_untouched(self) -> None:
        module = load_module("stop_validate_codex_surface_skip", STOP_HOOK_PATH)
        stdout = io.StringIO()
        with mock.patch.object(module, "PARITY_SOURCE_PATH", ROOT / "AGENTS.md"), mock.patch.object(
            module, "load_validation_targets", return_value=[".codex"]
        ), mock.patch.object(module, "working_tree_touches_targets", return_value=False), mock.patch(
            "sys.stdout", stdout
        ):
            result = module.main()

        self.assertEqual(result, 0)
        self.assertEqual(stdout.getvalue(), "")


if __name__ == "__main__":
    unittest.main()
