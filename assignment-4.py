import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import MinMaxScaler

df=pd.read_csv("healthcare-dataset.csv")

df.drop(['id'],axis=1,inplace=True)

df.fillna(value=df['bmi'].mean(),inplace=True)

lb=LabelEncoder()
df['gender']=lb.fit_transform(df['gender'])
df['ever_married']=lb.fit_transform(df['ever_married'])
df['work_type']=lb.fit_transform(df['work_type'])
df['Residence_type']=lb.fit_transform(df['Residence_type'])
df['smoking_status']=lb.fit_transform(df['smoking_status'])

scaler=MinMaxScaler()
df= scaler.fit_transform(df)


print(df_scaler_minMax.min())
print(df_scaler_minMax.max())

plt.scatter(df['age'],df['bmi'])
plt.xlabel('age')
plt.ylabel('bmi')

sns.pairplot(df)
plt.show()
