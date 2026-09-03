# import numpy as np
# import scipy.special as special
#
# # Universal physical constants
# E_CHARGE = 1.602176634e-19  # Electron charge (Coulombs)
# PLANCK_H = 6.62607015e-34  # Planck's constant (J s)
#
#
# def hln_equation(B, alpha, l_phi):
#     """
#     Computes the magnetoconductivity change using the HLN equation with SciPy.
#
#     Parameters:
#     B (ndarray): Applied magnetic field (Tesla)
#     alpha (float): Prefactor coefficient (-0.5 for a single WAL channel)
#     l_phi (float): Phase coherence length (meters)
#     """
#     # Prevent division by zero at B = 0 by shifting it by a tiny value
#     B = np.where(B == 0, 1e-9, B)
#
#     # Calculate characteristic magnetic field B_phi
#     B_phi = PLANCK_H / (4 * E_CHARGE * l_phi ** 2)
#
#     # Pre-factor constant: (e^2) / (pi * h)
#     quantum_conductance = (E_CHARGE ** 2) / (np.pi * PLANCK_H)
#
#     # Core HLN components using SciPy's digamma function (special.psi)
#     x = 0.5 + (B_phi / np.abs(B))
#     digamma_term = special.psi(x)
#     log_term = np.log(B_phi / np.abs(B))
#
#     # Combine elements to get the change in conductivity
#     delta_sigma = alpha * quantum_conductance * (digamma_term - log_term)
#     return delta_sigma
#
#
# # --- Example Run ---
# if __name__ == "__main__":
#     # Generate magnetic fields from -1.0 to 1.0 Tesla
#     magnetic_field = np.linspace(-1.0, 1.0, 11)
#
#     # Sample experimental parameters
#     sample_alpha = -0.5  # 1 channel of Weak Anti-Localization
#     sample_l_phi = 50e-9  # 50 nm phase coherence length
#
#     # Calculate the magnetoconductivity
#     results = hln_equation(magnetic_field, sample_alpha, sample_l_phi)
#
#     # Display the results
#     print(f"{'B Field (T)':<12} | {'Delta_Sigma (S)':<15}")
#     print("-" * 32)
#     for b, ds in zip(magnetic_field, results):
#         print(f"{b:11.2f} | {ds:14.4e}")

import sys
import numpy as np
import scipy.special as special

# Force matplotlib to save a file instead of trying to open a window
# This prevents 90% of matplotlib crashing/freezing errors
import matplotlib

matplotlib.use('Agg')
import matplotlib.pyplot as plt

# Universal physical constants
E_CHARGE = 1.602176634e-19  # Electron charge (Coulombs)
PLANCK_H = 6.62607015e-34  # Planck's constant (J s)


def hln_equation(B, alpha, l_phi):
    """
    Computes the magnetoconductivity change using the HLN equation.
    """
    # Ensure inputs are treated cleanly as float arrays
    B = np.asarray(B, dtype=float)

    # Prevent division by zero safely
    B = np.where(B == 0, 1e-9, B)

    # Calculate characteristic magnetic field B_phi
    B_phi = PLANCK_H / (4 * E_CHARGE * (float(l_phi) ** 2))

    # Pre-factor constant: (e^2) / (pi * h)
    quantum_conductance = (E_CHARGE ** 2) / (np.pi * PLANCK_H)

    # Core HLN components using SciPy's digamma function
    x = 0.5 + (B_phi / np.abs(B))
    digamma_term = special.psi(x)
    log_term = np.log(B_phi / np.abs(B))

    # Combine elements
    delta_sigma = alpha * quantum_conductance * (digamma_term - log_term)
    return delta_sigma


def main():
    print("Starting HLN script...")

    # 1. Generate clean magnetic field range
    magnetic_field = np.linspace(-0.5, 0.5, 500)

    # 2. Parameters
    sample_alpha = -0.5
    sample_l_phi = 100e-9

    # 3. Compute values
    print("Calculating HLN equation...")
    delta_sigma = hln_equation(magnetic_field, sample_alpha, sample_l_phi)

    # 4. Generate and save the plot safely
    print("Generating plot...")
    plt.figure(figsize=(8, 5))
    plt.plot(magnetic_field, delta_sigma, label=f'HLN Fit (alpha={sample_alpha})', color='blue', linewidth=2)
    plt.title('Magnetoconductivity Fit via HLN Equation', fontsize=12, fontweight='bold')
    plt.xlabel('Magnetic Field B (Tesla)')
    plt.ylabel('Delta Sigma (S)')
    plt.grid(True, linestyle='--', alpha=0.6)
    plt.legend(loc='best')
    plt.tight_layout()

    # Save the file to your computer
    output_filename = "hln_plot.png"
    plt.savefig(output_filename, dpi=300)
    print(f"Success! The plot has been saved perfectly as '{output_filename}' in your current folder.")


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print("\n=== AN ERROR OCCURRED ===")
        print(f"Error Type: {type(e).__name__}")
        print(f"Error Details: {e}")
        print("=========================\n")
        sys.exit(1)



