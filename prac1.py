# importing pandas as pd for using data frame
import pandas as pd

df = pd.DataFrame({
    'id': [403, 440, 451, 430, 429],
    'names': ['sai', 'suresh', 'gopi', 'sushu', 'vinnu'],
    'location': ['hyderabad', 'banglore', 'noida', 'banglore', 'hyderabad']
})
df2 = pd.DataFrame({
    'names': ['sai', 'suresh', 'gopi', 'sushu', 'vinnu'],
    'company': ['wipro', 'tcs', 'infosys', 'accenture', 'deloitte'],
    'salary': [25000, 28000, 21000, 35000, 47000]
})
total_df = pd.merge(df, df2, on='names')

grp = total_df.groupby('location')

for idx, data in grp:
    print("______________", str(idx).upper(), "______________")
    print(data)


