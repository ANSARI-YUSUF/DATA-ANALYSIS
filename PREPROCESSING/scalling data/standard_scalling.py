import pandas as pd
from sklearn.preprocessing import StandardScaler

# Sample data
data = {
    'Age': [22, 25, 47, 52, 46],
    'Salary': [15000, 29000, 48000, 60000, 52000]
}

df = pd.DataFrame(data)
print("Original Data:")
print(df)

# Initialize the scaler
scaler = StandardScaler()

# Fit and transform the data
scaled_array = scaler.fit_transform(df)

# Create a scaled DataFrame
scaled_df = pd.DataFrame(scaled_array, columns=['Age', 'Salary'])

print("\nScaled Data (StandardScaler):")
print(scaled_df)
