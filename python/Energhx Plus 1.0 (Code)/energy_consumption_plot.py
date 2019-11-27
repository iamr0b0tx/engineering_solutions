from math import ceil, pi
from matplotlib.pyplot import subplot, plot, title, legend, bar, show
from scipy.optimize import minimize
from numpy import full, array, inf
import sys

from PyQt5.QtWidgets import (QApplication, QComboBox, QDialog,
    QDialogButtonBox, QFormLayout, QGridLayout, QGroupBox, QHBoxLayout,
    QLabel, QLineEdit, QMenu, QMenuBar, QPushButton, QSpinBox, QTextEdit,
    QVBoxLayout
)
from PyQt5.QtCore import Qt

import matplotlib.pylab as plt
from matplotlib.backends.backend_qt5agg import FigureCanvas
from matplotlib.figure import Figure
from matplotlib import pyplot as plt
import matplotlib
matplotlib.use('QT5Agg')


class EnergyConsumptionPlot(QDialog):
    NumGridRows = 3
    NumButtons = 4

    def __init__(self, parent):
        super(QDialog, self).__init__()

        self.parent = parent
        self.createFormGroupBox()

        buttonBox = QDialogButtonBox(
            QDialogButtonBox.Ok | QDialogButtonBox.Cancel)
        buttonBox.accepted.connect(self.accept)
        buttonBox.rejected.connect(self.reject)

        mainLayout = QVBoxLayout()
        mainLayout.addWidget(self.formGroupBox)
        mainLayout.addWidget(buttonBox)
        self.setLayout(mainLayout)

        self.setWindowTitle("Optimization results")
        # self.setWindowModality(Qt.ApplicationModal)

    def closeEvent(self, event):
        self.parent.focus_on_main_window = True
        self.hide()
        event.ignore()

    def createFormGroupBox(self):
        self.formGroupBox = QGroupBox("Form layout")
        layout = QFormLayout()

        self.figure = Figure()

        # plot
        self.plotWidget = FigureCanvas(self.figure)
        layout.addRow(self.plotWidget)

        self.label_opt_result = QLabel("Minimum Energy Consumption")
        layout.addRow(self.label_opt_result)

        self.formGroupBox.setLayout(layout)

# the lighting options
light_types = ['Type 1', 'Type 2', 'Type 3', 'Type 4', 'Type 5']
light_cost = [100, 500, 300, 350, 300]
light_power_rating = [60, 60, 60, 60, 60]
luminous_efficacy = [15, 20, 60, 90, 87]
lighting_use_factor = [1, 1, 1, 1, 1]
lighting_balast_factor = [0.8, 1.2, 0.95, 0.87, 1.0]

# the cooling options
cooling_types = ['Type 1', 'Type 2', 'Type 3', 'Type 4', 'Type 5']
cooling_power_rating = [1, 2, 1.5, 1.5, 1.5]
cooling_power_rating = [value for value in cooling_power_rating]
cooling_cost = [82_000, 188_000, 87_000, 95_000, 78_000]

# number of data points
number_of_light_types = len(light_cost)
number_of_cooling_options = len(cooling_power_rating)

total_number_of_options = number_of_cooling_options + number_of_light_types

assert len(light_cost) == number_of_light_types
assert len(light_power_rating) == number_of_light_types
assert len(luminous_efficacy) == number_of_light_types
assert len(lighting_use_factor) == number_of_light_types
assert len(lighting_balast_factor) == number_of_light_types

# start index of PV starting index
lighting_starting_index = 0
cooling_starting_index = number_of_light_types
cooling_ending_index = cooling_starting_index + number_of_cooling_options

# all solutions
solutions = []

def callback(x):
    solutions.append(x)


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
        x[i] * cooling_power_rating[i-number_of_light_types]
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


def getMinimum(area_of_room, foot_candles, total_cooling_load):
    global solutions

    def lightingConstraint(x):
        lum_eff = sum([x[i] * luminous_efficacy[i]
                       for i in range(number_of_light_types)])
        pow_rate = sum([x[i] * light_power_rating[i]
                        for i in range(number_of_light_types)])

        denom = (lum_eff * pow_rate)

        nl = inf if denom == 0 else (area_of_room * foot_candles) / denom
        return nl - 1

    def coolingConstraint(x):
        total_power = sum([x[i] * cooling_power_rating[i-number_of_light_types]
                           for i in range(cooling_starting_index, cooling_ending_index)])

        nl = inf if total_power == 0 else total_cooling_load / total_power
        return nl - 1

    # define constriants
    cons = ([
        {'type': 'eq', 'fun': lightingConstraint},
        {'type': 'eq', 'fun': coolingConstraint},
    ])

    max_guess = 50

    # initial guesses
    # x0=np.random.randint(max_guess, size=total_number_of_options)
    x0 = full(total_number_of_options, max_guess)

    # solutions
    solutions = [x0]

    # show initial objective
    print('Initial SSE Objective: ' + str(objective(x0)))

    # the bounds
    b = (0, 5)
    bnds = tuple(b for _ in range(total_number_of_options))

    solution = minimize(objective, x0, method='SLSQP', bounds=bnds,
                        constraints=cons, callback=callback)
    x = solution.x

    # show final objective
    print('Final SSE Objective: ' + str(objective(x)), end='\n\n')

    # total energy required
    total_energy, _ = calcObjective(x)

    # print solution
    print('Solution\n===============')
    text = 'Lighting Type'
    offset = 1
    for i in range(total_number_of_options):
        if i == cooling_starting_index:
            text = 'Cooling Type'
            offset -= number_of_light_types

        print('{:>15s} {} = {:.4f}'.format(text, i+offset, x[i]))

    solutions = array(solutions)
    energy, cost = array([calcObjective(x) for x in solutions]).T

    light = solutions[:, 0:number_of_light_types]
    x_light = [x[i] for i in range(light.shape[1])]

    cooling = solutions[:, cooling_starting_index:cooling_ending_index]
    x_cooling = [
        x[cooling_starting_index + i] for i in range(cooling.shape[1])
    ]

    return energy, cost, light, x_light, cooling, x_cooling


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ecp = EnergyConsumptionPlot()
    ecp.showMaximized()
    sys.exit(app.exec_())
