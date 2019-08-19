# Pandas


| Command | Desc |
| ------- | ---- |
| df.drop('col_name',axis=1) | Drops the column col_name |
| df.head(n) | Show top n rows, Default = 5 |
| df.shape | Displays the shape of the df (count(rows),count(cols)) |
| df.columns | Displays the cols / Header of the df |
| df['col_name'].sum() | Returns the sum of the col |
| df['col_name'].distinct() | Returns the distinct values of the col |
| df.duplicated() | Returns the number of records duplicated |
| df.drop_duplicates() | Drop all duplicated |
| df['col_name'].notnull() |  To check the records that is not null |
| df['col_name'].value_counts() | for a given col, give the count for each distinct values |



## Examples:

### Drop a column in a pandas df
```
new_df = df.drop('col_name',axis=1)
```

### Show top 5 rows
```
df.head(n)
# Default = 5
```

### Number of rows and cols
```
df.shape
```

### Get number of duplicate records in the DF
```
sum(df.duplicated())
```

### Drop duplicates in a df
```
print(sum(df.duplicated()))
df.drop_duplicates()
```

### Get total number of records that is not null
```
print(sum(df['col_name'].notnull()))
```

### Get count of all distinct values in the first col
```
print(df['col_1'].values_counts())
```

