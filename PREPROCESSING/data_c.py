# import pandas as pd
# import numpy as np

# # Sample messy data
# data = {
#     'Name': ['Alice', 'Bob', 'Charlie', 'bob', 'Eve', None],
#     'Age': [25, np.nan, 30, 29, 999, 22],
#     'Email': ['alice@example.com', 'bob@example.com', 'charlie@example.com', 'bob@example.com', None, 'eve@example.com'],
#     'City': ['New York', 'los angeles', 'New York', 'LOS ANGELES', 'Chicago', 'Chicago']
# }

# # Load into a DataFrame
# df = pd.DataFrame(data)

# print("Original Data:")
# print(df)

# # Step 1: Remove duplicates
# df = df.drop_duplicates()

# # Step 2: Handle missing values
# df['Name'] = df['Name'].fillna('Unknown')
# df['Age'] = df['Age'].replace(999, np.nan)  # Replace outlier with NaN
# df['Age'] = df['Age'].fillna(df['Age'].median())  # Fill missing ages with median
# df['Email'] = df['Email'].fillna('noemail@example.com')

# # Step 3: Standardize formatting
# df['Name'] = df['Name'].str.title()  # Capitalize names
# df['City'] = df['City'].str.title()  # Capitalize city names

# # Step 4: Final cleaned data
# print("\nCleaned Data:")
# print(df)

import pandas as pd
from sklearn.preprocessing import OneHotEncoder

# Sample dataset
df = pd.DataFrame({
    'City': ['New York', 'Paris', 'London', 'Paris', 'New York']
})

print("Original Data:")
print(df)

# Initialize encoder with sparse=False to get dense array
encoder = OneHotEncoder(sparse_output=False)
encoder.fit(df)
encoder.transform(df)

# Fit and transform the City column
encoded_array = encoder.fit_transform(df[['City']])

# Get feature names (column names after encoding)
feature_names = encoder.get_feature_names_out(['City'])

# Create a DataFrame with encoded features
encoded_df = pd.DataFrame(encoded_array, columns=feature_names)

# Combine with original data (if needed)
df_encoded = pd.concat([df, encoded_df], axis=1)

print("\nEncoded Data:")
print(df_encoded)
