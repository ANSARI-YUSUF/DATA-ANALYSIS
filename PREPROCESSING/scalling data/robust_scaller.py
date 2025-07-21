from sklearn.preprocessing import RobustScaler
import pandas as pd

data = {'Salary': [30000, 35000, 40000, 1000000, 32000]}  # 1,000,000 is an outlier
df = pd.DataFrame(data)

scaler = RobustScaler()
scaled = scaler.fit_transform(df)

print(pd.DataFrame(scaled, columns=['Salary']))
