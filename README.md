# Biomass Process Modeling

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.20841046.svg)](https://doi.org/10.5281/zenodo.20841046)

Simplified engineering models, Cantera-based reactor examples, curated simulation data, and technical notes for biomass conversion, biochar production, heat generation, syngas formation, and screening-level carbon-management assessment.

This repository is being developed as an open technical companion to selected publications by Ahmad Saylam on biomass conversion, thermochemical process development, waste-to-X pathways, biochar, syngas, and preliminary carbon-credit potential.

## Repository status

**Initial public technical repository.**

The repository contains:

- a cleaned repository structure;
- selected source-publication references;
- a wood-pyrolysis mechanism file;
- the original uploaded simulation script;
- a refactored Python entry point for future reproducible simulations;
- curated simulation CSV data for selected sensitivity cases;
- documentation on model consistency, assumptions, limitations, and validation needs.

The current model should be treated as a **screening and process-orientation tool**, not as an experimentally validated design basis.

Experimental validation, parameter review, unit-consistency checks, mass-balance checks, and sensitivity testing remain part of the development roadmap.

## Technical scope

The repository focuses on four connected questions:

1. How do temperature, moisture content, oxygen exposure, and residence time influence biomass-to-biochar conversion?
2. How do drying, pyrolysis, partial oxidation, char conversion, and gas formation interact in a simplified reactor model?
3. How can syngas use, heat supply, and emissions be compared across different thermochemical treatment concepts?
4. How can biochar and pyrogenic carbon be discussed responsibly in the context of carbon management and preliminary carbon-credit potential?

## Scientific basis

The initial repository is based on three related technical outputs:

- **Enhancing Biomass Conversion: Advanced Modelling and Process Optimization for Efficient Biochar and Heat Production**  
  DOI: `10.5281/zenodo.19438451`

- **Advancing Waste-to-X Technologies: Sustainable Thermochemical Pathways for Biomass Valorization and Carbon Credit Potential**  
  DOI: `10.5281/zenodo.19785243`

- **Thermochemical Process Development: From Mechanism to Scale-Up and Industrial Adoption**  
  DOI: `10.5281/zenodo.20760609`

## Repository layout

```text
biochar-process-modeling/
├── README.md
├── CITATION.cff
├── LICENSE
├── LICENSE_NOTES.md
├── MANIFEST.md
├── pyproject.toml
├── requirements.txt
├── environment.yml
├── data/
│   ├── README.md
│   ├── manifest_simulation_cases.csv
│   └── curated/
│       ├── moisture_sweep_T790_O2-N2-23-77/
│       ├── temperature_sweep_H2O10_O2-N2-23-77/
│       └── oxygen_sweep_H2O10_T790/
├── docs/
│   ├── model_scope.md
│   ├── assumptions_and_limitations.md
│   ├── carbon_credit_caution.md
│   ├── model_consistency_notes.md
│   ├── model_validation_plan.md
│   ├── publications.md
│   ├── repository_roadmap.md
│   ├── github_profile_snippet.md
│   └── source_publications/
├── mechanisms/
│   ├── Wood_pyrolysis.yaml
│   └── Wood_pyrolysis.cti
├── originals/
│   └── blasi_original.py
├── src/
│   └── biochar_model/
│       ├── __init__.py
│       ├── cantera_reactor.py
│       ├── feedstock.py
│       └── carbon_screening.py
├── scripts/
│   └── run_biochar_case.py
├── examples/
│   └── run_base_case.py
├── notebooks/
│   └── README.md
└── tests/
    └── test_feedstock.py
```

## Using the curated data

This repository includes selected, reduced Cantera simulation outputs that can be inspected without running the full Cantera reactor model.

These curated CSV files support qualitative review of:

- biomass conversion;
- biochar formation;
- moisture sensitivity;
- temperature sensitivity;
- oxygen/inert-gas sensitivity;
- carbon monoxide, hydrogen, methane, and carbon dioxide evolution.

The selected CSV files are stored inside `data/curated/` and organized by sensitivity group. Open the `curated/` folder to access the individual CSV files for moisture, temperature, and O2/N2 atmosphere cases.

The curated data are organized in:

- `data/curated/moisture_sweep_T790_O2-N2-23-77/`
- `data/curated/temperature_sweep_H2O10_O2-N2-23-77/`
- `data/curated/oxygen_sweep_H2O10_T790/`

A case overview is provided in:

- `data/manifest_simulation_cases.csv`

Additional notes are provided in:

- `data/README.md`
- `docs/model_consistency_notes.md`
- `docs/model_validation_plan.md`

The data are simulated reactor outputs, not experimental measurements. They are provided for screening-level analysis, documentation, and reproducibility of qualitative trends. They should not be interpreted as experimentally validated design data for industrial-scale biochar plants.

## Quick start

Create an environment and install the required packages:

```bash
conda env create -f environment.yml
conda activate biochar-carbon
```

or with pip:

```bash
python -m venv .venv
source .venv/bin/activate

# Windows:
# .venv\Scripts\activate

pip install -r requirements.txt
```

Run the first example:

```bash
python scripts/run_biochar_case.py --temperature-k 1063.15 --biomass-kg-h 100 --air-kg-h 466 --moisture 0.10 --ash 0.015 --time-s 1800 --output results/base_case.csv
```

The mechanism file is stored in:

```text
mechanisms/Wood_pyrolysis.yaml
```

The original uploaded script is preserved in:

```text
originals/blasi_original.py
```

## Important technical note on temperature units

The original script uses:

```python
tk = 790.0
```

and passes this value to Cantera as Kelvin.

Some publication figures and captions discuss temperatures such as 780, 790, and 800 °C. Before claiming exact reproduction of the published figures, the temperature basis must be checked and documented.

For example:

```text
790 °C = 1063.15 K
```

See:

```text
docs/model_consistency_notes.md
```

## Development roadmap

The next recommended development steps are:

1. Clean and verify the README, data structure, and documentation.
2. Add plotting scripts for the curated CSV data.
3. Verify unit consistency and reproduce the baseline biomass/biochar mass-rate figure.
4. Convert the original script into parameterized simulation functions.
5. Add sensitivity runs for temperature, moisture, and O2/N2 atmosphere.
6. Export reproducible CSV results and publication-quality figures.
7. Add a screening-level carbon-management module for the three thermochemical cases.
8. Add notebooks for educational and technical communication.
9. Validate model behavior against experimental or literature data where possible.

## Responsible use

This repository does not certify carbon credits and does not provide investment-grade process design.

It supports transparent modeling, engineering interpretation, and early-stage process comparison.

Carbon-credit discussions are treated as screening-level and must be supported by full system boundaries, durable carbon storage evidence, emissions accounting, monitoring, reporting, and verification before any formal claim is made.

## License

This repository is distributed under the MIT License unless otherwise stated. See:

```text
LICENSE
LICENSE_NOTES.md
```

## Citation

Citation metadata are provided in:

```text
CITATION.cff
```
