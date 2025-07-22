import pandas as pd
import numpy as np

# Sample messy data
fpath="openpowerlifting.csv"
# print(fpath)
data = pd.read_csv(fpath) 

# # Load into a DataFrame
df = pd.DataFrame(data)

print("Original Data:")
print(df.describe())
print(df.info())

# Step 1: Remove duplicates
df = df.drop_duplicates()
# print(df.describe())
# print(df.info())


# Step 2: Handle missing values
# # df['Name'] = df['Name'].fillna('Unknown')

median_age = df['Age'].median()
# print(median_age)

df['Age'].fillna(median_age, inplace=True)
nan_in_row = df['Age'].isna()
# print(nan_in_row)
# median_age = df['Age'].median()
ahe100=df.loc[df['Age'] > 90, 'Age']
# print(df.loc[df['Age'] > 100, 'Age'] )
# print(ahe100.head())
# df['Age'] = df['Age'<100].fillna(median_age) # Replace outlier with NaN
# # df['Age'] = df['Age'].fillna(df['Age'].median())  # Fill missing ages with median
# # df['Email'] = df['Email'].fillna('noemail@example.com')

# # Step 3: Standardize formatting
# # df['Name'] = df['Name'].str.title(p
# # Step 4: Final cleaned data
# print("\nCleaned Data:")
# print(df)


# print(df.describe())
print(df.info())
print(df.head())