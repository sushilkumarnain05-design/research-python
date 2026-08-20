import numpy as np


def classify_transport(T, R):
    """
    Basic classification of R(T) behavior.

    Returns:
        classification: metallic-like, insulating-like, or mixed
        dR_dT: numerical derivative
    """

    T = np.asarray(T, dtype=float)
    R = np.asarray(R, dtype=float)

    dR_dT = np.gradient(R, T)

    positive_fraction = np.mean(dR_dT > 0)
    negative_fraction = np.mean(dR_dT < 0)

    if positive_fraction > 0.8:
        classification = "Metallic-like"
    elif negative_fraction > 0.8:
        classification = "Insulating / semiconducting-like"
    else:
        classification = "Mixed / crossover behavior"

    return classification, dR_dT