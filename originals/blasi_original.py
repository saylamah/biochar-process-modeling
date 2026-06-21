import cantera as ct
import matplotlib.pyplot as plt

tk = 790.0     # temperature [K]
p = 95325.0 #101325.0    # pressure [Pa]

gas = ct.Solution('Wood pyrolysis.yaml')
#gas.TP = tk, p
M_Biom = 250 #Kg/h
M_Air = 1165 #1165Kg/h
Moisture_Per= 0.144 #moisture persentage in Biomass
Ash_Per= 0.015 # 0.005 - 0.015 of wood
M_Water = M_Biom*Moisture_Per
M_Ash = M_Biom*Ash_Per
Biom = M_Biom-M_Water-M_Ash
Wm = M_Biom + M_Air
M_O2 = M_Air * 0.23
M_N2 = M_Air * 0.77
Y_Biom = Biom / Wm
Y_Water = M_Water / Wm
Y_O2 = M_O2 / Wm
Y_N2 = M_N2 / Wm
Y_ASH = M_Ash / Wm
gas.TPY = tk, p, {'WOOD': Y_Biom,'O2': Y_O2, 'N2': Y_N2, 'H2O(L)': Y_Water}
#gas.TPX = tk, p, {'WOOD': 0.032,'O2': 0.12, 'N2': 0.516, 'H2O(L)': 0.032,'H2O': 0.1,'CO2': 0.1, 'CO': 0.1}
#help (gas)
#print (gas.X[gas.species_index('WOOD')],gas.X[gas.species_index('O2')], gas.X[gas.species_index('N2')], gas.X[gas.species_index('H2O(L)')])
#input(aa)
#gas.TPX = tk, p, 'WOOD:1,O2:1,N2:4'
r = ct.IdealGasConstPressureReactor(gas)
n=0
sim = ct.ReactorNet([r])
time = 0.0
states = ct.SolutionArray(gas, extra=['t'])

for n in range(50):
    time += 1
    sim.advance(time)
    states.append(r.thermo.state, t=time)

plt.figure()
#plt.plot(states.t, states.X[:, gas.species_index('O2')], label='O2')
#plt.plot(states.t, states.X[:, gas.species_index('CO')], label='CO')
#plt.plot(states.t, states.X[:, gas.species_index('CO2')], label='CO2')
#plt.plot(states.t, states.X[:, gas.species_index('H2O')], label='H2O')
plt.plot(states.t, Wm*states.Y[:, gas.species_index('wood')], label='Biomass')
#plt.plot(states.t, Ash_Per*Wm*states.Y[:, gas.species_index('wood')], label='Asche')
#plt.plot(states.t,  Wm*states.Y[:, gas.species_index('ASH')], label='Ash')
#plt.plot(states.t, Wm*states.Y[:, gas.species_index('H2')], label='H2')
#plt.plot(states.t, Wm*states.Y[:, gas.species_index('CO')], label='CO')
#plt.plot(states.t, Wm*states.Y[:, gas.species_index('CO2')], label='CO2')
#plt.plot(states.t, Wm*states.Y[:, gas.species_index('CH4')], label='CH4')
#plt.plot(states.t, Wm*states.Y[:, gas.species_index('C2H2')], label='C2H2')
plt.plot(states.t, Wm*states.Y[:, gas.species_index('char')], label='Biokohle')
plt.xlabel('Zeit [s]')
plt.ylabel('Massenrate [kg/h]')
#plt.ylabel('Concentration [kg/m^3]')
plt.legend()
plt.show()
#states.save('results_H2O0_T790_O2-N2-23-77.csv', basis="mass", overwrite=True)
