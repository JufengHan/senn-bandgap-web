import streamlit as st
from pathlib import Path

from senn_bandgap import BandgapPredictor


# ============================================================
# Page configuration
# ============================================================
st.set_page_config(
    page_title="SENN Bandgap Predictor",
    page_icon="🌟",
    layout="centered",
)


# ============================================================
# Paths
# ============================================================
BASE_DIR = Path(__file__).resolve().parent
ASSET_DIR = BASE_DIR / "assets"

CAS_LOGO = ASSET_DIR / "cas_logo.png"
ANNILAB_LOGO = ASSET_DIR / "annilab_logo.png"


# ============================================================
# Style
# ============================================================
st.markdown(
    """
<style>
.main {
    background-color: #ffffff;
}

.block-container {
    padding-top: 2rem;
    padding-bottom: 2rem;
    max-width: 960px;
}

.title-text {
    text-align: center;
    font-size: 2.3rem;
    font-weight: 800;
    color: #0B3D91;
    margin-bottom: 0.2rem;
}

.subtitle-text {
    text-align: center;
    font-size: 1.05rem;
    color: #555555;
    margin-bottom: 1.5rem;
}

.info-card {
    padding: 1.1rem 1.2rem;
    border-radius: 16px;
    background-color: #F7F9FC;
    border: 1px solid #E4E8F0;
    margin-bottom: 1.2rem;
}

.section-title {
    font-size: 1.25rem;
    font-weight: 700;
    color: #0B3D91;
    margin-top: 1.2rem;
    margin-bottom: 0.6rem;
}

.result-card {
    padding: 1.2rem 1.4rem;
    border-radius: 18px;
    background: linear-gradient(135deg, #EEF5FF 0%, #F8FBFF 100%);
    border: 1px solid #D5E6FF;
    text-align: center;
    margin-top: 1rem;
}

.result-value {
    font-size: 2rem;
    font-weight: 800;
    color: #0B3D91;
}

.small-note {
    color: #666666;
    font-size: 0.9rem;
}

.logo-box {
    display: flex;
    align-items: center;
    justify-content: center;
}
</style>
""",
    unsafe_allow_html=True,
)


# ============================================================
# Load model
# ============================================================
@st.cache_resource
def load_predictor():
    return BandgapPredictor()


predictor = load_predictor()


# ============================================================
# Initialize session state
# ============================================================
default_values = {
    "MA": 0.0,
    "FA": 1.0,
    "Cs": 0.0,
    "Br": 0.0,
    "Cl": 0.0,
    "I": 1.0,
}

for key, value in default_values.items():
    if key not in st.session_state:
        st.session_state[key] = value


def set_example_fapi3():
    st.session_state["MA"] = 0.0
    st.session_state["FA"] = 1.0
    st.session_state["Cs"] = 0.0
    st.session_state["Br"] = 0.0
    st.session_state["Cl"] = 0.0
    st.session_state["I"] = 1.0


def set_example_mixed():
    st.session_state["MA"] = 0.0
    st.session_state["FA"] = 0.9
    st.session_state["Cs"] = 0.1
    st.session_state["Br"] = 0.2
    st.session_state["Cl"] = 0.0
    st.session_state["I"] = 0.8


# ============================================================
# Header with logos
# ============================================================
logo_col1, title_col, logo_col2 = st.columns([1.2, 3.0, 2.0])

with logo_col1:
    if CAS_LOGO.exists():
        st.image(str(CAS_LOGO), use_container_width=True)

with title_col:
    st.markdown(
        """
<div class="title-text">SENN Bandgap Predictor</div>
<div class="subtitle-text">
Perovskite bandgap prediction powered by Symbolically Encoded Neural Networks
</div>
""",
        unsafe_allow_html=True,
    )

with logo_col2:
    if ANNILAB_LOGO.exists():
        st.image(str(ANNILAB_LOGO), use_container_width=True)


st.markdown("---")


# ============================================================
# Description
# ============================================================
st.markdown(
    """
<div class="info-card">
This web tool predicts the bandgap of perovskite compositions using a pretrained
<b>SENN</b> model. Please input the composition fractions of the A-site and X-site ions.
<br><br>
The input order is:
<code>[MA, FA, Cs, Br, Cl, I]</code>
</div>
""",
    unsafe_allow_html=True,
)


# ============================================================
# Example buttons
# ============================================================
st.markdown('<div class="section-title">Examples</div>', unsafe_allow_html=True)

ex_col1, ex_col2 = st.columns(2)

with ex_col1:
    st.button(
        "Use FAPbI₃ Example",
        on_click=set_example_fapi3,
        use_container_width=True,
    )

with ex_col2:
    st.button(
        "Use Mixed Composition Example",
        on_click=set_example_mixed,
        use_container_width=True,
    )


# ============================================================
# Input composition
# ============================================================
st.markdown('<div class="section-title">Input Composition</div>', unsafe_allow_html=True)

st.markdown("**A-site composition**")

a_col1, a_col2, a_col3 = st.columns(3)

with a_col1:
    MA = st.number_input(
        "MA",
        min_value=0.0,
        max_value=1.0,
        step=0.01,
        format="%.4f",
        key="MA",
    )

with a_col2:
    FA = st.number_input(
        "FA",
        min_value=0.0,
        max_value=1.0,
        step=0.01,
        format="%.4f",
        key="FA",
    )

with a_col3:
    Cs = st.number_input(
        "Cs",
        min_value=0.0,
        max_value=1.0,
        step=0.01,
        format="%.4f",
        key="Cs",
    )


st.markdown("**X-site composition**")

x_col1, x_col2, x_col3 = st.columns(3)

with x_col1:
    Br = st.number_input(
        "Br",
        min_value=0.0,
        max_value=1.0,
        step=0.01,
        format="%.4f",
        key="Br",
    )

with x_col2:
    Cl = st.number_input(
        "Cl",
        min_value=0.0,
        max_value=1.0,
        step=0.01,
        format="%.4f",
        key="Cl",
    )

with x_col3:
    I = st.number_input(
        "I",
        min_value=0.0,
        max_value=1.0,
        step=0.01,
        format="%.4f",
        key="I",
    )


# ============================================================
# Composition check
# ============================================================
a_sum = MA + FA + Cs
x_sum = Br + Cl + I

st.markdown('<div class="section-title">Composition Check</div>', unsafe_allow_html=True)

check_col1, check_col2 = st.columns(2)

with check_col1:
    st.metric("A-site sum", f"{a_sum:.4f}")

with check_col2:
    st.metric("X-site sum", f"{x_sum:.4f}")

if abs(a_sum - 1.0) > 1e-3:
    st.warning("A-site composition does not sum to 1. Please check MA + FA + Cs.")

if abs(x_sum - 1.0) > 1e-3:
    st.warning("X-site composition does not sum to 1. Please check Br + Cl + I.")


# ============================================================
# Prediction
# ============================================================
st.markdown('<div class="section-title">Prediction</div>', unsafe_allow_html=True)

predict_button = st.button(
    "Predict Bandgap",
    type="primary",
    use_container_width=True,
)

if predict_button:
    try:
        bandgap = predictor.predict_one(
            MA=MA,
            FA=FA,
            Cs=Cs,
            Br=Br,
            Cl=Cl,
            I=I,
        )

        st.markdown(
            f"""
<div class="result-card">
    <div class="small-note">Predicted Bandgap</div>
    <div class="result-value">{bandgap:.6f} eV</div>
</div>
""",
            unsafe_allow_html=True,
        )

    except Exception as e:
        st.error(f"Prediction failed: {e}")


# ============================================================
# Footer
# ============================================================
st.markdown("---")

st.markdown(
    """
<div class="small-note" style="text-align:center;">
Developed for perovskite bandgap modeling with SENN.
</div>
""",
    unsafe_allow_html=True,
)
