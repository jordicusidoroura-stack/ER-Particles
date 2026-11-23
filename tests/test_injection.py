"""Injection and regression tests for the thermal-law notebooks (12 and 13)."""
import re
from pathlib import Path

from test_notebooks import ROOT, run

NB12 = ROOT / "notebooks" / "12_leyes_termicas_de_horizonte.ipynb"
NB13 = ROOT / "notebooks" / "13_escala_y_redshift.ipynb"

# Replace the synthetic dark-matter galaxies by galaxies that obey the Bose law
# with s = a_Lambda / 2pi, before the discovery/held-out split is made.
INJECT_BOSE = r'''
_s0 = 8.626e-11
for _k, _g in GAL.items():
    _gN = (_g["vgas2"] + 0.5 * _g["vstar2"]) / _g["r"] * (1e6 / 3.0857e19)
    _x = np.sqrt(np.clip(_gN, 1e-16, None) / _s0)
    _v = np.sqrt(_gN / (-np.expm1(-_x)) * _g["r"] / (1e6 / 3.0857e19))
    _g["vobs"] = _v + RNG.normal(0, 1, len(_v)) * _g["err"]
print("INJECTED: Bose law, s = a_Lambda/2pi")
'''


def test_nb12_recovers_injected_scale(tmp_path):
    (tmp_path / "inject.py").write_text(INJECT_BOSE)
    out = run(NB12, tmp_path, "--inject-before", "import hashlib", "--inject", "inject.py")
    assert "INJECTED" in out
    ratios = re.search(r"2\) Robustez.*= ([\d\., ]+) →", out).group(1)
    vals = [float(v) for v in ratios.split(",")]
    assert all(0.8 <= v <= 1.25 for v in vals), vals
    assert re.search(r"1\) Grupo reservado.*✓", out)
    assert re.search(r"3\) Sistema Solar.*✓", out)


def test_nb12_null_does_not_claim_cosmological_scale(tmp_path):
    out = run(NB12, tmp_path)
    assert "LA COSMOLOGÍA FIJA LA ESCALA" not in out


def test_nb13_redshift_fits_published_bins(tmp_path):
    # Part B uses the published MUSE-DARK bins, so its numbers are real even offline.
    out = run(NB13, tmp_path)
    m = re.search(r"Barras = 1σ: p\(Λ constante\) = ([\d\.e\-\+]+) \| p\(H\) = ([\d\.e\-\+]+) \| amplitud H f = ([\d\.]+)", out)
    pL, pH, f = float(m.group(1)), float(m.group(2)), float(m.group(3))
    assert pL < 1e-4
    assert pH > 0.05
    assert abs(f - 1.33) < 0.02
