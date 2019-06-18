# Linear Regression in python
import numpy as np
import pandas as pd
from sklearn.model_selection import test_train_split
from sklearn.linear_model import LinearRegression
from google.colab import files

'''
Get the data set from the following link: (Salary_data.csv)
			--> https://sds-platform-private.s3-us-east-2.amazonaws.com/uploads/P14-Simple-Linear-Regression.zip			
'''
#upload the data File
files.upload()

data = pd.read_csv("/content/Salary_Data.csv")

# Check the sample data
print(data.head())

# x = attributes[0]
x = data.iloc[:, :1].values

# y = feature[0]
y = data.iloc[:, 1].values

# Note: x is a 2D array and y is a 1D array!

# Split the data into test and train data 
X_train, x_test, Y_train, y_test = train_test_split(x,y, test_size = 1/3, random_state = 0)

regression = LinearRegression()
regression.fit(X_train, Y_train)

Y_pred = regression.predict(X_test)
#plt.scatter(X_train, y_train, color = 'red')
plt.scatter(X_test, y_pred, color = 'black')
plt.scatter(X_test, y_test, color = 'green')

#plt.plot(X_train, regressor.predict(X_train), color = 'blue')
plt.title('Salary vs Experience (Training set)')
plt.xlabel('Years of Experience')
plt.ylabel('Salary')
plt.show()
