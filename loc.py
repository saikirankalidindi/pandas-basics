import pandas as pd
import numpy as np

# df = pd.DataFrame(np.random.randn(8, 4),
# index=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h'], columns=['A', 'B', 'C', 'D'])
#
# # select all rows for a specific column
# print(df.loc['a':'d', 'A':'B'])


df = pd.DataFrame(np.random.randn(8, 4), columns=['A', 'B', 'C', 'D'])

print(df.iloc[:4, 1:3])
