import json
import subprocess


class GhError(RuntimeError):
    """Raised when a `gh` CLI command fails, with stderr included in the message."""


def _run(args):
    result = subprocess.run(["gh", *args], capture_output=True, text=True)

    if result.returncode != 0:
        raise GhError(result.stderr.strip() or f"gh {' '.join(args)} failed")

    return result


def run_gh(args):
    """Run a `gh` CLI command, raising GhError with stderr if it fails."""

    _run(args)


def run_gh_json(args):
    """Run a `gh` CLI command and parse its stdout as JSON."""

    result = _run(args)

    return json.loads(result.stdout)
