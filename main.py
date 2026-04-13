import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, r2_score
import os

# Create outputs folder automatically
os.makedirs("outputs", exist_ok=True)
# Load dataset
df = pd.read_csv('data/energy.csv')

print(df.head())

# Convert date
df['Date'] = pd.to_datetime(df['Date'])
df = df.sort_values('Date')

# Feature engineering
df['day'] = df['Date'].dt.day
df['month'] = df['Date'].dt.month

# Lag feature
df['lag1'] = df['Energy'].shift(1)
df = df.dropna()

print(df.head())

# Features and target
X = df[['day', 'month', 'lag1']]
y = df['Energy']

# Train-test split
split = int(len(df) * 0.8)
X_train, X_test = X[:split], X[split:]
y_train, y_test = y[:split], y[split:]

# Model
model = RandomForestRegressor()
model.fit(X_train, y_train)

# Predictions
y_pred = model.predict(X_test)

# Evaluation
rmse = np.sqrt(mean_squared_error(y_test, y_pred))
r2 = r2_score(y_test, y_pred)

print("RMSE:", rmse)
print("R2:", r2)

# Plot
plt.plot(y_test.values, label='Actual')
plt.plot(y_pred, label='Predicted')
plt.legend()
plt.savefig('outputs/prediction.png')
plt.show()