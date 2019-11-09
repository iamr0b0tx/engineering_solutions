# Battery Design
from math import cos, pi, ceil

# from third party
import numpy as np

from scipy.integrate import quad
from matplotlib import pyplot as plt

# m_v = total vehicle mass (kg)
# a_v = vehicle acceleration (m / s2)
# g = gravitational acceleration
# ∝_s = road slope angle
# c_rr = road rolling resistance coefficient
# c_d = air drag coefficient
# rho = air density (kg / m3)
# A = vehicle frontal area (m2)
# v_v = vehicle speed (m / s)
# T_d = total length of drive cycle (km)

m_v = 1908
a_v = 10
g = 9.81
alpha_s = 0
c_rr = .011
c_d = .36
rho = 1.202
A = 2.42
v_v = 220

def total_energy_consumed_integrand(t, m_v, a_v, g, alpha_s, c_rr, c_d, rho, A, v_v): 
    # converts degrees to rad
    degree_to_radian = lambda deg: deg * pi / 180
    return (m_v * a_v) + (m_v * g * (alpha_s)) + (m_v * g * cos(degree_to_radian(alpha_s)) * c_rr) + (0.5 * c_d * rho * A * v_v**2)


total_energy_consumed = quad(total_energy_consumed_integrand, 0, 10, args=(
    m_v, a_v, g, alpha_s, c_rr, c_d, rho, A, v_v))[0]

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
battery_pack_energy = [
    ((total_energy_consumed / total_length_of_drive_cycle) + auxilliary_energy) * \
    (2 - efficiency_of_the_powertrain) * vehicle_drive_range * (battery_cell_capacity[i]) * \
    (battery_cell_voltage[i]) for i in range(length_of_battery_options)
]

# total number of cells in battery pack
total_number_of_cells_in_battery_pack = [
    battery_pack_energy[i] / (battery_cell_capacity[i] * battery_cell_voltage[i]) for i in range(length_of_battery_options)
]

total_battery_cost = [
    total_number_of_cells_in_battery_pack[i] * battery_cost[i] for i in range(length_of_battery_options)
]

# find the min cost
minimum_battery_cost = optimal_index = None
for i in range(length_of_battery_options):
    if total_energy_consumed > battery_pack_energy[i]:
        continue

    if minimum_battery_cost is None:
        minimum_battery_cost = total_battery_cost[i]
        optimal_index = i

    elif minimum_battery_cost > total_battery_cost[i]:
        minimum_battery_cost = total_battery_cost[i]
        optimal_index = i

if optimal_index is not None:
    # battery pack mass
    m_bp = battery_pack_energy[optimal_index] / (battery_cell_capacity[optimal_index] * \
        battery_cell_voltage[optimal_index]) * battery_cell_mass[optimal_index]

    # battery pack capacity
    C_bp = (total_number_of_cells_in_battery_pack[optimal_index] * \
        battery_cell_voltage[optimal_index] * battery_cell_capacity[optimal_index]) / \
        battery_nominal_voltage[optimal_index]

    # volume of battery cell
    volume_of_battery_pack = total_number_of_cells_in_battery_pack[optimal_index] * \
        volume_of_battery_cell[optimal_index]

    print(
        'optimal type is Type {}: cost = {:,.4f}, energy = {:,.4f}'.format(
            optimal_index+1, minimum_battery_cost, battery_pack_energy[optimal_index]
        )
    )
    print(total_battery_cost)
    print(battery_pack_energy)

    plt.subplot(211)
    plt.title('Battery Pack Cost')
    plt.bar(range(1, length_of_battery_options+1), total_battery_cost)

    plt.subplot(212)
    plt.title('Battery Pack Energy')
    plt.bar(range(1, length_of_battery_options+1), battery_pack_energy)
    plt.show()

else:
    print('No suitable choice found!')

# show all plots
plt.show()
