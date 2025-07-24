import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

import warnings as w
w.filterwarnings('ignore')
pd.set_option('display.max_columns',None)



df =pd.read_csv('jobs_dataset.csv')
sample=df.sample(5)
# print(df.head())



# checking the data set
shape=df.shape

print(# identify the coloums
df.columns)


desc=df.describe(include="all")
print(desc)


# info reading the data set
info=df.info()

print(info)


plt.figure(figsize=(10, 10))

# Top 8 locations for better visualization
top_8_locations = df['location'].value_counts().head(8)

# Create donut chart
colors = sns.color_palette("husl", len(top_8_locations))
wedges, texts, autotexts = plt.pie(top_8_locations.values, 
                                  labels=top_8_locations.index, 
                                  autopct='%1.1f%%', colors=colors,
                                  startangle=90, pctdistance=0.85)

# Create donut effect
centre_circle = plt.Circle((0,0), 0.70, fc='white')
fig = plt.gcf()
fig.gca().add_artist(centre_circle)

plt.title('Geographic Distribution of Top Job Markets', 
          fontsize=16, fontweight='bold')
plt.axis('equal')
plt.tight_layout()
plt.show()
