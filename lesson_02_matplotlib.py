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
plt.savefig("resistance_vs_temperature_100dpi.png", dpi=100)
plt.savefig("resistance_vs_temperature_300dpi.png", dpi=300)
plt.show()

import numpy as np
import matplotlib.pyplot as plt

raman_shift = np.array([100, 110, 120, 130, 140, 150])
intensity = np.array([50, 80, 150, 90, 60, 45])

baseline = np.array([40, 45, 50, 55, 60, 65])

plt.figure(figsize=(8, 5))

plt.plot(
    raman_shift,
    intensity,
    linewidth=2,
    label="Raw Raman spectrum"
)

plt.plot(
    raman_shift,
    baseline,
    linewidth=2,
    label="Baseline"
)

plt.xlabel("Raman Shift (cm$^{-1}$)")
plt.ylabel("Intensity (a.u.)")
plt.title("Raman Spectrum with Baseline")

plt.legend()
plt.grid()

plt.savefig("raman_raw_baseline.pdf")

plt.show()