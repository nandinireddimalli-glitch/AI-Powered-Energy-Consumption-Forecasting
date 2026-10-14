from __future__ import annotations

import argparse
from pathlib import Path

from src.pipeline import run_pipeline

def main():
    parser = argparse.ArgumentParser(
        description="Educational energy consumption forecasting with a reproducible synthetic dataset."
    )
    parser.add_argument("--data", default="data/energy_consumption.csv",
                        help="Path to CSV with timestamp and energy_kwh columns.")
    parser.add_argument("--forecast-hours", type=int, default=24,
                        help="Number of future hourly values to forecast.")
    parser.add_argument("--force-synthetic", action="store_true",
                        help="Regenerate the sample dataset even if the CSV already exists.")
    args = parser.parse_args()
    run_pipeline(Path(args.data), forecast_hours=args.forecast_hours,
                 force_synthetic=args.force_synthetic)

if __name__ == "__main__":
    main()
