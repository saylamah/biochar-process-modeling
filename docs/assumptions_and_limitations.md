# Assumptions and limitations

## Main assumptions

- The reactor is represented as an ideal constant-pressure reactor.
- The process is treated as spatially lumped.
- Pressure is approximately atmospheric.
- The wood-pyrolysis mechanism is simplified and uses lumped species: `WOOD`, `CHAR`, and `TAR`.
- Moisture is introduced as `H2O(L)` and evaporates to `H2O`.
- Ash is tracked as an external feedstock fraction but is not yet a Cantera species in the mechanism.
- Air is represented as O2/N2 with fixed mass fractions.

## Current limitations

- Temperature-unit consistency must be verified before exact reproduction of publication figures. The original script passes `tk = 790.0` to Cantera as Kelvin, while several paper figures describe treatment temperature in degrees Celsius.
- The original script contains plotting calls using lowercase species names such as `wood` and `char`, while the mechanism species are uppercase `WOOD` and `CHAR`.
- The mechanism should be reviewed against the intended source kinetic scheme and publication assumptions.
- The model is not experimentally validated within this repository.
- Ash, PAHs, contaminants, gas cleaning, and downstream treatment are not yet modeled.
- Carbon-credit estimates are not certified and must be treated as preliminary screening.

## Development priority

The first technical milestone is a reproducible baseline simulation with documented units, inputs, outputs, assumptions, and comparison to the published biomass/biochar mass-rate behavior.
