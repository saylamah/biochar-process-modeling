#!/usr/bin/env python
"""Run a simplified biomass-to-biochar reactor case and save CSV results."""

from __future__ import annotations

import argparse
from pathlib import Path

from biochar_model.cantera_reactor import ReactorCase, save_case_results


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--temperature-k", type=float, default=1063.15, help="Reactor temperature in Kelvin.")
    parser.add_argument("--pressure-pa", type=float, default=95325.0, help="Pressure in Pa.")
    parser.add_argument("--biomass-kg-h", type=float, default=100.0, help="Wet biomass feed rate in kg/h.")
    parser.add_argument("--air-kg-h", type=float, default=466.0, help="Air feed rate in kg/h.")
    parser.add_argument("--moisture", type=float, default=0.10, help="Wet-basis moisture fraction.")
    parser.add_argument("--ash", type=float, default=0.015, help="Wet-basis ash fraction.")
    parser.add_argument("--time-s", type=float, default=1800.0, help="Simulation time in seconds.")
    parser.add_argument("--step-s", type=float, default=10.0, help="Output time step in seconds.")
    parser.add_argument("--mechanism", type=Path, default=Path("mechanisms/Wood_pyrolysis.yaml"), help="Cantera YAML mechanism path.")
    parser.add_argument("--output", type=Path, default=Path("results/base_case.csv"), help="Output CSV path.")
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    case = ReactorCase(
        temperature_k=args.temperature_k,
        pressure_pa=args.pressure_pa,
        biomass_kg_h=args.biomass_kg_h,
        air_kg_h=args.air_kg_h,
        moisture_fraction=args.moisture,
        ash_fraction=args.ash,
        time_s=args.time_s,
        step_s=args.step_s,
        mechanism_path=args.mechanism,
    )
    output = save_case_results(case, args.output)
    print(f"Saved results to {output}")


if __name__ == "__main__":
    main()
