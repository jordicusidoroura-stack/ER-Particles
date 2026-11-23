# ER-Particles

**Can entanglement mimic dark matter? A speculative idea, tested step by step against real galaxies.**

This repository follows one idea from its first formulation to the version that survives contact with data, in 13 notebooks that run in Google Colab. It started from ER=EPR (entangled particles joined by Einstein–Rosen bridges) and ended with a thermal law for galaxy rotation whose scale is set by the temperature of the cosmic horizon.

It is a companion to the educational course [quantum-vacuum-journey](https://github.com/jordicusidoroura-stack/quantum-vacuum-journey).

## The result in one paragraph

Rotating galaxies are well described by a law of Bose–Einstein form,

```
a = g_N / (1 − exp(−√(g_N / s)))        with   s(z) = c·H(z) / 2π
```

where g_N is the Newtonian acceleration of the visible matter and s is fixed by the temperature ħH/2π of the cosmic apparent horizon, with no free acceleration parameter. On 149 SPARC galaxies the fitted scale is s ≈ 0.93 × 10⁻¹⁰ m/s² (0.89 × cH₀/2π). A version with that scale fixed in advance predicts held-out galaxies as well as a fitted one. The correction vanishes in the Solar System (≈10⁻³⁸² m/s² at Saturn). Published intermediate-redshift data (MUSE-DARK, 2026) reject a constant scale and are compatible with s ∝ H(z).

**What is not new:** the functional form is the empirical radial acceleration relation (McGaugh, Lelli & Schombert 2016), the coincidence a₀ ≈ cH₀/2π is Milgrom's, and the evolution with H(z) has been proposed and measured by others. What this project adds is a thermal reading that links them, a systematic pre-registered comparison of laws and scales, and the whole path, failures included, in reproducible form.

## The path, notebook by notebook

| # | Notebook | Question | Outcome |
|---|---|---|---|
| 01 | [Bridges and dark matter](notebooks/01_puentes_ER_y_materia_oscura.ipynb) | Can an ER-bridge term fit rotation curves? Error estimates against Verlinde and NFW. | Baryons alone fall short; sets up the model. |
| 02 | [Global fit and overfitting](notebooks/02_ajuste_global_y_sobreajuste.ipynb) | Do global parameters survive cross-validation? | First global fit, cross-validation and extrapolation. |
| 03 | [Non-linear model and RAR](notebooks/03_modelo_no_lineal_y_RAR.ipynb) | Does a coupling κ(g) beat the RAR? | Compared directly with the RAR. |
| 04 | [Non-local RAR](notebooks/04_RAR_no_local.ipynb) | Does a bridge range λ improve the RAR? | Apparent signal, λ ≈ 0.7 kpc. |
| 05 | [Physical or instrumental λ](notebooks/05_lambda_fisica_o_instrumental.ipynb) | Is λ a property of galaxies or of the data? | Tested against instrumental resolution models. |
| 06 | [Disc geometry, QUMOND, 3D](notebooks/06_disco_QUMOND_3D.ipynb) | Does λ survive a proper disc geometry? | Mixed. |
| 07 | [Geometry of entanglement](notebooks/07_geometria_del_entrelazamiento.ipynb) | Does entanglement build geometry in a toy model? | Yes (chains, TFD, emergent distance, first law), but no extra mass term. |
| 08 | [Independent validation](notebooks/08_validacion_independiente.ipynb) | Does λ ≈ 0.7 kpc survive a pre-registered held-out test? | **No** (p = 0.34). |
| 09 | [Dust and systematics](notebooks/09_polvo_y_sistematicos.ipynb) | Could dust explain the failure, or the signal? | No; clean subsample p = 0.15. |
| 10 | [Summing distortions](notebooks/10_suma_de_distorsiones.ipynb) | Can bridge distortions add up to a halo? | Only if concentrated where g ≲ 10⁻¹⁰ m/s². |
| 11 | [Acceleration and horizons](notebooks/11_aceleracion_y_horizontes.ipynb) | Does a horizon-temperature law (Milgrom 1999) work? | Right weak-field form, but it never switches off (ΔBIC 569). |
| 12 | [Thermal horizon laws](notebooks/12_leyes_termicas_de_horizonte.ipynb) | Does a thermal (Bose) law with a cosmological scale work, with nothing fitted? | **All 4 pre-registered criteria pass.** |
| 13 | [Scale and redshift](notebooks/13_escala_y_redshift.ipynb) | Constant scale (Λ) or one that tracks H(z)? | Local data cannot tell; redshift data favour H(z). |

Open any notebook in Colab: replace `github.com` with `colab.research.google.com/github` in its URL, or use
`https://colab.research.google.com/github/jordicusidoroura-stack/ER-Particles/blob/main/notebooks/<name>.ipynb`.

## Method

Every test from notebook 08 on follows the same rules:

1. **Pre-registration.** Hypotheses, fixed scales and pass–fail thresholds are written in the notebook before it is run on real data. Any later change is stated in the text.
2. **Held-out galaxies.** A hash of each galaxy's name splits SPARC into discovery and held-out halves. Nothing is tuned on the held-out half.
3. **Injection tests.** Synthetic galaxies with a planted law check that the pipeline recovers it, and synthetic dark-matter galaxies check that it does not invent it.
4. **Varying the assumptions.** Stellar mass-to-light priors, bulge masses, distances and inclinations are varied to see how much each result moves.

## Data

- **SPARC** rotation curves and mass models (Lelli, McGaugh & Schombert 2016, [AJ 152, 157](https://arxiv.org/abs/1606.09251)), downloaded at runtime from astroweb.case.edu/SPARC. In Colab, if the download fails, the notebook asks you to upload `Rotmod_LTG.zip`. Not redistributed here.
- **MUSE-DARK** redshift bins (Ciocan et al. 2026, [A&A 709, L16](https://arxiv.org/abs/2604.22613)), as tabulated in Alcock 2026 ([arXiv:2609.38796](https://arxiv.org/abs/2609.38796)). Four values typed into notebook 13, with their source.

Without network access every notebook falls back to synthetic galaxies and says so in its output. Those runs check the code only; they have no physical meaning.

## Running the tests

```bash
pip install -r requirements.txt
pytest -q tests
```

The tests run every notebook offline on synthetic data (about 3 minutes in total) and check three results:

- notebook 12 recovers a Bose law injected at s = a_Λ/2π, and passes its held-out and Solar System criteria;
- notebook 12 does not claim a cosmological scale for dark-matter galaxies;
- notebook 13 reproduces the redshift fits on the published bins (constant scale rejected, H(z) compatible, amplitude 1.33).

GitHub Actions runs the same tests on every push.

## Status and open problems

- The Bose factor and the variable √(g_N/s) are a reading of the data, not yet derived from entanglement across two horizons.
- Nothing here addresses lensing, galaxy clusters or the cosmic microwave background.
- The amplitude of s differs between SPARC and MUSE-DARK by a factor of 1.33; mass calibration or physics is open.
- A paper draft (pedagogical, in English) is in preparation.

## Licence

Code and notebooks: [MIT](LICENSE). Data belong to their authors; cite the original papers above.
