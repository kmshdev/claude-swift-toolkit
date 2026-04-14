from __future__ import annotations

import importlib.util
import json
import unittest
from pathlib import Path
from tempfile import TemporaryDirectory
from unittest import mock


ROOT = Path(__file__).resolve().parents[1]
DOCTOR_PATH = (
    ROOT
    / ".codex"
    / "skills"
    / "codex-runtime-doctor"
    / "scripts"
    / "check_runtime.py"
)


def load_module(name: str, path: Path):
    """Load the runtime doctor module from a file path."""
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:  # pragma: no cover - importlib guardrail
        raise RuntimeError(f"Unable to load module from {path}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def completed(stdout: str = "", stderr: str = "", returncode: int = 0):
    """Create a completed process stub for subprocess probes."""
    return mock.Mock(stdout=stdout, stderr=stderr, returncode=returncode)


class CodexRuntimeDoctorTests(unittest.TestCase):
    def test_ready_report_on_supported_platform(self) -> None:
        module = load_module("codex_runtime_doctor_ready", DOCTOR_PATH)
        with mock.patch.object(module, "run_command", side_effect=[
            completed(stdout="Codex support validation passed."),
            completed(stdout="/Applications/Xcode.app/Contents/Developer/usr/bin/xcodebuild"),
            completed(stdout="/Applications/Xcode.app/Contents/Developer/usr/bin/mcpbridge"),
        ]), mock.patch.object(module.platform, "system", return_value="Darwin"), mock.patch.object(
            module.Path, "home", return_value=Path("/tmp/no-overlay-home")
        ):
            report = module.build_report()

        self.assertEqual(report["summary"], "ready")
        self.assertEqual(report["sections"]["repo_hooks"]["status"], "ready")
        self.assertEqual(report["sections"]["xcode_bridge"]["status"], "ready")
        self.assertEqual(report["sections"]["external_hook_overlay"]["status"], "absent")

    def test_windows_marks_hooks_unavailable_without_breaking_whole_runtime(self) -> None:
        module = load_module("codex_runtime_doctor_windows", DOCTOR_PATH)
        with mock.patch.object(module, "run_command", side_effect=[
            completed(stdout="Codex support validation passed."),
            completed(stdout="/Applications/Xcode.app/Contents/Developer/usr/bin/xcodebuild"),
            completed(stdout="/Applications/Xcode.app/Contents/Developer/usr/bin/mcpbridge"),
        ]), mock.patch.object(module.platform, "system", return_value="Windows"), mock.patch.object(
            module.Path, "home", return_value=Path("/tmp/no-overlay-home")
        ):
            report = module.build_report()

        self.assertEqual(report["sections"]["repo_hooks"]["status"], "unavailable")
        self.assertEqual(report["sections"]["canonical_surface"]["status"], "ready")

    def test_stale_contract_reports_degraded_canonical_surface(self) -> None:
        module = load_module("codex_runtime_doctor_stale", DOCTOR_PATH)
        with mock.patch.object(module, "run_command", side_effect=[
            completed(stderr="Codex support validation failed: stale or invalid parity contract", returncode=1),
            completed(stdout="/Applications/Xcode.app/Contents/Developer/usr/bin/xcodebuild"),
            completed(stdout="/Applications/Xcode.app/Contents/Developer/usr/bin/mcpbridge"),
        ]), mock.patch.object(module.platform, "system", return_value="Darwin"), mock.patch.object(
            module.Path, "home", return_value=Path("/tmp/no-overlay-home")
        ):
            report = module.build_report()

        self.assertEqual(report["sections"]["canonical_surface"]["status"], "degraded")
        self.assertIn("Validator failed", report["sections"]["canonical_surface"]["evidence"][1])

    def test_external_hook_overlay_is_reported_without_parsing_it(self) -> None:
        module = load_module("codex_runtime_doctor_overlay", DOCTOR_PATH)
        overlay_home = ROOT / "tests" / "fixtures-home"
        (overlay_home / ".codex").mkdir(parents=True, exist_ok=True)
        overlay_path = overlay_home / ".codex" / "hooks.json"
        overlay_path.write_text("not-json-on-purpose")
        try:
            with mock.patch.object(module, "run_command", side_effect=[
                completed(stdout="Codex support validation passed."),
                completed(stdout="/Applications/Xcode.app/Contents/Developer/usr/bin/xcodebuild"),
                completed(stdout="/Applications/Xcode.app/Contents/Developer/usr/bin/mcpbridge"),
            ]), mock.patch.object(module.platform, "system", return_value="Darwin"), mock.patch.object(
                module.Path, "home", return_value=overlay_home
            ):
                report = module.build_report()
        finally:
            overlay_path.unlink(missing_ok=True)
            (overlay_home / ".codex").rmdir()
            overlay_home.rmdir()

        self.assertEqual(report["sections"]["external_hook_overlay"]["status"], "present")
        self.assertIn("external hook overlay", report["sections"]["external_hook_overlay"]["evidence"][0])

    def test_non_xcrun_bridge_declaration_is_degraded(self) -> None:
        module = load_module("codex_runtime_doctor_bridge_decl", DOCTOR_PATH)
        with mock.patch.object(module, "MCP_PATH", ROOT / "tests" / "mcp-invalid.json"), mock.patch.object(
            module, "run_command", side_effect=[completed(stdout="Codex support validation passed.")]
        ), mock.patch.object(module.platform, "system", return_value="Darwin"), mock.patch.object(
            module.Path, "home", return_value=Path("/tmp/no-overlay-home")
        ):
            module.MCP_PATH.write_text(json.dumps({"mcpServers": {"xcode": {"command": "python3", "args": ["bridge.py"]}}}))
            try:
                report = module.build_report()
            finally:
                module.MCP_PATH.unlink(missing_ok=True)

        self.assertEqual(report["sections"]["xcode_bridge"]["status"], "degraded")
        self.assertIn("xcrun mcpbridge", report["sections"]["xcode_bridge"]["evidence"][0])

    def test_session_start_matcher_drift_is_degraded(self) -> None:
        module = load_module("codex_runtime_doctor_session_start", DOCTOR_PATH)
        with TemporaryDirectory() as temp_dir:
            hooks_path = Path(temp_dir) / "hooks.json"
            hooks_path.write_text(
                json.dumps(
                    {
                        "hooks": {
                            "SessionStart": [
                                {
                                    "matcher": "all",
                                    "hooks": [
                                        {
                                            "type": "command",
                                            "command": '/usr/bin/python3 ".codex/hooks/session_context.py"',
                                        }
                                    ],
                                }
                            ],
                            "PreToolUse": [
                                {
                                    "matcher": "Bash",
                                    "hooks": [
                                        {
                                            "type": "command",
                                            "command": '/usr/bin/python3 ".codex/hooks/pre_tool_use_policy.py"',
                                        }
                                    ],
                                }
                            ],
                            "PostToolUse": [
                                {
                                    "matcher": "Bash",
                                    "hooks": [
                                        {
                                            "type": "command",
                                            "command": '/usr/bin/python3 ".codex/hooks/post_tool_use_policy.py"',
                                        }
                                    ],
                                }
                            ],
                            "Stop": [
                                {
                                    "hooks": [
                                        {
                                            "type": "command",
                                            "command": '/usr/bin/python3 ".codex/hooks/stop_validate_codex_surface.py"',
                                        }
                                    ],
                                }
                            ],
                        }
                    }
                )
            )
            with mock.patch.object(module, "HOOKS_PATH", hooks_path), mock.patch.object(
                module, "run_command", side_effect=[
                    completed(stdout="Codex support validation passed."),
                    completed(stdout="/Applications/Xcode.app/Contents/Developer/usr/bin/xcodebuild"),
                    completed(stdout="/Applications/Xcode.app/Contents/Developer/usr/bin/mcpbridge"),
                ]
            ), mock.patch.object(module.platform, "system", return_value="Darwin"), mock.patch.object(
                module.Path, "home", return_value=Path("/tmp/no-overlay-home")
            ):
                report = module.build_report()

        self.assertEqual(report["sections"]["repo_hooks"]["status"], "degraded")
        self.assertIn("startup/resume", report["sections"]["repo_hooks"]["evidence"][0])

    def test_missing_xcrun_gets_targeted_remediation(self) -> None:
        module = load_module("codex_runtime_doctor_missing_xcrun", DOCTOR_PATH)
        with mock.patch.object(module, "run_command", side_effect=[
            completed(stdout="Codex support validation passed."),
            completed(stderr="xcrun: error: unable to find utility 'xcodebuild'", returncode=1),
        ]), mock.patch.object(module.platform, "system", return_value="Darwin"), mock.patch.object(
            module.Path, "home", return_value=Path("/tmp/no-overlay-home")
        ):
            report = module.build_report()

        self.assertEqual(report["sections"]["xcode_bridge"]["status"], "unavailable")
        self.assertIn("Install Xcode command line tools", report["sections"]["xcode_bridge"]["remediation"][0])


if __name__ == "__main__":
    unittest.main()
