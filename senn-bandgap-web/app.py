import streamlit as st
from senn_bandgap import BandgapPredictor


st.set_page_config(
    page_title="SENN Bandgap Predictor",
    page_icon="🌟",
    layout="centered",
)


@st.cache_resource(show_spinner="Loading SENN model...")
def load_predictor():
    return BandgapPredictor()


def predict_bandgap(ma, fa, cs, br, cl, iodine):
    predictor = load_predictor()
    return predictor.predict_one(
        MA=ma,
        FA=fa,
        Cs=cs,
        Br=br,
        Cl=cl,
        I=iodine,
    )


st.title("🌟 SENN Bandgap Predictor")
st.caption("Perovskite bandgap prediction using a pretrained SENN model")

st.markdown(
    """
This web app predicts the bandgap of perovskite compositions using a pretrained
**SENN (Symbolically Encoded Neural Network)** model.

The input order is fixed as:

```text
[MA, FA, Cs, Br, Cl, I]
```
"""
)

st.divider()

preset = st.selectbox(
    "Choose an example composition or enter your own values below",
    [
        "FAPbI3: MA=0, FA=1, Cs=0, Br=0, Cl=0, I=1",
        "Mixed example: MA=0, FA=0.9, Cs=0.1, Br=0.2, Cl=0, I=0.8",
        "Custom",
    ],
)

if preset.startswith("FAPbI3"):
    default_values = dict(MA=0.0, FA=1.0, Cs=0.0, Br=0.0, Cl=0.0, I=1.0)
elif preset.startswith("Mixed"):
    default_values = dict(MA=0.0, FA=0.9, Cs=0.1, Br=0.2, Cl=0.0, I=0.8)
else:
    default_values = dict(MA=0.0, FA=1.0, Cs=0.0, Br=0.0, Cl=0.0, I=1.0)

st.subheader("Input Composition")

a1, a2, a3 = st.columns(3)
with a1:
    MA = st.number_input("MA", min_value=0.0, max_value=1.0, value=default_values["MA"], step=0.01, format="%.4f")
with a2:
    FA = st.number_input("FA", min_value=0.0, max_value=1.0, value=default_values["FA"], step=0.01, format="%.4f")
with a3:
    Cs = st.number_input("Cs", min_value=0.0, max_value=1.0, value=default_values["Cs"], step=0.01, format="%.4f")

x1, x2, x3 = st.columns(3)
with x1:
    Br = st.number_input("Br", min_value=0.0, max_value=1.0, value=default_values["Br"], step=0.01, format="%.4f")
with x2:
    Cl = st.number_input("Cl", min_value=0.0, max_value=1.0, value=default_values["Cl"], step=0.01, format="%.4f")
with x3:
    I = st.number_input("I", min_value=0.0, max_value=1.0, value=default_values["I"], step=0.01, format="%.4f")

a_sum = MA + FA + Cs
x_sum = Br + Cl + I

st.subheader("Composition Check")
col_a, col_x = st.columns(2)
col_a.metric("A-site sum", f"{a_sum:.4f}")
col_x.metric("X-site sum", f"{x_sum:.4f}")

if abs(a_sum - 1.0) > 1e-3:
    st.warning("A-site composition does not sum to 1. Please check MA + FA + Cs.")
if abs(x_sum - 1.0) > 1e-3:
    st.warning("X-site composition does not sum to 1. Please check Br + Cl + I.")

st.divider()

if st.button("Predict Bandgap", type="primary", use_container_width=True):
    try:
        bandgap = predict_bandgap(MA, FA, Cs, Br, Cl, I)
        st.success(f"Predicted bandgap: {bandgap:.6f} eV")

        st.markdown("#### Input vector")
        st.code(f"[{MA:.4f}, {FA:.4f}, {Cs:.4f}, {Br:.4f}, {Cl:.4f}, {I:.4f}]")

    except Exception as e:
        st.error("Prediction failed.")
        st.exception(e)

st.markdown(
    """
---
**Note.** This tool is intended for fast research screening. Predictions outside the
training-data distribution should be interpreted carefully.
"""
)
