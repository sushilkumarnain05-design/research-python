import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

from analysis.transport import classify_transport


st.title("🔬 Scientific Research Copilot")

st.write("Experimental Condensed Matter Physics")

st.header("Transport Analysis")

# Upload experimental data
uploaded_file = st.file_uploader(
    "Upload R(T) data",
    type=["csv", "xlsx"]
)

if uploaded_file is not None:

    # Read file
    if uploaded_file.name.endswith(".csv"):
        data = pd.read_csv(uploaded_file)
    else:
        data = pd.read_excel(uploaded_file)

    st.subheader("Uploaded Data")

    st.dataframe(data)

    st.write("Columns detected:", list(data.columns))

    temperature_column = None
    resistance_column = None

    for column in data.columns:
        name = str(column).lower()

        if "temp" in name or name in ["t", "temperature (k)", "t (k)"]:
            temperature_column = column

        if "res" in name or "resistance" in name or name in ["r", "r (ohm)", "r (ω)"]:
            resistance_column = column

    if temperature_column is not None:
        st.success(f"Temperature column detected: {temperature_column}")
    else:
        st.warning("Temperature column could not be identified.")

    if resistance_column is not None:
        st.success(f"Resistance column detected: {resistance_column}")
    else:
        st.warning("Resistance column could not be identified.")
    if temperature_column is not None and resistance_column is not None:

        temperature = data[temperature_column]
        resistance = data[resistance_column]
        analysis_data = pd.DataFrame({
            "Temperature": pd.to_numeric(temperature),
            "Resistance": pd.to_numeric(resistance)
        }).sort_values("Temperature")

        temperature = analysis_data["Temperature"]
        valid_mask = (
            np.isfinite(analysis_data["Temperature"]) &
            np.isfinite(analysis_data["Resistance"]) &
            (analysis_data["Temperature"] > 0) &
            (analysis_data["Resistance"] > 0)
        )

        analysis_data = analysis_data[valid_mask]
        removed_points = len(valid_mask) - valid_mask.sum()

        if removed_points == 0:
            st.success("No invalid data points were removed.")
        else:
            st.warning(
                f"{removed_points} invalid data point(s) were excluded from analysis."
            )
        temperature = analysis_data["Temperature"]
        resistance = analysis_data["Resistance"]


        st.subheader("Data Quality Check")
        st.write("Basic checks completed before transport analysis.")

        # Missing values
        missing_temperature = temperature.isna().sum()
        missing_resistance = resistance.isna().sum()

        if missing_temperature == 0 and missing_resistance == 0:
            st.success("No missing values detected.")
        else:
            st.warning(
                f"Missing values detected: "
                f"Temperature = {missing_temperature}, "
                f"Resistance = {missing_resistance}"
            )

        # Duplicate temperature points
        duplicate_temperature = temperature.duplicated().sum()

        if duplicate_temperature == 0:
            st.success("No duplicate temperature points detected.")
        else:
            st.warning(
                f"Duplicate temperature points detected: "
                f"{duplicate_temperature}"
            )

        # Temperature sorting
        if temperature.is_monotonic_increasing:
            st.success("Temperature data are sorted in ascending order.")
        elif temperature.is_monotonic_decreasing:
            st.info("Temperature data are sorted in descending order.")
        else:
            st.warning("Temperature data are not sorted.")

        # Numerical validity
        try:
            temperature_numeric = pd.to_numeric(temperature)
            resistance_numeric = pd.to_numeric(resistance)

            invalid_temperature = (~np.isfinite(temperature_numeric)).sum()
            invalid_resistance = (~np.isfinite(resistance_numeric)).sum()

            if invalid_temperature == 0 and invalid_resistance == 0:
                st.success("No invalid numerical values detected.")
            else:
                st.warning(
                    f"Invalid values detected: "
                    f"Temperature = {invalid_temperature}, "
                    f"Resistance = {invalid_resistance}"
                )

            # Physical validity
            if temperature_numeric.min() <= 0:
                st.error(
                    "Invalid temperature detected: "
                    "Temperature must be greater than 0 K."
                )
            else:
                st.success(
                    "All temperature values are physically valid (> 0 K)."
                )

            if resistance_numeric.min() <= 0:
                st.error("Non-positive resistance detected.")
            else:
                st.success("All resistance values are positive.")


        except (ValueError, TypeError):

            st.error("Temperature or Resistance contains non-numeric values.")
        if len(temperature) < 5:
            st.error(
                "Too few valid data points for reliable transport analysis "
                f"({len(temperature)} points). At least 5 points are required."
            )
            st.stop()
        st.subheader("Resistance vs Temperature (R–T)")
        st.caption("Temperature: K | Resistance: Ω")
        st.write(
            f"Temperature range: {temperature.min():.2f}–{temperature.max():.2f} K"
        )
        st.write(f"Number of data points: {len(temperature)}")
        if temperature.duplicated().any():
            st.warning(
                "Duplicate temperature values are present in the analysis data. "
                "Review these points before quantitative fitting."
            )
        else:
            st.success("Temperature values are unique in the analysis data.")
            temperature_steps = np.diff(temperature.to_numpy())
            if len(temperature_steps) > 0:
                st.write(
                    f"Temperature step range: "
                    f"{temperature_steps.min():.2f}–{temperature_steps.max():.2f} K"
                )
            if len(temperature_steps) > 1:
                step_ratio = temperature_steps.max() / temperature_steps.min()

                if step_ratio > 3:
                    st.warning(
                        f"Temperature spacing is highly uneven "
                        f"(max/min ratio = {step_ratio:.2f})."
                    )
                else:
                    st.success("Temperature spacing is reasonably uniform.")

            if np.all(temperature_steps > 0):
                st.success("Temperature points are strictly increasing.")
            else:
                st.warning(
                    "Temperature spacing is not strictly increasing. "
                    "Check the experimental data before quantitative analysis."
                )

        plot_data = pd.DataFrame({
            "Temperature": temperature,
            "Resistance": resistance
        })

        fig, ax = plt.subplots()

        ax.scatter(
            plot_data["Temperature"],
            plot_data["Resistance"]
        )

        ax.set_xlabel("Temperature (K)")
        ax.set_ylabel("Resistance (Ω)")
        ax.set_title("Resistance vs Temperature")

        st.pyplot(fig)
        plt.close(fig)

        classification, dR_dT = classify_transport(
            temperature,
            resistance
        )

        positive_fraction = np.mean(dR_dT > 0)
        negative_fraction = np.mean(dR_dT < 0)

        st.subheader("Transport Classification")

        st.write(f"**R(T) Classification:** {classification}")
        st.write(
            f"Positive dR/dT fraction: {positive_fraction:.1%}"
        )

        st.write(
            f"Negative dR/dT fraction: {negative_fraction:.1%}"
        )
        if 0.2 < positive_fraction < 0.8:
            st.warning(
                "R(T) contains substantial changes in dR/dT sign. "
                "Possible crossover or multiple transport regimes."
            )
        log_temperature = np.log(temperature.to_numpy())
        log_resistance = np.log(resistance.to_numpy())
        inverse_temperature = 1 / temperature.to_numpy()
        st.subheader("Arrhenius Representation")
        arrhenius_fit = linregress(
            inverse_temperature,
            log_resistance
        )

        arrhenius_r2 = arrhenius_fit.rvalue ** 2

        k_B = 8.617333262e-5  # eV/K

        activation_energy = arrhenius_fit.slope * k_B

        arrhenius_data = pd.DataFrame({
            "1/T (1/K)": inverse_temperature,
            "ln(R)": log_resistance
        })

        fig, ax = plt.subplots()

        ax.scatter(
            arrhenius_data["1/T (1/K)"],
            arrhenius_data["ln(R)"]
        )
        fitted_lnR = (
            arrhenius_fit.intercept
            + arrhenius_fit.slope * inverse_temperature
        )

        ax.plot(
            inverse_temperature,
            fitted_lnR
        )

        ax.set_xlabel("1/T (1/K)")
        ax.set_ylabel("ln(R)")
        ax.set_title("Arrhenius Representation")

        st.pyplot(fig)
        plt.close(fig)

        st.write(
            f"Arrhenius R²: {arrhenius_r2:.4f}"
        )

        st.write(
            f"Arrhenius slope: {arrhenius_fit.slope:.4e}"
        )

        st.write(
            f"Arrhenius intercept: {arrhenius_fit.intercept:.4f}"

        )
        st.write(
            f"Activation energy: {activation_energy:.4e} eV"
        )
        st.write(
            f"Arrhenius equation: ln(R) = "
            f"{arrhenius_fit.intercept:.4f} + "
            f"{arrhenius_fit.slope:.4e} × (1/T)"
        )
        arrhenius_residuals = (
                log_resistance - fitted_lnR
        )

        arrhenius_rmse = np.sqrt(
            np.mean(arrhenius_residuals ** 2)
        )

        st.subheader("Arrhenius Residual Analysis")

        st.write(
            f"Arrhenius RMSE: {arrhenius_rmse:.4e}"
        )

        residual_data = pd.DataFrame({
            "Temperature": temperature,
            "Arrhenius Residual": arrhenius_residuals
        })

        fig, ax = plt.subplots()

        ax.scatter(
            residual_data["Temperature"],
            residual_data["Arrhenius Residual"]
        )

        ax.axhline(
            0,
            linestyle="--"
        )

        ax.set_xlabel("Temperature (K)")
        ax.set_ylabel("Residual in ln(R)")
        ax.set_title("Arrhenius Residuals")

        st.pyplot(fig)
        plt.close(fig)
        residual_mean = np.mean(arrhenius_residuals)
        residual_std = np.std(arrhenius_residuals)

        st.write(
            f"Mean residual: {residual_mean:.4e}"
        )

        st.write(
            f"Residual standard deviation: {residual_std:.4e}"
        )

        if abs(residual_mean) < 0.1 * residual_std:
            st.success(
                "Residuals are approximately centered around zero."
            )
        else:
            st.warning(
                "Residuals show a possible systematic offset."
            )

        dlnR_dlnT = np.gradient(
            log_resistance,
            log_temperature
        )
        st.subheader("Logarithmic Derivative")

        log_derivative_data = pd.DataFrame({
            "Temperature": temperature,
            "dlnR/dlnT": dlnR_dlnT
        })

        fig, ax = plt.subplots()

        ax.plot(
            log_derivative_data["Temperature"],
            log_derivative_data["dlnR/dlnT"]
        )

        ax.set_xlabel("Temperature (K)")
        ax.set_ylabel("dlnR/dlnT")
        ax.set_title("Logarithmic Derivative")

        st.pyplot(fig)
        plt.close(fig)
        log_derivative_mean = np.mean(dlnR_dlnT)
        log_derivative_std = np.std(dlnR_dlnT)

        st.write(
            f"Mean dlnR/dlnT: {log_derivative_mean:.3f}"
        )

        st.write(
            f"Std. dev. of dlnR/dlnT: {log_derivative_std:.3f}"
        )
        st.subheader("dR/dT vs Temperature")

        derivative_data = pd.DataFrame(
            {
                "dR/dT": dR_dT
            },
            index=temperature_numeric
        )

        st.line_chart(derivative_data)
else:
    st.info("Upload a CSV or Excel file containing Temperature and Resistance data.")