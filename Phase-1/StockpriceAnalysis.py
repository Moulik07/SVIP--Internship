import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
file_path = 'RELIANCE.csv'  # Update with your file path if different
reliance_df = pd.read_csv(file_path)

# Convert 'Date' to datetime object
reliance_df['Date'] = pd.to_datetime(reliance_df['Date'])

# Fill missing values with 0
reliance_df_filled = reliance_df.fillna(0)

# Adding a new column for daily price change
reliance_df_filled['Daily Price Change'] = reliance_df_filled['Close'] - reliance_df_filled['Open']

# Time-Series Plot for Closing Prices
plt.figure(figsize=(12, 6))
plt.plot(reliance_df_filled['Date'], reliance_df_filled['Close'], label='Closing Price')
plt.title('Reliance Industries Closing Price Trend')
plt.xlabel('Year')
plt.ylabel('Closing Price (INR)')
plt.legend()
plt.show()

# Histogram for Daily Price Changes
plt.figure(figsize=(8, 6))
reliance_df_filled['Daily Price Change'].hist(bins=50)
plt.title('Distribution of Daily Price Changes')
plt.xlabel('Daily Price Change (INR)')
plt.ylabel('Frequency')
plt.show()

# Bar Plot for Average Trading Volume per Year
reliance_df_filled['Year'] = reliance_df_filled['Date'].dt.year
avg_volume_per_year = reliance_df_filled.groupby('Year')['Volume'].mean()
avg_volume_per_year.plot(kind='bar', figsize=(12, 6))
plt.title('Average Trading Volume per Year')
plt.xlabel('Year')
plt.ylabel('Average Volume')
plt.show()
