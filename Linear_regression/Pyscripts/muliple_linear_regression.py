import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from google.colab import files
import matplotlib.pyplot as plt
import seaborn as sns

files.upload()

data = pd.read_csv("/content/50_Startups.csv")
data.head()

corr_matrix = data.corr().round(2)
fig, ax = plt.subplots(figsize=(5,5))
sns.heatmap(data = corr_matrix, annot = True, linewidths = .5, ax = ax)

x = data.iloc[:,:-1]
y = data.iloc[:,-1]
print(x.shape,y.shape)
y.head()
x.head()

from sklearn.preprocessing import LabelEncoder, OneHotEncoder
labelencoder = LabelEncoder()
x.iloc[:,3] = labelencoder.fit_transform(x.iloc[:, 3])

x_train, x_test, y_train, y_test = train_test_split(x,y,test_size=1/3,random_state = 0)
regressor = LinearRegression()
regressor.fit(x_train,y_train)
res = regressor.predict(x_test)

plt.scatter(range(0,17),y_test,color = 'red')
plt.scatter(range(0,17),res,color='green')
y_test.shape
