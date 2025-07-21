from sklearn.preprocessing import MinMaxScaler
import pandas as pd

data = {'Age': [22, 25, 47, 52, 46]}
df = pd.DataFrame(data)

scaler = MinMaxScaler()
scaled = scaler.fit_transform(df)

print(pd.DataFrame(scaled, columns=['Age']))
