import pandas as pd

df = pd.DataFrame({
    'id': [403, 440, 451, 430, 429],
    'names': ['sai', 'suresh', 'gopi', 'sushu', 'vinnu'],
    'location': ['hyd', 'blg', 'bza', 'blg', 'hyd']
})

df2 = pd.DataFrame({
    'names': ['sai', 'suresh', 'gopi', 'sushu', 'vinnu'],
    'company': ['wipro', 'tcs', 'infosys', 'accenture', 'deloitte'],
    'salary': [25000, 28000, 21000, 35000, 47000]
})
ser = pd.Series(['2km', '4km', '1km', '5km', '3km'], name='Distance')
print(df)
print(df2)

print(pd.merge(df2, df, on='names'))

print(pd.concat([df, df2, ser], axis=1))

# print(df.join(df2))
print(pd.concat([df, ser], axis=1))
