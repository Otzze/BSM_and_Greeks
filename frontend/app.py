from BSM.bsm_pricing import compute_prices, compute_greeks
import streamlit as st

# Page config
st.set_page_config(page_title="Option Pricing Calculator", layout="centered")

# Title
st.title("Option Pricing Calculator App")

# Sidebar for user inputs
st.sidebar.header("User Input Parameters")

# Get user inputs
s = st.sidebar.number_input("Current Stock Price (S)", value=100.0, step=1.0)
k = st.sidebar.number_input("Option Strike Price (K)", value=100.0, step=1.0)
T = st.sidebar.number_input("Time to Expiration (T in years)", value=1.0, step=0.01)
r = st.sidebar.number_input("Risk-Free Interest Rate (r)", value=0.05, step=0.01)
sigma = st.sidebar.number_input("Volatility (σ)", value=0.2, step=0.01)

st.sidebar.markdown(
    """
    ### ℹ️ Notes
    - Time to expiration (T) is in years.
    - Risk-free rate (r) and volatility (σ) should be annualized.
    """
)

# Main content
st.header("Option Prices")
if st.sidebar.button("Calculate Option Prices", key="calculate"):
    call_price, put_price = compute_prices(s, k, T, r, sigma)

    # Compute Greeks
    call_greeks = compute_greeks(s, k, T, r, sigma, option_type='call')
    put_greeks = compute_greeks(s, k, T, r, sigma, option_type='put')

    col1, col2 = st.columns(2)

    with col1:
        st.markdown(
            f"""
            <div style="background-color:#d4edda; padding:20px; border-radius:10px;">
                <h3 style="color:#155724; text-align:center;">CALL</h3>
                <p style="font-size:30px; text-align:center;"><strong>${call_price:.2f}</strong></p>
                <hr style="border-top: 1px solid #155724;">
                <ul style="color:#155724; font-size:16px; list-style: none;">
                    <li><strong>Delta:</strong> {call_greeks[0]:.4f}</li>
                    <li><strong>Gamma:</strong> {call_greeks[1]:.4f}</li>
                    <li><strong>Theta:</strong> {call_greeks[2]:.4f}</li>
                    <li><strong>Vega:</strong> {call_greeks[3]:.4f}</li>
                    <li><strong>Rho:</strong> {call_greeks[4]:.4f}</li>
                </ul>
            </div>
            """,
            unsafe_allow_html=True
        )

    with col2:
        st.markdown(
            f"""
            <div style="background-color:#f8d7da; padding:20px; border-radius:10px;">
                <h3 style="color:#721c24; text-align:center;">PUT</h3>
                <p style="font-size:30px; text-align:center;"><strong>${put_price:.2f}</strong></p>
                <hr style="border-top: 1px solid #721c24;">
                <ul style="color:#721c24; font-size:16px; list-style: none;">
                    <li><strong>Delta:</strong> {put_greeks[0]:.4f}</li>
                    <li><strong>Gamma:</strong> {put_greeks[1]:.4f}</li>
                    <li><strong>Theta:</strong> {put_greeks[2]:.4f}</li>
                    <li><strong>Vega:</strong> {put_greeks[3]:.4f}</li>
                    <li><strong>Rho:</strong> {put_greeks[4]:.4f}</li>
                </ul>
            </div>
            """,
            unsafe_allow_html=True
        )
else:
    st.info("Enter parameters in the sidebar and click **Calculate Option Prices**.")

