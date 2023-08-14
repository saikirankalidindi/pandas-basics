import pandas as pd
import numpy as np

N = 20
df = pd.DataFrame({
    'A': pd.date_range(start='2016-01-01', periods=N, freq='D'),
    'x': np.linspace(0, stop=N - 1, num=N),
    'y': np.random.rand(N),
    'C': np.random.choice(['Low', 'Medium', 'High'], N).tolist(),
    'D': np.random.normal(100, 10, size=N).tolist()
})

for k, v in df.items():
    print(k, v)

for i, s in df.iterrows():
    print(i, s)

for row in df.itertuples():
    print(row)
