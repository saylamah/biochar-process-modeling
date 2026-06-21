"""Minimal Python example for running the base biomass-to-biochar case."""

from pathlib import Path

from biochar_model.cantera_reactor import ReactorCase, save_case_results

case = ReactorCase(
    temperature_k=1063.15,  # 790 °C expressed in Kelvin
    biomass_kg_h=100.0,
    air_kg_h=466.0,
    moisture_fraction=0.10,
    ash_fraction=0.015,
    time_s=1800.0,
    step_s=10.0,
)

save_case_results(case, Path("results/base_case.csv"))
