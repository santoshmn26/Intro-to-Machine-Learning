# Pacakegs to import
import numpy as np
from sklearn.linear_model import LinearRegression
import pandas as pd
from sklearn.model_selection import train_test_split
from google.colab import files
import matplotlib.pyplot as plt

# Upload files when working in google colab
files.upload()
data = pd.read_csv("/content/Salary_Data.csv")

print(data.head())
# Split the data for dependent variable and feature variable 
x = data.iloc[:,:1]   # Note feature variable is 2D numpy array
y = data.iloc[:,1]    # Feature variable is a 1D numpy array

print(x.shape, y.shape)

# Split the data into test and train data 30:70

x_train, x_test, y_train, y_test = train_test_split(x,y,test_size=1/3,random_state=1)

# Create a regressor to train and test the data
regressor = LinearRegression()
regressor.fit(x_train,y_train)

# Predict the regressor
pred = regressor.predict(x_test)

# Plot the data
plt.scatter(x_train, y_train, color = 'red')
plt.scatter(x_test,pred,color= 'green')
