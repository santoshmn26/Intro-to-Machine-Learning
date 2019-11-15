## Tips on ML workflow

### Techniques to handle categorical data
We have to be careful choosing the right converters

Label encoding: same columnn convert cat to int values
problem: some algorithm treats higher values with more bias

Ex:
ori 	new_col
a 	 	1 	
b		2 
a		1
c 		3


One hot encoding: Creates switches, new columns are created = number of distinct values in the original cat column
Ex:
ori 	new_a	new_b	new_c
a 		1		0		0
b 		0 		1		0
a 		1   	0		0
c 		0		0		1



# Function to dummy all the categorical variables used for modeling
```
def dummy_df(df, todummy_list):
    for x in todummy_list:
        dummies = pd.get_dummies(df[x], prefix=x, dummy_na=False)
        df = df.drop(x, 1)
        df = pd.concat([df, dummies], axis=1)
    return df 


```


## check models performance
### To get model's mean absolute error

from sklearn import mean_absolute_error