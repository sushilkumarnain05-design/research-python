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
import numpy as np
resistance = np.array ([120, 125, 132, 140, 150])
print("average:",np.mean (resistance))
print("maximum:", np.max(resistance))
print("minimum:", np.min(resistance))
print ("standard deviation:", np.std(resistance))
high_R = resistance[resistance > 130]
print(high_R)


intensity = np.array ([120, 450, 80, 1250, 300, 1800])
strong = intensity [intensity >500]
print(strong)

temperature = np.array([300, 310, 320, 330, 340])
resistance = np.array([120, 125, 132, 140, 150])
print(temperature)
print(resistance)


import numpy as np
import matplotlib.pyplot as plt

temperature = np.array([300, 310, 320, 330, 340])
resistance1 = np.array([120, 125, 132, 140, 150])
resistance2 = np.array([115, 122, 130, 138, 148])
plt.figure(figsize = (8,5))
plt.plot(
    temperature,
    resistance1,
    linewidth=2,
    marker="o",
    label= "sample1"
)

plt.plot(temperature,
    resistance2,
    linewidth=2,
    marker="s",
    label="sample2",
)

plt.xlabel("Temperature(K)")
plt.ylabel("Resistance(Ω)")
plt.title ("resistance vs temperature")
plt.grid()
plt.legend(loc="upper left")
plt.savefig("resistance vs temperature.pdf")
plt.savefig("resistance_vs_temperature.png", dpi=300)
plt.show()