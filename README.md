# AI-Powered Energy Consumption Forecasting System

A beginner-friendly, GitHub-ready machine-learning project that forecasts hourly electricity consumption using Python, Pandas, scikit-learn, and a reproducible virtual simulation dataset.

> **Data transparency:** The default data is synthetic and generated locally. It is not sourced from a real home, building, utility, or company. This project is for education and portfolio demonstration, not live grid operations.

## Problem statement
Energy operators need estimates of future demand to plan capacity, understand peak periods, and make informed efficiency decisions. This project demonstrates an end-to-end forecasting workflow on hourly building energy data.

## Features
- Automatic generation of two years of synthetic hourly energy data
- Data validation, cleaning, and summary statistics
- Calendar, lag, and rolling-window feature engineering
- Chronological train/test split
- Comparison of Linear Regression and Random Forest
- Evaluation using MAE, RMSE, and R²
- Recursive forecast for the next 24 hours (configurable)
- Saved model, metrics, CSV outputs, and graphs

## Tech stack
- Python 3.11 or 3.12
- Pandas, NumPy
- scikit-learn
- Matplotlib
- Joblib

## Architecture

```text
Hourly energy CSV (or synthetic data generator)
                  |
                  v
       Validation and cleaning
                  |
                  v
 Calendar + lag + rolling features
                  |
                  v
       Chronological train/test
                  |
                  v
  Linear Regression vs Random Forest
                  |
                  v
      MAE / RMSE / R² evaluation
                  |
          +-------+--------+
          |                |
          v                v
  Test predictions    Future forecast
          |                |
          +-------+--------+
                  v
       CSVs + JSON + PNG graphs
```

## Folder structure

```text
AI-Energy-Forecasting/
├── data/                  # Generated dataset and data instructions
├── notebooks/             # Optional exploratory notebooks
├── src/                   # Data, features, models, pipeline, plotting
├── models/                # Saved fitted model (generated)
├── outputs/               # Metrics and prediction CSVs (generated)
├── images/                # PNG visualizations (generated)
├── docs/                  # Project report
├── main.py                # Entry point
├── requirements.txt
├── .gitignore
└── README.md
```

## Installation

### Windows PowerShell

```powershell
py -3.11 -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

If PowerShell blocks activation, run `Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass` and activate again.

### macOS / Linux

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

## Run the project

From the repository root:

```bash
python main.py
```

To forecast the next 48 hours:

```bash
python main.py --forecast-hours 48
```

To regenerate the synthetic data:

```bash
python main.py --force-synthetic
```

On first run, the program creates `data/energy_consumption.csv`. It then cleans the data, trains two models, compares test metrics, selects the model with the lower RMSE, forecasts future consumption, and saves the outputs.

## Generated outputs

- `outputs/evaluation_metrics.json` — dataset details, model metrics, selected model
- `outputs/test_predictions.csv` — actual and predicted values for the held-out test period
- `outputs/future_forecast.csv` — next N hourly forecasts
- `models/best_energy_forecaster.joblib` — selected fitted model
- `images/energy_history.png` — historical consumption plot
- `images/actual_vs_predicted.png` — test-period comparison
- `images/error_distribution.png` — forecast residual distribution
- `images/future_forecast.png` — future forecast graph

Open the generated graphs on Windows with:

```powershell
explorer .\images
```

## Dataset format for real data
If replacing the generated dataset, provide a CSV with:
- `timestamp`: parseable date/time
- `energy_kwh`: numeric hourly energy use

Keep real/private customer data out of GitHub. Confirm licensing before using external datasets.

## Evaluation and limitations
The script reports Mean Absolute Error (MAE), Root Mean Squared Error (RMSE), and R². Results vary with data and environment; use the generated metrics rather than inventing scores. Synthetic data is useful for demonstrating the pipeline but does not prove performance on real facilities. The future forecast is recursive and can accumulate error. This project is not a live energy-management or billing system.

## Industry relevance
The workflow is related to demand planning for smart buildings, manufacturing sites, data centers, electricity providers, and renewable-energy operations. A production system would need real metering data, weather and calendar inputs, operational monitoring, retraining, access controls, and validation before decisions are made from predictions.

## Learning outcomes
- Time-series data preparation and chronological validation
- Lag and rolling-window features
- Regression model comparison
- Forecast metrics and error analysis
- Reproducible Python project organization
- Saving model artifacts, CSV outputs, and visual evidence

## Suggested portfolio proof
1. Commit the initial project structure.
2. Commit dataset generation and cleaning.
3. Commit feature engineering.
4. Commit model comparison and evaluation.
5. Commit visualizations and example output screenshots.
6. Add a short report explaining results and limitations.

## License
Add an appropriate license if you intend others to reuse the code. The included project does not grant rights to third-party datasets you may add later.
