import numpy as np
import matplotlib as mpl
import scipy
import pybaselines

print("All libraries imported successfully!")

print("NEW RUN")

temperature = 300

if temperature > 300:
    print("High")
else:
    print("Low")

temperature=200
if temperature > 300:
    print("high")
elif temperature >250:
    print("medium")
else:
    print("low")

def calculate_resistance (voltage, current):
    return voltage / current
R = calculate_resistance (10,0.05)
print (R)

def calculate_seebeck (delta_V, delta_T):
    S = delta_V / delta_T
    return S
delta_V = 0.012
delta_T = 20
S = calculate_seebeck(delta_V, delta_T)
print (S)

temperature = [300, 310, 320, 330, 340]
resistance = [120, 125, 132, 140, 150]
for T,R in zip (temperature, resistance):
    print(T,R)

import numpy as np
temperature= np.array([300, 310, 320, 330, 340])
resistance = np.array ([120, 125, 132, 140, 150])
print (temperature)
print (resistance)
R2 = resistance *2
print (R2)