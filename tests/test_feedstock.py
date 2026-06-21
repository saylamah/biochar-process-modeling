from biochar_model.feedstock import AirFeed, BiomassFeed, cantera_mass_fractions


def test_biomass_feed_mass_breakdown():
    feed = BiomassFeed(biomass_kg_h=100.0, moisture_fraction=0.10, ash_fraction=0.015)
    assert abs(feed.water_kg_h - 10.0) < 1e-12
    assert abs(feed.ash_kg_h - 1.5) < 1e-12
    assert abs(feed.dry_reactive_wood_kg_h - 88.5) < 1e-12


def test_cantera_mass_fractions_sum_to_one():
    feed = BiomassFeed(biomass_kg_h=100.0, moisture_fraction=0.10, ash_fraction=0.015)
    air = AirFeed(air_kg_h=466.0)
    y, basis = cantera_mass_fractions(feed, air)
    assert basis > 0
    assert abs(sum(y.values()) - 1.0) < 1e-12
