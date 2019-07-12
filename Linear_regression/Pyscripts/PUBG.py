import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns 
from google.colab import files, drive
import warnings
warnings.filterwarnings("ignore")

drive.mount('/content/gdrive')

data = pd.read_csv("/content/gdrive/My Drive/PUBG/train_V2.csv")

print(data.shape)
data.head()

pros = data.loc[data['kills'] > data['kills'].quantile(0.99)]
noobs = data.loc[data['kills'] < 1 ]
data.loc[data['kills'] > data['kills'].quantile(0.99)] = 8


print("Total pro players: ", pros.shape[0])
print("Total noobs and bots: ", noobs.shape[0])


plt.figure(figsize=(10,7))
sns.countplot(data['kills'].sort_values())

correlation_matrix = data.corr().round(2)
fig, ax = plt.subplots(figsize=(20,20))
sns.heatmap(data = correlation_matrix, annot = True, linewidths = .5, ax = ax)

data.dtypes.sort_values()
print(data['matchType'].unique())

data['matchType'] = data['matchType'].map(lambda x: 'squad' if('squad' in x) else 'duo' if('duo' in x) else 'solo')
data.head()

from sklearn.preprocessing import LabelEncoder
labelencoder = LabelEncoder()
categorical_data_index = [0,1,2,25]
for i in categorical_data_index:
  data.iloc[:,i] = labelencoder.fit_transform(data.iloc[:, i].astype(str))
data.head()

for col in data.columns:
  print("Null values for "+col,": ",sum(data[col].isnull()))
print("Duplicated data: ",sum(data.duplicated()))

data = data.drop_duplicates()
data = data[data['winPlacePerc'].notnull()]
print("Confirm droping of duplicates :", sum(data.duplicated()))

x_train = data.iloc[:, :-1]
y_train = data.iloc[:, -1]
print(x_train.shape,y_train.shape)


test_data = pd.read_csv("/content/gdrive/My Drive/PUBG/test_V2.csv")
test_data['matchType'] = test_data['matchType'].map(lambda x: 'squad' if('squad' in x) else 'duo' if('duo' in x) else 'solo')
test_data.head()

from sklearn.preprocessing import LabelEncoder
categorical_data_index = [0,1,2,15]
for i in categorical_data_index:
  test_data.iloc[:,i] = labelencoder.fit_transform(test_data.iloc[:, i].astype(str))
test_data.head()  

from sklearn.linear_model import LinearRegression
regressor_2 = LinearRegression()
regressor_2.fit(x_train,y_train)

pred = regressor_2.predict(test_data)

print("Model score: ",round(regressor_2.score(x_train,y_train) * 100))

x_train.head()