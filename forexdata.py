from datetime import datetime, timedelta
import dukascopy_python
from dukascopy_python.instruments import INSTRUMENT_FX_MAJORS_EUR_USD

# Define date range
start = datetime(2025, 1, 1)
end = datetime(2025, 8, 1)

# Fetch 1-minute OHLCV data
df = dukascopy_python.fetch(
    instrument=INSTRUMENT_FX_MAJORS_EUR_USD,
    interval=dukascopy_python.INTERVAL_MIN_15,
    offer_side=dukascopy_python.OFFER_SIDE_BID,
    start=start,
    end=end,
)

# Reduce timestamp by 3 hours
df.index = df.index + timedelta(hours=3)

# Save to CSV
df.to_csv("EURUSD_15min.csv")
print(df.head(), df.shape)
