"""Smoke tests: every notebook runs end to end on synthetic data, offline."""
import subprocess
import sys
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[1]
NOTEBOOKS = sorted((ROOT / "notebooks").glob("*.ipynb"))
RUNNER = ROOT / "tests" / "nbrun.py"


def run(nb, tmp_path, *extra, timeout=1800):
    res = subprocess.run([sys.executable, str(RUNNER), str(nb), *extra], cwd=tmp_path,
                         capture_output=True, text=True, timeout=timeout)
    assert res.returncode == 0, f"{nb.name} failed:\n{res.stdout[-3000:]}\n{res.stderr[-3000:]}"
    return res.stdout


@pytest.mark.parametrize("nb", NOTEBOOKS, ids=[p.stem for p in NOTEBOOKS])
def test_notebook_runs(nb, tmp_path):
    out = run(nb, tmp_path)
    assert "SINTÉTIC" in out or "sintétic" in out or nb.stem.startswith(("07", "10")), \
        "expected the offline run to fall back to synthetic data"
