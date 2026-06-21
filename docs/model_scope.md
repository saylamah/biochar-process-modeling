# Model scope

The first model family in this repository is a simplified Cantera-based ideal constant-pressure reactor representation of biomass drying, pyrolysis, oxidation, char conversion, and gas formation.

## Included phenomena

- Liquid water evaporation to gas-phase water.
- Wood decomposition into char, light gases, water, and tar.
- Tar decomposition and partial oxidation.
- CH4, CO, H2, and char oxidation or conversion reactions.
- Residence-time sensitivity under specified reactor temperature and pressure.
- Initial sensitivity to moisture, air/oxygen exposure, and temperature.

## Not included yet

- Particle-scale intraparticle heat and mass transfer.
- Real reactor residence-time distribution.
- Heat losses, wall effects, or full heat balance.
- Ash chemistry, slagging, fouling, and deposition.
- Detailed tar speciation.
- PAH formation chemistry.
- Reactor hydrodynamics.
- Experimental calibration or uncertainty quantification.
- Full life-cycle carbon accounting.

## Recommended interpretation

The current model is suitable for exploratory technical communication, teaching, sensitivity screening, and hypothesis generation. It should not be used alone for design guarantees, investment decisions, permitting, certification, or carbon-credit claims.
