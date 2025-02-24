```markdown
# Capital Asset Pricing Model (CAPM) Explained

## Overview

The **Capital Asset Pricing Model (CAPM)** is a foundational financial model that estimates the expected return of an asset based on its systematic risk (β). This interactive Streamlit application allows users to explore how changes in key parameters—such as the risk-free rate, expected market return, and asset beta—affect the expected return of an asset. It includes interactive tools, comprehensive tutorials, practical labs, and theoretical foundations, all designed for educational purposes.

## Table of Contents
- [Overview](#overview)
- [Features](#features)
- [Installation](#installation)
  - [Prerequisites](#prerequisites)
  - [Cloning the Repository](#cloning-the-repository)
  - [Creating a Virtual Environment](#creating-a-virtual-environment)
  - [Installing Dependencies](#installing-dependencies)
- [Usage](#usage)
- [Troubleshooting](#troubleshooting)
- [Editing the Code](#editing-the-code)
- [Additional Resources](#additional-resources)
- [Support](#support)
- [License & Legal Disclaimer](#license--legal-disclaimer)

## Features

- **Interactive Calculator:** Adjust CAPM parameters using sliders and view the expected return in real time.
- **Security Market Line Visualization:** Plot the Security Market Line (SML) and see how your asset compares.
- **Tabbed Content:** Explore multiple tabs including an interactive tool, CAPM theory, comprehensive tutorials, practical labs, and the basics.
- **Practical Labs:** Pre-set scenarios to analyze baseline, high beta, and defensive assets.
- **Educational Content:** Detailed explanations and tutorials to deepen your understanding of CAPM.

## Installation

### Prerequisites

Before setting up the project locally, ensure you have:

1. **A Computer:** Windows, macOS, or Linux.
2. **Python 3.9 or Higher:** (Python 3.12 is preferred).  
   Download from: [python.org/downloads](https://www.python.org/downloads/)
3. **Visual Studio Code (VS Code):**  
   Download from: [code.visualstudio.com](https://code.visualstudio.com/)
4. **Git:** (Optional, but recommended for cloning the repository).  
   Download from: [git-scm.com/downloads](https://git-scm.com/downloads)

### Cloning the Repository

#### Option 1: Cloning via Git (Recommended)

1. Open Terminal (macOS/Linux) or Command Prompt/PowerShell (Windows).
2. Navigate to your desired directory:
   ```bash
   cd Documents
   ```
3. Clone the repository:
   ```bash
   git clone https://github.com/luiscunhacsc/capm_explained_v3.git
   ```
4. Enter the project folder:
   ```bash
   cd capm_explained_v3
   ```

#### Option 2: Download as ZIP

1. Visit [https://github.com/luiscunhacsc/capm_explained_v3](https://github.com/luiscunhacsc/capm_explained_v3).
2. Click on **Code > Download ZIP**.
3. Extract the ZIP file to your preferred location.

### Creating a Virtual Environment

1. Open VS Code and navigate to the project folder.
2. Open the integrated terminal (Ctrl + ` in VS Code or select *Terminal > New Terminal*).
3. Create a virtual environment:
   ```bash
   python -m venv venv
   ```
4. Activate the virtual environment:
   - **On Windows:**
     ```bash
     venv\Scripts\activate
     ```
   - **On macOS/Linux:**
     ```bash
     source venv/bin/activate
     ```

### Installing Dependencies

After activating the virtual environment, install the required packages:
```bash
python -m pip install --upgrade pip
pip install -r requirements.txt
```
This command installs libraries such as:
- **Streamlit** – For the interactive UI.
- **NumPy** – For numerical computations.
- **Matplotlib** – For plotting visualizations.

## Usage

To launch the CAPM application:

1. Ensure your virtual environment is activated.
2. Run the following command:
   ```bash
   streamlit run capm_explained.py
   ```
3. The application should open automatically in your web browser at [http://localhost:8501](http://localhost:8501). If it does not, open your browser and navigate to that URL manually.

## Troubleshooting

- **ModuleNotFoundError:**  
  Make sure the virtual environment is activated (`venv\Scripts\activate` on Windows or `source venv/bin/activate` on macOS/Linux).

- **Python Not Recognized:**  
  Ensure that Python is installed and properly added to your system's PATH.

- **Browser Does Not Open Automatically:**  
  Open your browser and navigate to [http://localhost:8501](http://localhost:8501).

## Editing the Code

To customize or enhance the application:

1. Open `capm_explained.py` in VS Code.
2. Modify the code as needed.
3. After saving your changes, restart the Streamlit app by stopping the current session (Ctrl + C) and running:
   ```bash
   streamlit run capm_explained.py
   ```

## Additional Resources

- **Streamlit Documentation:** [docs.streamlit.io](https://docs.streamlit.io)
- **CAPM Overview:** [Investopedia CAPM Guide](https://www.investopedia.com/terms/c/capm.asp)
- **Modern Portfolio Theory:** [Investopedia Modern Portfolio Theory](https://www.investopedia.com/terms/m/modernportfoliotheory.asp)

## Support

For issues, suggestions, or contributions, please open an issue on GitHub:  
[https://github.com/luiscunhacsc/capm_explained_v3/issues](https://github.com/luiscunhacsc/capm_explained_v3/issues)

## License & Legal Disclaimer

This project is licensed under the [CC BY-NC 4.0 License](https://creativecommons.org/licenses/by-nc/4.0/).

**By Luís Simões da Cunha**

This software is provided for educational purposes only. All information and results generated by this tool are intended solely for educational use and should not be construed as financial, investment, or professional advice. The author makes no guarantees regarding the accuracy, reliability, or completeness of the information provided. Use of this software is entirely at your own risk, and the author shall not be held liable for any errors, inaccuracies, or damages arising from its use.

---

Happy exploring the Capital Asset Pricing Model (CAPM)!
```