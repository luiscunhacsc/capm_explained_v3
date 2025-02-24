import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

#############################################
# 1) Define callback functions for CAPM labs:
#############################################
def reset_capm_parameters():
    st.session_state["rf_slider"] = 2.0   # 2%
    st.session_state["rm_slider"] = 8.0   # 8%
    st.session_state["beta_slider"] = 1.0

def set_lab1_capm_parameters():
    st.session_state["rf_slider"] = 2.0   # 2%
    st.session_state["rm_slider"] = 8.0   # 8%
    st.session_state["beta_slider"] = 1.0

def set_lab2_capm_parameters():
    st.session_state["rf_slider"] = 3.0   # 3%
    st.session_state["rm_slider"] = 10.0  # 10%
    st.session_state["beta_slider"] = 1.5

def set_lab3_capm_parameters():
    st.session_state["rf_slider"] = 1.0   # 1%
    st.session_state["rm_slider"] = 7.0   # 7%
    st.session_state["beta_slider"] = 0.5

#############################################
# 2) CAPM Calculation Function
#############################################
def capm_expected_return(rf, rm, beta):
    """
    CAPM: E(R_i) = R_f + beta*(E(R_m)-R_f)
    Inputs:
      rf   : risk-free rate (in decimals)
      rm   : expected market return (in decimals)
      beta : asset beta
    Returns:
      Expected return (in decimals)
    """
    return rf + beta * (rm - rf)

#############################################
# 3) Configure the Streamlit App
#############################################
st.set_page_config(layout="wide")
st.title("📈 Understanding the CAPM Model")
st.markdown("Explore how an asset’s expected return is determined by its risk relative to the market using the Capital Asset Pricing Model (CAPM).")

#############################################
# 4) Sidebar: CAPM Parameters and Disclaimer
#############################################
with st.sidebar:
    st.header("⚙️ CAPM Parameters")
    st.button("↺ Reset Parameters", on_click=reset_capm_parameters)
    
    # Sliders for input parameters (expressed in percentage for easier reading)
    rf = st.slider("Risk-Free Rate (Rₒ) [%]", 0.0, 10.0, 2.0, step=0.1, key='rf_slider') / 100
    rm = st.slider("Expected Market Return (E(Rₘ)) [%]", 0.0, 20.0, 8.0, step=0.1, key='rm_slider') / 100
    beta = st.slider("Asset Beta (β)", -2.0, 3.0, 1.0, step=0.1, key='beta_slider')
    
    st.markdown("---")
    st.markdown(
    """
    **⚠️ Disclaimer**  
    *Educational purposes only. This tool is intended for learning about the CAPM model and should not be used for actual investment decisions.*
    """
    )
    st.markdown(
    """
    <div style="margin-top: 20px;">
        <a href="https://creativecommons.org/licenses/by-nc/4.0/" target="_blank">
            <img src="https://licensebuttons.net/l/by-nc/4.0/88x31.png" alt="CC BY-NC 4.0">
        </a>
        <br>
        <span style="font-size: 0.8em;">By Luís Simões da Cunha</span>
    </div>
    """, unsafe_allow_html=True)

#############################################
# 5) Main Calculation and Tabs
#############################################
# Calculate CAPM expected return
expected_return = capm_expected_return(rf, rm, beta)

# Create tabs for different sections
tab1, tab2, tab3, tab4, tab5 = st.tabs([
    "🎮 Interactive Tool", 
    "📚 Theory Behind CAPM", 
    "📖 Comprehensive Tutorial", 
    "🛠️ Practical Labs",
    "🧠 The Very Basics of CAPM"
])

#############################################
# Tab 1: Interactive CAPM Calculator
#############################################
with tab1:
    st.subheader("Interactive CAPM Calculator")
    st.markdown(f"### Expected Return: **{expected_return*100:.2f}%**")
    
    col1, col2 = st.columns([1, 2])
    with col1:
        st.markdown("**CAPM Equation:**")
        st.latex(r"E(R_i) = R_f + \beta \, (E(R_m) - R_f)")
        st.markdown(f"""
        - **Risk-Free Rate (Rₒ):** {rf*100:.2f}%
        - **Expected Market Return (E(Rₘ)):** {rm*100:.2f}%
        - **Beta (β):** {beta:.2f}
        """)
    with col2:
        # Plot the Security Market Line (SML)
        beta_range = np.linspace(-2, 3, 100)
        expected_returns_range = rf + beta_range * (rm - rf)
        fig, ax = plt.subplots(figsize=(10, 5))
        ax.plot(beta_range, expected_returns_range*100, color='blue', linewidth=2, label="Security Market Line (SML)")
        ax.scatter([beta], [expected_return*100], color='red', label="Your Asset", zorder=5)
        ax.set_title("Security Market Line (CAPM)")
        ax.set_xlabel("Beta (β)")
        ax.set_ylabel("Expected Return (%)")
        ax.grid(True)
        ax.legend()
        st.pyplot(fig)

#############################################
# Tab 2: Theory Behind CAPM
#############################################
with tab2:
    st.markdown("""
    ## CAPM: Theoretical Foundations

    The **Capital Asset Pricing Model (CAPM)** explains the relationship between systematic risk and expected return for assets, particularly stocks.

    **Key Concepts:**
    - **Risk-Free Rate (Rₒ):** The return of a riskless investment (e.g., government bonds).
    - **Beta (β):** Measures an asset's volatility relative to the market.
    - **Market Risk Premium:** The excess return of the market over the risk-free rate, i.e., (E(Rₘ) - Rₒ).

    **CAPM Equation:**
    $$
    E(R_i) = R_f + \\beta_i (E(R_m) - R_f)
    $$

    This model implies that an asset’s expected return increases with its beta. In other words, assets with higher systematic risk should offer higher expected returns.
    """)

#############################################
# Tab 3: Comprehensive CAPM Tutorial
#############################################
with tab3:
    st.markdown("""
    ## Comprehensive CAPM Tutorial

    **What you'll learn:**
    
    1. **Understanding Beta:**  
       - Beta measures the asset's sensitivity to overall market movements.
       - A beta of 1 means the asset moves in line with the market.
       - Betas above 1 indicate more volatility; below 1 indicate less.
       
    2. **Risk-Free Rate & Market Return:**  
       - The risk-free rate is your baseline return.
       - The market return represents the average return expected from the market.
       - The difference (market risk premium) compensates investors for taking on extra risk.
       
    3. **Calculating Expected Return:**  
       - Use the CAPM formula to see how variations in beta, Rₒ, and E(Rₘ) impact an asset's expected return.
       - Experiment with the interactive tool by adjusting the sliders.
       
    4. **Interpreting the Security Market Line (SML):**  
       - The SML graphically represents the relationship between beta and expected return.
       - Your asset’s position on this line can indicate whether it is fairly priced given its risk.
       
    Use the controls in the sidebar to change parameters and observe the effects in real time!
    """)

#############################################
# Tab 4: Practical Labs
#############################################
with tab4:
    st.header("🔬 Practical CAPM Labs")
    lab_choice = st.radio(
        "Select a Lab:",
        ("Lab 1: Baseline Analysis", "Lab 2: High Beta Asset", "Lab 3: Defensive Asset"),
        index=0
    )
    
    if lab_choice == "Lab 1: Baseline Analysis":
        st.subheader("Baseline Analysis")
        st.markdown("""
        **Scenario:**  
        Analyze an asset with a beta of 1 (moving in line with the market).  
        **Parameters:**
        - Risk-Free Rate: 2%
        - Expected Market Return: 8%
        - Beta: 1.0
        """)
        st.button("⚡ Set Lab 1 Parameters", on_click=set_lab1_capm_parameters, key="lab1_capm")
    
    elif lab_choice == "Lab 2: High Beta Asset":
        st.subheader("High Beta Asset Analysis")
        st.markdown("""
        **Scenario:**  
        Investigate an asset that is more volatile than the market.  
        **Parameters:**
        - Risk-Free Rate: 3%
        - Expected Market Return: 10%
        - Beta: 1.5
        """)
        st.button("⚡ Set Lab 2 Parameters", on_click=set_lab2_capm_parameters, key="lab2_capm")
    
    else:
        st.subheader("Defensive Asset Analysis")
        st.markdown("""
        **Scenario:**  
        Explore an asset with lower volatility.  
        **Parameters:**
        - Risk-Free Rate: 1%
        - Expected Market Return: 7%
        - Beta: 0.5
        """)
        st.button("⚡ Set Lab 3 Parameters", on_click=set_lab3_capm_parameters, key="lab3_capm")

#############################################
# Tab 5: The Very Basics of CAPM
#############################################
with tab5:
    st.header("🧠 The Very Basics of CAPM")
    st.markdown("""
    **What is CAPM?**
    
    - **CAPM (Capital Asset Pricing Model)** is used to estimate the expected return on an asset based on its systematic risk.
    - Investors are compensated for both the time value of money (via the risk-free rate) and the risk taken (via beta and the market risk premium).
    
    **The Basic Equation:**
    
    $$
    E(R_i) = R_f + \\beta (E(R_m) - R_f)
    $$
    
    **Key Takeaways:**
    - A higher beta suggests higher risk—and therefore, a higher expected return.
    - The model assumes efficient markets and rational investors.
    - It provides a foundation for portfolio management and asset pricing.
    """)
