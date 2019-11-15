## Tips on ML workflow

### Techniques to handle categorical data
There are multiple ways to convert categorical data to numerical data
We have to be careful choosing the right methods.

## Label encoding: In the same columnn categorical data is converted to numerical data
problem: This can cause some issue with some ML algorithms since some algorithm treats higher values with more bias

Ex:
| ori | new_col |
| --- | ------- |
| a | 1 |
| b	| 2 |
| a	| 1 |
| c | 3 |


## One hot encoding: Creates switches, 
new columns are created = number of distinct values in the original cat column
Problem: Problem with this approch is if the original column has more distinct values
then the dimension of the data is going to increase significantly.

Also some newly generated columns can be highly co-related which can impact negatively on some ML models.

Ex:
| ori | new_a | new_b | new_c |

| --- | ----- | ----- | ----- |

| a | 1 | 0 | 0 |

| b | 0 | 1 | 0 |

| a | 1 | 0 | 0 |

| c | 0 | 0 | 1 |


## Using pandas get_dummies: It is very similar to  One hot encoding, this package is availabe under Pandas 
where as one hot encoder is under sklearn preprocessing package.

Ex:
| ori | new_a | new_b | new_c |

| --- | ----- | ----- | ----- |

| a | 1 | 0 | 0 |

| b | 0 | 1 | 0 |

| a | 1 | 0 | 0 |

| c | 0 | 0 | 1 |

# Function to dummy all the categorical variables used for modeling
```
def dummy_df(df, todummy_list):
    for x in todummy_list:
        dummies = pd.get_dummies(df[x], prefix=x, dummy_na=False)
        df = df.drop(x, 1)
        df = pd.concat([df, dummies], axis=1)
    return df 

```

## Check the Performance of a model
### Get the Accuracy of a model
### Get model's mean absolute error

```
from sklearn import mean_absolute_error
from sklearn.metrics import accuracy_score
from sklearn.linear_model import LogisticRegression

model = LogisticRegression()

accuracy_score(y_test,y_pred)*100) 
model.score(X_train,y_train)*100) 			# same as above.
mean_absolute_error(X_test,y_test)

```
