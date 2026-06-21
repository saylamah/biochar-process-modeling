"""Cantera reactor utilities for simplified biomass-to-biochar examples."""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import Iterable

import pandas as pd

from .feedstock import AirFeed, BiomassFeed, cantera_mass_fractions


DEFAULT_MECHANISM = Path(__file__).resolve().parents[2] / "mechanisms" / "Wood_pyrolysis.yaml"
DEFAULT_SPECIES = ("WOOD", "CHAR", "TAR", "CO", "CO2", "H2", "CH4", "H2O", "O2", "N2")


@dataclass(frozen=True)
class ReactorCase:
    """Simplified constant-pressure reactor case definition."""

    temperature_k: float = 1063.15
    pressure_pa: float = 95_325.0
    biomass_kg_h: float = 100.0
    air_kg_h: float = 466.0
    moisture_fraction: float = 0.10
    ash_fraction: float = 0.015
    time_s: float = 1800.0
    step_s: float = 10.0
    mechanism_path: Path = DEFAULT_MECHANISM


def run_case(case: ReactorCase, species: Iterable[str] = DEFAULT_SPECIES) -> pd.DataFrame:
    """Run a simplified ideal constant-pressure reactor case.

    Returns a table with time and selected species mass-flow estimates in kg/h
    on the reactive inlet basis. Ash is not included in the mechanism and must be
    tracked separately.
    """

    try:
        import cantera as ct
    except ModuleNotFoundError as exc:
        raise ModuleNotFoundError(
            "Cantera is required to run this model. Install it with conda or pip "
            "using the repository environment files."
        ) from exc

    mechanism_path = Path(case.mechanism_path)
    if not mechanism_path.exists():
        raise FileNotFoundError(f"Mechanism file not found: {mechanism_path}")

    feed = BiomassFeed(
        biomass_kg_h=case.biomass_kg_h,
        moisture_fraction=case.moisture_fraction,
        ash_fraction=case.ash_fraction,
    )
    air = AirFeed(air_kg_h=case.air_kg_h)
    inlet_y, basis_kg_h = cantera_mass_fractions(feed, air)

    gas = ct.Solution(str(mechanism_path))
    gas.TPY = case.temperature_k, case.pressure_pa, inlet_y

    reactor = ct.IdealGasConstPressureReactor(gas)
    network = ct.ReactorNet([reactor])

    selected_species = tuple(species)
    missing = [name for name in selected_species if name not in gas.species_names]
    if missing:
        raise ValueError(f"Species not found in mechanism: {missing}")

    rows: list[dict[str, float]] = []
    time = 0.0
    while time <= case.time_s + 1e-12:
        network.advance(time)
        row = {
            "time_s": time,
            "time_min": time / 60.0,
            "temperature_k": reactor.T,
            "pressure_pa": reactor.thermo.P,
            "reactive_basis_kg_h": basis_kg_h,
            "external_ash_kg_h": feed.ash_kg_h,
        }
        for name in selected_species:
            row[f"{name}_kg_h"] = basis_kg_h * reactor.thermo.Y[gas.species_index(name)]
        rows.append(row)
        time += case.step_s

    return pd.DataFrame(rows)


def save_case_results(case: ReactorCase, output_path: Path, species: Iterable[str] = DEFAULT_SPECIES) -> Path:
    """Run a case and save results as CSV."""

    output_path = Path(output_path)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    df = run_case(case, species=species)
    df.to_csv(output_path, index=False)
    return output_path
