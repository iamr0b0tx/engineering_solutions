from math import ceil, pi

# from third party
import numpy as np
from scipy.optimize import minimize
from matplotlib import pyplot as plt
from scipy.integrate import quad

'''
R - Wall Resistance
A_wall - Area of Wall
CLTD_wall - Cooling Load Temperature difference
max_outdoor_temp - Maximum Outdoor Temperature
daily_range_temp - Daily Range Temp
inside_temp - Inside Temperature
U_window - Overall Heat transmission Co-efficient
A_window - Area of Window
CLTD_window - Cooling Load Temperature Difference of Window
SC - Shading Co-efficient
SCL - Solar Cooling Load Factor
N - Number of People
sensible_heat_gain - Sensible Heat Gain
latent_heat_gain - Latent Heat Gain
CLF_people - Cooling Load Factor for People
CLF_light - Cooling Load Factor For Light
'''

R = 1.554
A_wall = 18
CLTD_wall = 9
max_outdoor_temp = 31
daily_range_temp = 9
inside_temp = 25.5
U_window = 7
A_window = 10
CLTD_window = 2.1
SC = 1
SCL = 211
N = 50
sensible_heat_gain = 70
latent_heat_gain = 45
CLF_people = 0.85
CLF_light = 0.93


# define parameters for wind
per = 1
air_density = 1
wind_speed = 1

# define constants
max_guess = 3
area_of_room, foot_candles = 81, 50

# the lighting options
light_cost = [100, 500, 300, 350, 300]
light_power_rating = [60, 60, 60, 60, 60]
luminous_efficacy = [15, 20, 60, 90, 87]
lighting_use_factor = [1, 1, 1, 1, 1]
lighting_balast_factor = [0.8, 1.2, 0.95, 0.87, 1.0]

# the cooling options
cooling_power_rating = [1, 2, 1.5, 1.5, 1.5]
cooling_power_rating = [value*735.499 for value in cooling_power_rating]
cooling_cost = [82_000, 188_000, 87_000, 95_000, 78_000]

# number of data points
number_of_light_types = len(light_cost)
number_of_cooling_options = len(cooling_power_rating)
number_of_wind_options = 1

total_number_of_options = number_of_cooling_options + \
    number_of_light_types + number_of_wind_options

assert len(light_cost) == number_of_light_types
assert len(light_power_rating) == number_of_light_types
assert len(luminous_efficacy) == number_of_light_types
assert len(lighting_use_factor) == number_of_light_types
assert len(lighting_balast_factor) == number_of_light_types

# start index of PV starting index
lighting_starting_index = 0
cooling_starting_index = number_of_light_types
wind_starting_index = number_of_cooling_options + number_of_light_types

cooling_ending_index = cooling_starting_index + number_of_cooling_options
wind_ending_index = wind_starting_index + number_of_wind_options

# solar parameters
total_area = 1
fcomp = 1
fmain = 1
fdirt = 1
n_alpha_cable = 1
n_ac_cable = 1
n_inverter = 1
peak_sun_hours = 1

# options
pv_rating = [1]
pv_cost = [1]
pv_area = [1]
length_of_solar_options = len(pv_cost)

npv = lambda area_PV: total_area / area_PV
sys_eff = fcomp * fmain * fdirt * n_inverter * n_alpha_cable * n_ac_cable
Epv = lambda area_PV, power_rating_PV: npv(area_PV) * sys_eff * power_rating_PV * peak_sun_hours

def callback(x):
    solutions.append(x)

def getCoolingLoad(x):
    # cooling load for wall
    U_wall = R ** -1
    T_m = 0.5 * (max_outdoor_temp - daily_range_temp)
    CLTD_c = CLTD_wall + (25 - inside_temp) + (T_m - 29.4)
    Q_wall = U_wall * A_wall * CLTD_c

    # cooling load for window
    Q_window = U_window * A_window * CLTD_window

    # cooling load for solar heat through class
    Q_shtg = A_window * SC * SCL

    # cooling load for people
    Q_sensible = N * sensible_heat_gain * CLF_people
    Q_latent = N * latent_heat_gain

    # cooling load for light
    Q_lighting = sum([x[i] * light_power_rating[i] * lighting_use_factor[i] *
                     lighting_balast_factor[i] for i in range(number_of_light_types)]) * CLF_light

    # total cooling load
    total_cooling_energy = Q_wall + Q_window + \
        Q_shtg + Q_sensible + Q_latent + Q_lighting
    return total_cooling_energy


def calcObjective(x):
    # total lighting values
    total_light_energy = sum([
        x[i] * light_power_rating[i] for i in range(number_of_light_types)
    ])
    
    total_light_cost = sum([
        x[i] * light_cost[i] for i in range(number_of_light_types)
    ])

    # total cooling values
    total_cooling_energy = sum([
            x[i] * cooling_power_rating[i-number_of_light_types]\
                for i in range(cooling_starting_index, cooling_ending_index)
        ]
    )
    
    total_cooling_cost = sum([
        x[i] * cooling_cost[i-number_of_light_types] for i in range(
            cooling_starting_index, cooling_ending_index)
        ]
    )

    # total energy and cost
    total_energy = total_light_energy + total_cooling_energy
    total_cost = total_light_cost + total_cooling_cost

    return total_energy, total_cost


def objective(x):
    return sum(calcObjective(x))


def lightingConstraint(x):
    lum_eff = sum([x[i] * luminous_efficacy[i]
                  for i in range(number_of_light_types)])
    pow_rate = sum([x[i] * light_power_rating[i]
                   for i in range(number_of_light_types)])

    denom = (lum_eff * pow_rate)

    nl = np.inf if denom == 0 else (area_of_room * foot_candles) / denom
    return nl - 1


def coolingConstraint(x):
    total_cooling_load = getCoolingLoad(x)
    total_power = sum([x[i] * cooling_power_rating[i-number_of_light_types]
                      for i in range(cooling_starting_index, cooling_ending_index)])

    nl = np.inf if total_power == 0 else total_cooling_load / total_power
    return nl - 1

def windConstraint(x):
    total_energy, _ = calcObjective(x)
    rotor_radius = x[wind_starting_index:wind_ending_index]
    return total_energy - (0.5 * per * air_density * pi * rotor_radius * wind_speed)

# specify energy type
energy_supply_type='solar'

# define constriants
cons = ([
    {'type': 'eq', 'fun': lightingConstraint},
    {'type': 'eq', 'fun': coolingConstraint},
])

solar_state = False
if energy_supply_type == 'wind':
    cons.append({'type': 'eq', 'fun': windConstraint})

else:
    solar_state = True
    total_number_of_options -= number_of_wind_options

# initial guesses
# x0=np.random.randint(max_guess, size=total_number_of_options)
x0 = np.full(total_number_of_options, max_guess)

# solutions
solutions=[x0]

# show initial objective
print('Initial SSE Objective: ' + str(objective(x0)))

# the bounds
b=(0, 5)
bnds=tuple(b for _ in range(total_number_of_options))

solution=minimize(objective, x0, method='SLSQP', bounds=bnds,
                  constraints=cons, callback=callback)
x=solution.x

# show final objective
print('Final SSE Objective: ' + str(objective(x)), end='\n\n')

# total energy required
total_energy, _ = calcObjective(x)

# print solution
print('Solution\n===============')
text='Lighting Type'
offset=1
for i in range(total_number_of_options):
    if i == cooling_starting_index:
        text='Cooling Type'
        offset -= number_of_light_types

    elif i == wind_starting_index:
        text = 'Wind Type'
        offset -= number_of_cooling_options

    print('{:>15s} {} = {:.4f}'.format(text, i+offset, x[i]))

solutions=np.array(solutions)
energy, cost=np.array([calcObjective(x) for x in solutions]).T

plt.subplot(321)
plt.plot(energy)
plt.title('Energy against Number of Iterations')
plt.legend(['Min Energy {:,.4f} Watt'.format(energy[-1])])


plt.subplot(322)
plt.plot(cost)
plt.title('Cost against Number of Iterations')
plt.legend(['Min Cost {:,.4f} Naira'.format(cost[-1])])

light=solutions[:, 0:number_of_light_types]
plt.subplot(323)
plt.plot(light)
plt.title('Number of Light Types against Number of Iterations')
plt.legend(['x{} {:.4f}~{}'.format(i+1, x[i], ceil(x[i]))
           for i in range(light.shape[1])])

cooling=solutions[:, cooling_starting_index:cooling_ending_index]
plt.subplot(324)
plt.plot(cooling)
plt.title('Number of Cooling Types against Number of Iterations')
plt.legend(['x{} {:.4f}~{}'.format(i+1, x[cooling_starting_index + i],
           ceil(x[cooling_starting_index + i])) for i in range(cooling.shape[1])])

if not solar_state:
    wind=solutions[:, wind_starting_index:wind_ending_index]
    plt.subplot(325)
    plt.plot(wind)
    plt.title('Rotor radius against Number of Iterations')
    plt.legend(['x{} {:.4f}~{}'.format(i+1, x[wind_starting_index + i], ceil(x[wind_starting_index + i])
            if i == 1 else x[wind_starting_index + i]) for i in range(wind.shape[1])])

else:
# -----------------------------------solar optimization------------------------------------
    minimum_pv_cost = optimal_pv_index = None
    costs = [1]
    pv_energy = [1]

    for i in range(length_of_solar_options):
        pv_energy.append(Epv(pv_area[i], pv_rating[i]))

        # skip of energy is not enough
        if pv_energy[-1] < total_energy:
            continue
        
        # cost of current pv
        costs.append(pv_cost * npv(pv_area[i]))

        if optimal_pv_index is None:
            optimal_pv_index = i
            minimum_pv_cost = costs[-1]

        elif cost < minimum_pv_cost:
            minimum_pv_cost = costs[-1]
            optimal_pv_index = i

    if optimal_pv_index is None:
        print('No good solar option found!')

    else:
        print(
            'optimal type is Type {}: cost = {:,.4f}, energy = {:,.4f}'.format(
                optimal_pv_index+1, minimum_pv_cost, pv_energy[-1][optimal_pv_index]
            )
        )
        print(costs)
        print(pv_energy)

        plt.subplot(325)
        plt.title('Solar PV Cost')
        plt.bar(range(1, length_of_solar_options+1), costs)

        plt.subplot(326)
        plt.title('Solar PV Energy')
        plt.bar(range(1, length_of_solar_options+1), pv_energy)

# show all plots
plt.show()


