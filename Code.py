import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl

# Updated array which contains the room temperature (0 to 60°C)
temperature = np.arange(0, 61)

# Set the input
temp = ctrl.Antecedent(temperature, 'temp')

# Updated array to represent the possible AC temperatures (15 to 45°C)
ac_temperature = np.arange(15, 46)

# Set the output of the system
ac_temp = ctrl.Consequent(ac_temperature, 'ac_temp')

# Automatically generate the membership functions
temp.automf(5)
ac_temp.automf(5)

# Graphical representation of membership functions
temp.view()
ac_temp.view()

# Setting rules
rule1 = ctrl.Rule(temp['poor'], ac_temp['good'])
rule2 = ctrl.Rule(temp['average'], ac_temp['average'])
rule3 = ctrl.Rule(temp['good'], ac_temp['poor'])
rule4 = ctrl.Rule(temp['mediocre'], ac_temp['decent'])
rule5 = ctrl.Rule(temp['decent'], ac_temp['mediocre'])

# Creating control system
temperature_ctrl = ctrl.ControlSystem([rule1, rule2, rule3, rule4, rule5])

detect_temp = ctrl.ControlSystemSimulation(temperature_ctrl)

# Testing for room temperature 60°C
detect_temp.input['temp'] = 60
detect_temp.compute()
temp_output = detect_temp.output['ac_temp']
print("\nWhen room temperature is 60°C:")
print("The AC temperature is adjusted to", temp_output, "°C")
ac_temp.view(sim=detect_temp)

# Testing for room temperature 30°C
detect_temp.input['temp'] = 41
detect_temp.compute()
temp_output = detect_temp.output['ac_temp']
print("\nWhen room temperature is 30°C:")
print("The AC temperature is adjusted to", temp_output, "°C")
ac_temp.view(sim=detect_temp)

# Testing for room temperature 0°C
detect_temp.input['temp'] = 39
detect_temp.compute()
temp_output = detect_temp.output['ac_temp']
print("\nWhen room temperature is 17°C:")
print("The AC temperature is adjusted to", temp_output, "°C")
ac_temp.view(sim=detect_temp)
