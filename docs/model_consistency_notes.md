# Model Consistency Notes

This document records known consistency checks that should be resolved as the repository develops from an initial public scaffold toward a validated research-support package.

## 1. Temperature label versus Cantera input temperature

The historical Python script defines:

```python
tk = 790.0     # temperature [K]
```

and passes this value directly to Cantera. Therefore, in the script as written, `790.0` is interpreted as Kelvin.

However, the associated technical paper and plotted case descriptions discuss treatment temperatures such as 780, 790, and 800 °C. In thermochemical biomass conversion, this difference is large:

```text
790 °C = 1063.15 K
790 K  = 516.85 °C
```

Until the original simulation input basis is verified, result filenames such as `T790` should be treated as historical case labels rather than a confirmed temperature unit.

## 2. Species-name convention

The Cantera mechanism uses uppercase species names such as:

```text
WOOD
CHAR
TAR
```

The older plotting script included lowercase calls such as `wood` and `char`. Refactored scripts should use the species names exactly as defined in the mechanism file, typically through selected columns such as:

```text
Y_WOOD
Y_CHAR
Y_TAR
```

## 3. Mass fractions versus mass rates

The curated CSV files contain mass fractions and state variables. Published figures may present mass rates such as kg/h. Conversion from mass fraction to mass rate requires a consistent total mass-flow basis:

```text
species mass rate = total stream mass rate × species mass fraction
```

Because different historical scripts and papers may use different biomass and gas-flow bases, this repository should not convert curated mass fractions into absolute mass rates until the mass-flow basis is verified for each case.

## 4. Validation status

The data and scripts are useful for trend reproduction and process understanding. They are not yet experimentally validated design tools.

Before stronger claims are made, the repository should verify:

- the temperature unit and thermal boundary condition;
- the feedstock, moisture, ash, and gas-flow basis;
- the species naming and mechanism compatibility;
- material balance closure;
- trend agreement with the published figures;
- sensitivity to time step, reactor assumptions, and solver settings.
