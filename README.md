# Forex Historical Data Ingestion Module ( 😉FREE )

## Overview

This Python module facilitates the ingestion of historical forex data for the EUR/USD currency pair using the `dukascopy_python` library. It retrieves 15-minute OHLCV (Open, High, Low, Close, Volume) data for a specified date range, adjusts the timestamps, and saves the data to a CSV file. This module is designed for traders, data analysts, and developers who need reliable forex historical data for backtesting trading strategies or conducting market analysis.

## Features

- **Data Retrieval**: Fetches historical OHLCV data for EUR/USD from Dukascopy.
- **Customizable Date Range**: Allows users to specify start and end dates for data collection. 
- **Timestamp Adjustment**: Adjusts timestamps by a user-defined offset (e.g., +3 hours).
- **CSV Export**: Saves the retrieved data to a CSV file for further analysis.
- **Simple Integration**: Easy-to-use script that integrates with Python data analysis workflows.

## Prerequisites

Before using this module, ensure you have the following installed:

- Python 3.6 or higher
- `dukascopy_python` library
- `pandas` library (included as a dependency with `dukascopy_python`)

### Installation

1. Install Python from [python.org](https://www.python.org/downloads/) if not already installed.
2. Install the required library using pip:

   ```bash
   pip install dukascopy-python
   ```

3. Verify the installation:

   ```bash
   python -c "import dukascopy_python; print(dukascopy_python.__version__)"
   ```

## Usage

### Code Example

The following script demonstrates how to use the module to fetch 15-minute EUR/USD data, adjust timestamps, and save the output to a CSV file:

```python
from datetime import datetime, timedelta
import dukascopy_python
from dukascopy_python.instruments import INSTRUMENT_FX_MAJORS_EUR_USD

# Define date range
start = datetime(2020, 1, 1)
end = datetime(2025, 8, 1)

# Fetch 15-minute OHLCV data
df = dukascopy_python.fetch(
    instrument=INSTRUMENT_FX_MAJORS_EUR_USD,
    interval=dukascopy_python.INTERVAL_MIN_15,
    offer_side=dukascopy_python.OFFER_SIDE_BID,
    start=start,
    end=end,
)

# Adjust timestamp by +3 hours
df.index = df.index + timedelta(hours=3)

# Save to CSV
df.to_csv("EURUSD_15min.csv")
print(df.head(), df.shape)
```

### Explanation of Parameters

- `instrument`: Specifies the forex pair (e.g., `INSTRUMENT_FX_MAJORS_EUR_USD` for EUR/USD).
- `interval`: Sets the time interval for data (e.g., `INTERVAL_MIN_15` for 15-minute data).
- `offer_side`: Defines the bid or ask price (`OFFER_SIDE_BID` for bid prices).
- `start` and `end`: Datetime objects specifying the date range for data retrieval.
- `timedelta(hours=3)`: Adjusts the timestamp of the data by adding 3 hours.

### Output

- The script generates a CSV file named `EURUSD_15min.csv` containing the OHLCV data.
- The `print` statement displays the first five rows of the DataFrame and its shape (rows, columns).

Example output of `print(df.head(), df.shape)`:

```
                           open    high     low   close  volume
2025-01-01 03:00:00  1.0800  1.0810  1.0795  1.0805    1000
2025-01-01 03:15:00  1.0805  1.0820  1.0800  1.0815    1200
2025-01-01 03:30:00  1.0815  1.0825  1.0810  1.0820    1100
2025-01-01 03:45:00  1.0820  1.0830  1.0815  1.0825    1300
2025-01-01 04:00:00  1.0825  1.0835  1.0820  1.0830    1150
(10000, 5)
```

## Repository Structure

```
forex-data-ingestion/
├── README.md              # This file
├── fetch_forex_data.py    # Main script for data ingestion
├── EURUSD_15min.csv       # Output CSV file (generated after running the script)
```

## Installation Instructions for Repository

1. Clone the repository:

   ```bash
   git clone https://github.com/frostyalce000/forex-data-ingestion-free-dukacopy.git
   cd forex-data-ingestion
   ```

2. Install dependencies:

   ```bash
   pip install dukascopy-python
   ```

3. Run the script:

   ```bash
   python fetch_forex_data.py
   ```

## Customization

- **Change Currency Pair**: Modify the `instrument` parameter to fetch data for other pairs (e.g., `INSTRUMENT_FX_MAJORS_USD_JPY` for USD/JPY). Refer to `dukascopy_python.instruments` for available pairs.
- **Adjust Time Interval**: Use other intervals like `INTERVAL_MIN_1`, `INTERVAL_HOUR_1`, or `INTERVAL_DAY_1` as needed.
- **Timestamp Adjustment**: Modify the `timedelta` value to adjust timestamps differently (e.g., `timedelta(hours=-5)` for a 5-hour subtraction).
- **Output Format**: Replace `df.to_csv` with `df.to_parquet` or other formats for alternative storage options.

## Notes

- **Data Availability**: Ensure the date range specified is within the available data period provided by Dukascopy. Future dates (e.g., beyond the current date) will result in no data being returned.
- **API Limits**: Be aware of any rate limits or restrictions imposed by Dukascopy's data service. Check the [Dukascopy documentation](https://www.dukascopy.com/) for details.
- **Error Handling**: Add try-except blocks for robust error handling in production environments.

## Contributing

Contributions are welcome! To contribute:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Make your changes and commit (`git commit -m "Add new feature"`).
4. Push to the branch (`git push origin feature-branch`).
5. Open a pull request with a detailed description of your changes.

## Acknowledgments

- [Dukascopy](https://www.dukascopy.com/) for providing historical forex data.
- [dukascopy-python](https://github.com/Leo4815162342/dukascopy-node) for the Python wrapper used in this module.[](https://github.com/Leo4815162342/dukascopy-node)