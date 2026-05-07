#!/usr/bin/env bash
set -euo pipefail

script_path=${1:?usage: run_python_hook.sh <script-path> [args...]}
shift

supports_tomllib() {
	"$1" - <<'PY' >/dev/null 2>&1
import tomllib
PY
}

find_python() {
	local candidate
	local -a candidates=(
		"/opt/homebrew/bin/python3"
		"/usr/local/bin/python3"
	)
	if command -v python3 >/dev/null 2>&1; then
		candidates+=("$(command -v python3)")
	fi
	for candidate in "${candidates[@]}"; do
		if [[ -x "${candidate}" ]] && supports_tomllib "${candidate}"; then
			printf '%s\n' "${candidate}"
			return 0
		fi
	done
	return 1
}

python_bin=$(find_python) || {
	echo "No python3 with tomllib support found; install Python 3.11+ or expose it" >&2
	echo "at /opt/homebrew/bin/python3 or /usr/local/bin/python3." >&2
	exit 1
}

exec "${python_bin}" "${script_path}" "$@"
