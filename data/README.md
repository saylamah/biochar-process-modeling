# Data

This folder contains a curated, lightweight subset of Cantera simulation outputs for the `biochar-process-modeling` repository.

## Scope

The selected CSV files are reduced versions of larger simulation result files. They are provided to support reproducibility of qualitative trends in biomass conversion, biochar formation, and gas-product evolution.

The files are **simulated reactor outputs**, not experimental measurements. They should not be interpreted as experimentally validated design data for industrial-scale biochar plants.

The selected CSV files are stored inside `data/curated/` and organized by sensitivity group. Open the `curated/` folder to access the individual CSV files for moisture, temperature, and O₂/N₂ atmosphere cases.

## Curated columns

Each curated CSV contains:

- `time_s` — simulation time coordinate from the original output.
- `temperature_K` — reactor state temperature in Kelvin.
- `density_kg_per_m3` — reactor gas density.
- `Y_WOOD`, `Y_CHAR`, `Y_TAR` — selected solid/lumped biomass-conversion species mass fractions.
- `Y_O2`, `Y_N2`, `Y_H2O`, `Y_H2O_L` — selected oxidizer/inert/water mass fractions.
- `Y_CO`, `Y_CO2`, `Y_H2`, `Y_CH4` — selected gas-product mass fractions.

Absolute mass rates require the corresponding total stream mass-flow basis from the model setup. The curated data intentionally preserve mass fractions rather than imposing a possibly inconsistent mass-flow basis.

## Case groups

```text
data/curated/
├── moisture_sweep_T790_O2-N2-23-77/
├── temperature_sweep_H2O10_O2-N2-23-77/
└── oxygen_sweep_H2O10_T790/
```

The file `manifest_simulation_cases.csv` documents the source file, case labels, row count, time range, selected columns, and selected summary indicators for each case.

## Important temperature-unit note

The historical scripts and result filenames use labels such as `T790`. The original Python script assigns `tk = 790.0` and passes this value to Cantera as Kelvin, while the associated publication figures discuss treatment temperatures such as 780, 790, and 800 °C. This repository therefore treats the temperature labels as **historical case labels until the original input basis is fully verified**.

## Numerical artifacts

Very small negative mass fractions may appear in some outputs due to numerical solver tolerances. These values should be treated as numerical artifacts, not physically meaningful negative concentrations.

## Recommended use

Use these curated files for:

- plotting biomass and biochar evolution;
- comparing moisture sensitivity;
- comparing temperature sensitivity;
- comparing O2/N2 atmosphere sensitivity;
- checking qualitative trends in CO, H2, CH4, and CO2 formation.

Do not use these files for:

- industrial design guarantees;
- equipment sizing;
- certified carbon-credit calculations;
- investment-grade techno-economic assessment;
- regulatory emission reporting.
