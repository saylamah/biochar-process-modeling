# Model Validation Plan

This plan defines the minimum technical checks needed before the repository can claim reproducible model behavior beyond an initial public scaffold.

## Stage 1 — File and environment reproducibility

- Confirm that the Cantera mechanism loads without errors.
- Confirm that the refactored scripts run from a clean environment.
- Confirm that output folders are created automatically.
- Confirm that generated CSV files use stable, documented column names.

## Stage 2 — Baseline case reproduction

- Run the baseline biomass-to-biochar case.
- Plot `Y_WOOD` and `Y_CHAR` versus time.
- Compare the qualitative conversion profile with the published biomass/biochar trend.
- Check that the final values are physically interpretable.

## Stage 3 — Moisture sensitivity

Use the curated moisture-sweep data:

```text
data/curated/moisture_sweep_T790_O2-N2-23-77/
```

Check whether increasing moisture content produces the expected qualitative changes in biomass conversion and biochar formation.

## Stage 4 — Temperature sensitivity

Use the curated temperature-sweep data:

```text
data/curated/temperature_sweep_H2O10_O2-N2-23-77/
```

Before final interpretation, verify whether labels such as `T780`, `T790`, and `T800` refer to Kelvin inputs, Celsius targets, or historical case names.

## Stage 5 — Oxygen/inert-gas sensitivity

Use the curated oxygen-sweep data:

```text
data/curated/oxygen_sweep_H2O10_T790/
```

Compare `Y_CHAR`, `Y_CO`, `Y_CO2`, `Y_H2`, and `Y_CH4` across O2/N2 ratios of 0/100, 5/95, 10/90, and 23/77.

## Stage 6 — Mass-balance and numerical checks

- Check that selected mass fractions remain bounded within numerical tolerance.
- Identify tiny negative values caused by solver tolerance.
- Check whether major species account for a reasonable fraction of total mass.
- Document any unclosed material balance due to excluded species.

## Stage 7 — Publication comparison

For each figure targeted for reproduction:

- document the original case conditions;
- document the exact input parameters used in the script;
- generate a figure from the curated or regenerated data;
- state whether the comparison is qualitative, semi-quantitative, or quantitative.

## Stage 8 — Experimental validation boundary

The current data are simulated data. Future validation should compare model predictions with laboratory or pilot-scale measurements for:

- biochar yield;
- gas composition;
- moisture effect;
- oxygen exposure effect;
- residence-time dependence;
- carbon retention and ash behavior.
