import pandas as pd

df = pd.DataFrame({'A': [1, 2, 3, 4, 5, 6, 6, 7], 'B': [5, 4, 2, 7, 1, 3, 6, 0]})

print(df.describe())
print(df.median())
print(df['A'].mode())
print(df.sum())
print(df.var())
print(df.corr())
print(df.cov())
