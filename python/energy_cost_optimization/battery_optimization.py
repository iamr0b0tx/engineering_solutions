## Battery Design
from scipy.integrate import quad
from math import cos, pi, ceil

from scipy.optimize import minimize
from matplotlib import pyplot as plt

import numpy as np

##m_v = total vehicle mass (kg)
##a_v = vehicle acceleration (m / s2)
##g = gravitational acceleration
##∝_s = road slope angle
##c_rr = road rolling resistance coefficient
##c_d = air drag coefficient
##rho = air density (kg / m3)
##A = vehicle frontal area (m2)
##v_v = vehicle speed (m / s)
##T_d = total length of drive cycle (km)

m_v = 1908
a_v = 10
g = 9.81
alpha_s = 0
c_rr = .011
c_d = .36
rho = 1.202
A = 2.42
v_v = 220

# converts degrees to rad
degree_to_radian = lambda deg: deg * pi / 180
cosine = lambda x: cos(degree_to_radian(x))

total_energy_consumed_integrand = lambda t, m_v, a_v, g, alpha_s, c_rr, c_d, rho, A, v_v: (m_v * a_v) +  (m_v * g * (alpha_s)) + (m_v * g * cosine(alpha_s) * c_rr) + (0.5 * c_d  * rho * A * v_v**2)
total_energy_consumed = quad(total_energy_consumed_integrand, 0, 10, args=(m_v, a_v, g, alpha_s, c_rr, c_d, rho, A, v_v))[0]

total_length_of_drive_cycle = 23.266
auxilliary_energy = 9.241
efficiency_of_the_powertrain = 0.9
vehicle_drive_range = 250

# battery params
battery_cost = [100, 150, 200, 300]
length_of_battery_options = total_number_of_options = len(battery_cost)
battery_cell_capacity = [3.2, 3.4, 3.6, 3.8]
battery_cell_mass = [.0485] * length_of_battery_options
battery_cell_voltage = [3.57, 3.75, 3.8, 2.75]
battery_nominal_voltage = [400] * length_of_battery_options
volume_of_battery_cell = [1.8, 2.0, 1.5, 1.12]

# battery pack energy
battery_pack_energy = [((total_energy_consumed / total_length_of_drive_cycle) + auxilliary_energy) * (2 - efficiency_of_the_powertrain) * vehicle_drive_range * (battery_cell_capacity[i]) * (battery_cell_voltage[i]) for i in range(length_of_battery_options)]

# total number of cells in battery pack
total_number_of_cells_in_battery_pack = [battery_pack_energy[i] / (battery_cell_capacity[i] * battery_cell_voltage[i]) for i in range(length_of_battery_options)]

total_battery_cost = [total_number_of_cells_in_battery_pack[i]*battery_cost[i] for i in range(length_of_battery_options)]

total_battery_cost = np.array(total_battery_cost)
total_number_of_cells_in_battery_pack = np.array(total_number_of_cells_in_battery_pack)[total_battery_cost.argsort()]
battery_pack_energy = np.array(battery_pack_energy)[total_battery_cost.argsort()]

def callback(x):
    print(total_energy_consumed, battery_pack_energy, total_battery_cost)
    solutions.append(x)

def objective(x):
    # total lighting values
    return sum([(battery_pack_energy[i] * (x[i]-1)) + (total_battery_cost[i] * (x[i]-1)) for i in range(length_of_battery_options)])
    # return sum(x)

def batteryConstraint(x):
    return total_energy_consumed - sum([battery_pack_energy[i] * x[i] for i in range(length_of_battery_options)])

def countConstraint(x):
    return sum(x) - 1

# max guess value
max_guess = 10

# initial guesses
# x0 = np.random.randint(low=1, high=max_guess, size=total_number_of_options)
x0 = np.full(total_number_of_options, max_guess)
# x0 = np.array([max_guess], dtype=np.int64)

# solutions
solutions = [x0]

# show initial objective
print('Initial SSE Objective:', x0, str(objective(x0)))

# the bounds
b = (0, 10)
bnds = tuple(b for _ in range(total_number_of_options))

# define constriants
cons = ([
    # {'type': 'ineq', 'fun': batteryConstraint},
    # {'type': 'eq', 'fun': countConstraint},
])

# run solver
solution = minimize(objective, x0, method='SLSQP', bounds=bnds, constraints=cons, callback=callback)

# get the optimal value
x = (solution.x > 0).astype(np.int64)

# prepare optimization values
solutions = (np.array(solutions) > 0).astype(np.int8)

# show final objective
print('Final SSE Objective:', x, str(objective(x)), end='\n\n')

# print solution
print('Solution\n===============')

optimal_index = x.argsort()[-1]

# battery pack mass
m_bp = battery_pack_energy[optimal_index] / (battery_cell_capacity[optimal_index] * battery_cell_voltage[optimal_index]) * battery_cell_mass[optimal_index]

# battery pack capacity
C_bp = (total_number_of_cells_in_battery_pack[optimal_index] * battery_cell_voltage[optimal_index] * battery_cell_capacity[optimal_index]) / battery_nominal_voltage[optimal_index]

# volume of battery cell
volume_of_battery_pack = total_number_of_cells_in_battery_pack[optimal_index] * volume_of_battery_cell[optimal_index]

costs = solutions * np.array(total_battery_cost)
print(costs[-1], ['{:,.4f}'.format(xx) for xx in total_battery_cost])
plt.subplot(211)
plt.plot(costs)
plt.title('Cost of Battery')
plt.legend(['x{} {:,.4f}'.format(i+1, int(costs[-1][i])) for i in range(total_number_of_options)])

plt.subplot(212)
plt.plot(solutions)
plt.title('Number of Types')
plt.legend(['x{} {}'.format(i+1, int(x[i] > 0)) for i in range(total_number_of_options)])
# plt.show()
