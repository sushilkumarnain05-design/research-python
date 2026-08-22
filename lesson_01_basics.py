# import numpy as np
# import matplotlib as mpl
# import scipy
# import pybaselines

# print("All libraries imported successfully!")

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
import numpy as np
resistance = np.array ([120, 125, 132, 140, 150])
print("average:",np.mean (resistance))
print("maximum:", np.max(resistance))
print("minimum:", np.min(resistance))
print ("standard deviation:", np.std(resistance))
high_R = resistance[resistance > 130]

print(high_R)
