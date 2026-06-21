"""Screening-level carbon-management utilities.

These functions are intentionally simple. They are not a certified carbon-credit
methodology and should not be presented as one.
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class BiocharCarbonScreen:
    """Screening calculation for carbon retained in biochar."""

    biochar_kg_h: float
    biochar_carbon_fraction: float = 0.75
    durable_fraction: float = 0.80

    def carbon_retained_kg_h(self) -> float:
        return self.biochar_kg_h * self.biochar_carbon_fraction * self.durable_fraction

    def co2_equivalent_retained_kg_h(self) -> float:
        return self.carbon_retained_kg_h() * 44.0 / 12.0


def net_direct_co2_screening(
    biochar_kg_h: float,
    direct_co2_emissions_kg_h: float,
    biochar_carbon_fraction: float = 0.75,
    durable_fraction: float = 0.80,
) -> float:
    """Return screening-level retained CO2 equivalent minus direct CO2 emissions.

    This excludes upstream emissions, downstream emissions, leakage, monitoring,
    verification, baseline selection, permanence risk, and market-methodology rules.
    """

    retained = BiocharCarbonScreen(
        biochar_kg_h=biochar_kg_h,
        biochar_carbon_fraction=biochar_carbon_fraction,
        durable_fraction=durable_fraction,
    ).co2_equivalent_retained_kg_h()
    return retained - direct_co2_emissions_kg_h
