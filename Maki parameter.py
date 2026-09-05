import math


def calculate_maki_from_fields(B_c2_orb_0, B_p_0):
    """
    Calculates the Maki parameter using the orbital upper critical field
    and the Pauli paramagnetic limiting field at 0 Kelvin.
    """
    return math.sqrt(2) * (B_c2_orb_0 / B_p_0)

if __name__ == "__main__":

    b_c2_orb = 0.993
    b_p = 5.90

    alpha_fields = calculate_maki_from_fields(b_c2_orb, b_p)
    print(f"Maki parameter (from fields): {alpha_fields:.4f}")



