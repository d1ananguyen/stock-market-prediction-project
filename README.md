# 📊 Stock Market Prediction Project 

A machine learning project that predicts future stock prices based on historical NASDAQ data.  
We use Python, Jupyter Notebooks, `yfinance`, and regression models to explore and forecast trends.

We use a dataset of historical daily prices for all tickers currently trading on **NASDAQ**, sourced via the [`yfinance`](https://pypi.org/project/yfinance/) Python package and originally hosted on [Kaggle](https://www.kaggle.com/datasets/jacksoncrow/stock-market-dataset/data).

The goal is to build models that learn from past stock price movements and make accurate predictions about future prices.

### 🧠 Problem Statement
> **Input**: Historical stock prices (Open, High, Low, Close, Volume, etc.)  
> **Output**: Predicted future stock price (e.g., next day's closing price)

### 📊 Dataset Summary
- Contains daily stock price data for NASDAQ-listed companies
- Retrieved using the `yfinance` package
- Tickers include major companies like Apple (AAPL), Google (GOOG), Tesla (TSLA), etc.
- Accompanied by a metadata file (`symbols_valid_meta.csv`) describing each stock

This project is a great application of time series forecasting and helps build intuition around financial modeling, feature engineering, and evaluation techniques.

---

<details open>
<summary> <strong>🧱 Project Structure</strong></summary>

```
stock-market-prediction-project/
│                                  # Other folders can be ignored
├── notebooks/
│   └── final_models/              # Folder for all final trained models
│       ├── Baselines/             # Naïve, Moving Average models for comparison
│       ├── CNN/                   # Convolutional Neural Network model
│       ├── DNN/                   # Deep Neural Network model
│       └── MLP/                   # Multilayer Perceptron model
│
├── requirements.txt                # List of dependencies to install
├── README.md                       
└── venv/                           # Your virtual Python environment (not tracked in Git)
```

</details>

---

<details open>
<summary> <strong>⚙️ Setup Instructions</strong></summary>


### ✅ 1. Clone the Repository
```bash
git clone https://github.com/d1ananguyen/stock-market-prediction-project.git
cd stock-market-prediction-project
```

---

<details>
<summary>💡 What is a Virtual Environment?</summary>

A virtual environment is an isolated space where all project-specific Python packages are installed.  
This prevents version conflicts and keeps your global Python installation clean — making sure you and your teammates all work in the same consistent environment.

</details>

### ✅ 2. Create a Virtual Environment (First Time Only)

```bash
python -m venv venv
```

Then activate it:

- **Windows**:
  ```bash
  .\venv\Scripts\activate
  ```

- **Mac/Linux**:
  ```bash
  source venv/bin/activate
  ```

You should now see `(venv)` in your terminal prompt.

---

### 🔁 Every Time You Reopen the Project

Before running or modifying anything in this project, **you must re-activate your virtual environment**.

- **Windows**:
  ```bash
  .\venv\Scripts\activate
  ```

- **Mac/Linux**:
  ```bash
  source venv/bin/activate
  ```

Make sure `(venv)` appears in your terminal before you start working.

---

### ✅ 3. Install Required Packages

```bash
pip install -r requirements.txt
```

This installs all necessary libraries like `pandas`, `matplotlib`, `seaborn`, `yfinance`, and `scikit-learn`.

---

### ✅ 4. Learn to Use Jupyter Notebooks 

If you're new to Jupyter Notebooks or want a refresher, here are some helpful video walkthroughs and tutorials:

- 📺 [Jupyter Notebooks in VS Code Walkthrough](https://www.youtube.com/watch?v=DA6ZAHBPF1U)
- 📘 [Getting Started with Jupyter Notebooks in VS Code](https://www.youtube.com/watch?v=suAkMeWJ1yE)
- 🧠 [Why Use Jupyter Notebooks?](https://www.youtube.com/watch?v=cKFp8DBF75Y)

These will help you understand how to navigate, run cells, and make the most out of your notebooks for this project.

</details>

---
