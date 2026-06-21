"""Feedstock and inlet-stream utilities for biomass conversion examples."""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class BiomassFeed:
    """Biomass feed definition.

    Parameters
    ----------
    biomass_kg_h:
        Total wet biomass feed rate, including moisture and ash.
    moisture_fraction:
        Wet-basis moisture fraction, e.g. 0.10 for 10 wt%.
    ash_fraction:
        Wet-basis ash fraction, e.g. 0.015 for 1.5 wt%.
    """

    biomass_kg_h: float = 100.0
    moisture_fraction: float = 0.10
    ash_fraction: float = 0.015

    def __post_init__(self) -> None:
        if self.biomass_kg_h <= 0:
            raise ValueError("biomass_kg_h must be positive.")
        if not (0 <= self.moisture_fraction < 1):
            raise ValueError("moisture_fraction must be in [0, 1).")
        if not (0 <= self.ash_fraction < 1):
            raise ValueError("ash_fraction must be in [0, 1).")
        if self.moisture_fraction + self.ash_fraction >= 1:
            raise ValueError("moisture_fraction + ash_fraction must be less than 1.")

    @property
    def water_kg_h(self) -> float:
        return self.biomass_kg_h * self.moisture_fraction

    @property
    def ash_kg_h(self) -> float:
        return self.biomass_kg_h * self.ash_fraction

    @property
    def dry_reactive_wood_kg_h(self) -> float:
        return self.biomass_kg_h - self.water_kg_h - self.ash_kg_h


@dataclass(frozen=True)
class AirFeed:
    """Air feed represented by O2/N2 mass fractions."""

    air_kg_h: float = 466.0
    oxygen_mass_fraction: float = 0.23
    nitrogen_mass_fraction: float = 0.77

    def __post_init__(self) -> None:
        if self.air_kg_h < 0:
            raise ValueError("air_kg_h must be non-negative.")
        if abs((self.oxygen_mass_fraction + self.nitrogen_mass_fraction) - 1.0) > 1e-9:
            raise ValueError("oxygen_mass_fraction + nitrogen_mass_fraction must equal 1.")

    @property
    def oxygen_kg_h(self) -> float:
        return self.air_kg_h * self.oxygen_mass_fraction

    @property
    def nitrogen_kg_h(self) -> float:
        return self.air_kg_h * self.nitrogen_mass_fraction


def cantera_mass_fractions(feed: BiomassFeed, air: AirFeed) -> tuple[dict[str, float], float]:
    """Return normalized Cantera mass fractions and the reactive inlet basis.

    Ash is not included in the supplied mechanism and is therefore not included
    in the Cantera mass-fraction dictionary. It can be tracked separately.
    """

    basis_kg_h = feed.dry_reactive_wood_kg_h + feed.water_kg_h + air.air_kg_h
    if basis_kg_h <= 0:
        raise ValueError("Reactive inlet basis must be positive.")

    mass_fractions = {
        "WOOD": feed.dry_reactive_wood_kg_h / basis_kg_h,
        "H2O(L)": feed.water_kg_h / basis_kg_h,
        "O2": air.oxygen_kg_h / basis_kg_h,
        "N2": air.nitrogen_kg_h / basis_kg_h,
    }
    return mass_fractions, basis_kg_h
