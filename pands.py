import pandas as pd
import numpy as np

df=pd.read_csv(r'C:\Users\20101\OneDrive\Documents\data.csv',index_col='rank')


head=df.head()
print(head)

rows,cols=df.shape
print(rows,cols)










