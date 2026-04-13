import pandas as pd
import numpy as np
import os

print("📊 Generating dataset...")

# ✅ Create data folder automatically
os.makedirs("data", exist_ok=True)

# Create dates
dates = pd.date_range(start="2023-01-01", end="2023-12-31")

# Generate energy values
np.random.seed(42)
energy = 200 + np.cumsum(np.random.normal(2, 5, len(dates)))

# Create dataframe
df = pd.DataFrame({
    "Date": dates,
    "Energy": energy.astype(int)
})

# Save file
df.to_csv("data/energy.csv", index=False)

print("✅ Dataset created successfully!")
print("📁 Check: data/energy.csv")