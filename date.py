import pandas as pd

data = pd.date_range('1/1/2023', periods=10, freq='M')

df = pd.DataFrame()
df['Date'] = data
df['Year'] = df['Date'].dt.year
df['Month'] = df['Date'].dt.month
df['Day'] = df['Date'].dt.day
df['Hours'] = df['Date'].dt.hour
df['Minutes'] = df['Date'].dt.minute
print(df)
t = pd.Timestamp.now()
# print(t.to_datetime64())
print(t.year,t.month,t.day)
