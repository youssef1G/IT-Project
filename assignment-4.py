import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df=pd.read_csv("healthcare-dataset.csv")

df.drop(['id'],axis=1,inplace=True)

df.fillna(value=df['bmi'].mean(),inplace=True)
print(df)
plt.scatter(df['age'],df['bmi'])
plt.xlabel('age')
plt.ylabel('bmi')

sns.pairplot(df)
plt.show()