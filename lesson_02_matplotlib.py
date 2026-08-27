
# import numpy as np
# import matplotlib.pyplot as plt
#
# temperature = np.array([300, 310, 320, 330, 340])
# resistance1 = np.array([120, 125, 132, 140, 150])
# resistance2 = np.array([115, 122, 130, 138, 148])
# plt.figure(figsize = (8,5))
# plt.plot(
#     temperature,
#     resistance1,
#     linewidth=2,
#     marker="o",
#     label= "sample1"
# )
#
# plt.plot(temperature,
#     resistance2,
#     linewidth=2,
#     marker="s",
#     label="sample2",
# )
#
# plt.xlabel("Temperature(K)")
# plt.ylabel("Resistance(Ω)")
# plt.title ("resistance vs temperature")
# plt.grid()
# plt.legend(loc="upper left")
# plt.savefig("resistance vs temperature.pdf")
# plt.savefig("resistance_vs_temperature_100dpi.png", dpi=100)
# plt.savefig("resistance_vs_temperature_300dpi.png", dpi=300)
# plt.show()
#
# import numpy as np
# import matplotlib.pyplot as plt
#
# raman_shift = np.array([100, 110, 120, 130, 140, 150])
# intensity = np.array([50, 80, 150, 90, 60, 45])
#
# baseline = np.array([40, 45, 50, 55, 60, 65])
#
# plt.figure(figsize=(8, 5))
#
# plt.plot(
#     raman_shift,
#     intensity,
#     linewidth=2,
#     label="Raw Raman spectrum"
# )
#
# plt.plot(
#     raman_shift,
#     baseline,
#     linewidth=2,
#     label="Baseline"
# )
#
# plt.xlabel("Raman Shift (cm$^{-1}$)")
# plt.ylabel("Intensity (a.u.)")
# plt.title("Raman Spectrum with Baseline")
#
# plt.legend()
# plt.grid()
#
# plt.savefig("raman_raw_baseline.pdf")
#
# plt.show()


# import numpy as np
# import matplotlib.pyplot as plt
# data = np.loadtxt("raman_data.txt")
# raman_shift = data[:,0]
# intensity = data [:,1]
# plt.plot(raman_shift,intensity)
# plt.xlabel("raman_shift(cm${-1}$)")
# plt.ylabel("intensity(a.u.)")
# plt.title("raman spectrum")
# plt.grid()
# plt.show()

# import numpy as np
# import matplotlib.pyplot as plt
# data = np.loadtxt("raman_data.txt")
# raman_shift = data[:,0]
# intensity = data [:,1]
# baseline = np.array([40, 45, 50, 55, 60])
# corrected_intensity = intensity-baseline
# print("Raw:", intensity)
# print("Baseline:", baseline)
# print("Corrected:", corrected_intensity)
# plt.figure(figsize=(8,5))
# plt.plot(
#     raman_shift,
#     intensity,
#     label = "raw Raman"
# )
# plt.plot(
#     raman_shift,
#     baseline,
#     label = "Baseline"
# )
# plt.plot(
#     raman_shift,
#     corrected_intensity,
#     label= "Corrected Raman"
# )
# plt.xlabel("Raman_Shift(cm${-1}$)")
# plt.ylabel("Intensity(a.u.)")
# plt.title("Raman Spectrum:Raw, Baseline and corrected")
# plt.grid()
# plt.legend()
# plt.show()
import numpy as np
from matplotlib.pyplot import scatter

x=np.array([1,2,3,4,5])
y=np.array([2, 4, 5, 8, 10])
# coefficient=np.polyfit(x,y,1)
# print("Coefficient:",coefficient)

# coefficient=np.polyfit(x,y,1)
# print(coefficient)

# x = np.array([1, 2, 3, 4, 5])
# y = np.array([2, 4, 5, 8, 10])
#
# coefficients = np.polyfit(x, y, 1)
# # print("coefficients",coefficients)
# fitted_y=np.polyval(coefficients,x)
# print("fitted values:", fitted_y)

# import numpy as np
# import matplotlib.pyplot as plt
# x=np.array([0,1,2,3,4,])
# y=np.array([-0.2, 1.8, 3.8, 5.8, 7.8])
# coefficients=np.polyfit(x,y,1)
# m=coefficients[0]
# c=coefficients[1]
# y_fit=m*x+c
# print("slope=",m)
# print("intercept=",c)
# print("fitted y=", y_fit)

# import numpy as np
# import matplotlib.pyplot as plt
# x=np.array([0,1,2,3,4])
# y=np.array([1,2,5,10,17])
# coefficients=np.polyfit(x,y,2)
# print(coefficients)
# y_fit=np.polyval(coefficients,x)
# plt.scatter(x,y)
# plt.plot(x,y_fit)
# plt.show()
# print(y_fit)

import numpy as np
import matplotlib.pyplot as plt
x=np.array([0,1,2,3,4])
y=np.array([1,2,5,10,17])
coefficients=np.polyfit(x,y,2)
print(coefficients)
y_fit=np.polyval(coefficients,x)
plt.scatter(x,y)
plt.plot(x,y_fit)
plt.show()
