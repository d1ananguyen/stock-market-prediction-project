# 📊 Stock Market Prediction Project (COSC 4368)

A machine learning project that predicts future stock prices based on historical NASDAQ data.  
We use Python, Jupyter Notebooks, `yfinance`, and regression models to explore and forecast trends.

---

## 🧱 Project Structure

```
stock-market-prediction-project/
│
├── data/                            # All data files
│   ├── individual_tickers/         # Historical data for specific stocks (e.g., AAPL)
│   │   └── AAPL_historic.csv
│   ├── grouped_tickers/            # (Optional) Folder for grouped/combined data
│   └── symbols_valid_meta.csv      # Metadata for all NASDAQ-listed tickers
│
├── notebooks/
│   ├── exploration/                # Initial analysis + data visualization
│   │   ├── diana-exploration.ipynb
│   │   ├── david-exploration.ipynb
│   │   └── jr-exploration.ipynb
│   └── modeling/                   # Machine learning model notebooks
│
├── requirements.txt                # List of dependencies to install
├── README.md                       # You're here! Project overview + setup instructions
└── venv/                           # Your virtual Python environment (not tracked in Git)
```

---

## ⚙️ Setup Instructions

### ✅ 1. Clone the Repository
```bash
git clone https://github.com/your-username/stock-market-prediction-project.git
cd stock-market-prediction-project
```

---

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

### ✅ 3. Install Required Packages

```bash
pip install -r requirements.txt
```

This installs all necessary libraries like `pandas`, `matplotlib`, `seaborn`, `yfinance`, and `scikit-learn`.

---

### ✅ 4. Run Jupyter Notebooks in VS Code

- Open the repo in VS Code
- Click any `.ipynb` file to open it in the interactive notebook interface
- Use `Shift + Enter` to run cells
- Use the sidebar or file tree to navigate between exploration and modeling notebooks

---

## 🔍 Notebook Breakdown

| Notebook                     | Purpose |
|------------------------------|---------|
| `diana-exploration.ipynb`    | Loads AAPL data, visualizes prices & trends |
| `david-exploration.ipynb`    | Teammate's exploration of another stock |
| `jr-exploration.ipynb`       | Metadata analysis and filtering |
| `modeling/`                  | Where ML models (e.g., regression) will be built and evaluated |

---

## 📦 Data Files

- **`symbols_valid_meta.csv`**: Metadata about NASDAQ stocks (used to filter valid tickers)
- **`AAPL_historic.csv`**: Apple Inc. stock data pulled from Yahoo Finance
- Add more stocks in `individual_tickers/` for multi-stock modeling

---

## 🧠 Model Goal

> **Input**: Historical stock data  
> **Output**: Future closing price prediction

We’ll experiment with different regression models to forecast prices using features like closing price, volume, moving averages, and trends.

---

## 🙌 Contributions

Each team member can:
- Add their own exploration notebook inside `notebooks/exploration/`
- Add model versions inside `notebooks/modeling/`
- Pull/Push from GitHub regularly to stay in sync

---

Let me know if you want help structuring your model notebook or if you need a template for reporting results!