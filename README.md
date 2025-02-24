```markdown
# Capital Asset Pricing Model (CAPM) Explained

## 1. What Is This?

The **Capital Asset Pricing Model (CAPM)** is a foundational financial model used to estimate the expected return of an asset based on its systematic risk ($\beta$). The model helps investors understand the relationship between risk and return, making it a cornerstone of modern portfolio theory.

This project includes an interactive application where you can:
- Input key parameters such as the risk-free rate, market return, and beta.
- Visualize how changes in these parameters affect the expected return.
- Explore pedagogical sections explaining the theory behind CAPM, practical applications, and hands-on labs.

## 2. Setting Up a Local Development Environment

To modify and run the code locally, follow these steps:

### 2.1 Prerequisites

1. **A computer** (Windows, macOS, or Linux).
2. **Python 3.9 or higher** (Python 3.12 preferred, but anything 3.9+ should be fine).
   - If you do not have Python installed:
     - Go to [python.org/downloads](https://www.python.org/downloads/) and install the latest version for your system.
3. **Visual Studio Code (VS Code)**
   - Download from [code.visualstudio.com](https://code.visualstudio.com/)
4. **Git** (optional, but recommended for cloning the repository).
   - Install from [git-scm.com/downloads](https://git-scm.com/downloads)

### 2.2 Downloading the Project

#### Option 1: Cloning via Git (Recommended)

1. Open **Terminal** (macOS/Linux) or **Command Prompt** / **PowerShell** (Windows).
2. Navigate to the folder where you want to download the project:
   ```bash
   cd Documents
   ```
3. Run the following command:
   ```bash
   git clone https://github.com/luiscunhacsc/capm_explained_v01.git
   ```
4. Enter the project folder:
   ```bash
   cd capm_explained_v01
   ```

#### Option 2: Download as ZIP

1. Visit [https://github.com/luiscunhacsc/capm_explained_v01](https://github.com/luiscunhacsc/capm_explained_v01)
2. Click **Code > Download ZIP**.
3. Extract the ZIP file into a local folder.

### 2.3 Creating a Virtual Environment

It is recommended to use a virtual environment (`venv`) to manage dependencies:

1. Open **VS Code** and navigate to the project folder.
2. Open the integrated terminal (`Ctrl + ~` in VS Code or `Terminal > New Terminal`).
3. Run the following commands to create and activate a virtual environment:
   ```bash
   python -m venv venv
   ```
   - On Windows:
     ```bash
     venv\Scripts\activate
     ```
   - On macOS/Linux:
     ```bash
     source venv/bin/activate
     ```

### 2.4 Installing Dependencies

After activating the virtual environment, install the required dependencies:

```bash
python.exe -m pip install --upgrade pip
pip install -r requirements.txt
```

This installs libraries such as:
- **Streamlit** (for the interactive UI)
- **NumPy** (for mathematical calculations)
- **Matplotlib** (for plotting results)

## 3. Running the Application

To launch the application, execute:

```bash
streamlit run capm_explained.py
```

This should open a new tab in your web browser with the interactive tool. If it does not open automatically, check the terminal for a URL (e.g., `http://localhost:8501`) and open it manually.

### 3.1 Troubleshooting

- **ModuleNotFoundError:** Ensure the virtual environment is activated (`venv\Scripts\activate` or `source venv/bin/activate`).
- **Python not recognized:** Ensure Python is installed and added to your system's PATH.
- **Browser does not open:** Manually enter the `http://localhost:8501` URL in your browser.

## 4. Editing the Code

If you want to make modifications:
1. Open `capm_explained.py` in **VS Code**.
2. Modify the code as needed.
3. Restart the Streamlit app after changes (`Ctrl + C` to stop, then rerun `streamlit run capm_explained.py`).

## 5. Additional Resources

- **Streamlit Documentation**: [docs.streamlit.io](https://docs.streamlit.io)
- **CAPM Overview**: [Investopedia Guide](https://www.investopedia.com/terms/c/capm.asp)
- **Modern Portfolio Theory**: [Investopedia Guide](https://www.investopedia.com/terms/m/modernportfoliotheory.asp)

## 6. Support

For issues or suggestions, open an **Issue** on GitHub:
[https://github.com/luiscunhacsc/capm_explained_v01/issues](https://github.com/luiscunhacsc/capm_explained_v01/issues)

---
*Happy exploring the Capital Asset Pricing Model (CAPM)!*
```