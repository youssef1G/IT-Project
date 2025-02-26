import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.metrics import roc_curve,auc
from sklearn.naive_bayes import GaussianNB
from sklearn.preprocessing import MinMaxScaler
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report,confusion_matrix




df= pd.read_csv('Heart attack.csv')

print(df.head())
print(df.info())
print(df.isnull().sum())
print(df.duplicated().sum())

x=df.iloc[:,:-1]
y=df.iloc[:,-1]


scaler=MinMaxScaler()
x=scaler.fit_transform(x)


x_train, x_test, y_train,y_test = train_test_split(x,y,test_size=0.3,random_state=2,stratify=y)

gb=GaussianNB()
gb.fit(x_train,y_train)

print('accuracy of train: ',gb.score(x_train,y_train))
print('accuracy of test: ',gb.score(x_test,y_test))


DTmodel =DecisionTreeClassifier(criterion='entropy')

DTmodel.fit(x_train,y_train)
print('accuracy of train tree model: ',DTmodel.score(x_train,y_train))
print('accuracy of test tree model: ',DTmodel.score(x_test,y_test))



rfmodel=RandomForestClassifier(n_estimators=18,criterion='entropy',max_depth=50)
rfmodel.fit(x_train,y_train)
print('accuracy of train random forest model: ',rfmodel.score(x_train,y_train))
print('accuracy of test random forest model: ',rfmodel.score(x_test,y_test))

y_pred=rfmodel.predict(x_test)

cm=confusion_matrix(y_test,y_pred)
print(cm)
from sklearn.metrics import roc_curve, auc

y_probs = rfmodel.predict_proba(x_test)[:,1]
fpr, tpr, _ = roc_curve(y_test, y_probs)
roc_auc = auc(fpr, tpr)
plt.figure(figsize=(6,4))
plt.plot(fpr, tpr, color='blue', lw=2, label='AUC = %0.2f' % roc_auc)
plt.plot([0, 1], [0, 1], color='grey', linestyle='--')
plt.xlabel("False Positive Rate")
plt.ylabel("True Positive Rate")
plt.title("ROC Curve")
plt.legend()
plt.show()




y_probs = DTmodel.predict_proba(x_test)[:,1]
fpr, tpr, _ = roc_curve(y_test, y_probs)
roc_auc = auc(fpr, tpr)
plt.figure(figsize=(6,4))
plt.plot(fpr, tpr, color='blue', lw=2, label='AUC = %0.2f' % roc_auc)
plt.plot([0, 1], [0, 1], color='grey', linestyle='--')
plt.xlabel("False Positive Rate")
plt.ylabel("True Positive Rate")
plt.title("ROC Curve")
plt.legend()
plt.show()