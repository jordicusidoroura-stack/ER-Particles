"""Run a notebook's code cells as a plain script, offline, with synthetic data.

The notebooks try to download SPARC; here every network call fails on purpose,
so each notebook falls back to its built-in synthetic galaxies. Figures are
saved as PNG files instead of being shown.

Usage: python tests/nbrun.py notebooks/12_leyes_termicas_de_horizonte.ipynb [--inject-before TEXT --inject FILE]
"""
import json
import sys
from pathlib import Path

PRELUDE = r'''
import urllib.request as _ur
def _offline(*a, **k):
    raise OSError("offline test run")
_ur.urlopen = _offline
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
_fig = [0]
def _show(*a, **k):
    _fig[0] += 1
    plt.savefig(f"fig{_fig[0]:02d}.png", bbox_inches="tight")
    plt.close("all")
plt.show = _show
try:
    import plotly.io as _pio
    _pio.renderers.default = "json"
    import plotly.graph_objects as _go
    _go.Figure.show = lambda self, *a, **k: self.write_html(f"plotly{id(self)}.html")
except Exception:
    pass
def display(*a, **k):
    for x in a:
        print(x)
'''


def notebook_script(path, inject_before=None, inject_code=""):
    nb = json.loads(Path(path).read_text(encoding="utf-8"))
    parts = [PRELUDE]
    for cell in nb["cells"]:
        if cell["cell_type"] != "code":
            continue
        src = "".join(cell["source"])
        src = "\n".join(l for l in src.splitlines() if not l.lstrip().startswith(("!", "%")))
        if inject_before and inject_before in src:
            src = src.replace(inject_before, inject_code + "\n" + inject_before, 1)
            inject_before = None
        parts.append(src)
    if inject_before:
        raise ValueError("injection point not found")
    return "\n\n".join(parts)


if __name__ == "__main__":
    args = sys.argv[1:]
    nb = args[0]
    before = args[args.index("--inject-before") + 1] if "--inject-before" in args else None
    code = Path(args[args.index("--inject") + 1]).read_text() if "--inject" in args else ""
    exec(compile(notebook_script(nb, before, code), nb, "exec"), {"__name__": "__main__"})
