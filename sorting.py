import pandas as pd
import numpy as np
data = {'pcs': [4, 3, 5, 7, 8, 9, 1], 'prc': [1, 2, 3, 4, 5, 6, 0]}

unsorted_df = pd.DataFrame(data, index=[4, 3, 7, 2, 9, 1, 0])
print(unsorted_df)

sorted_df = unsorted_df.sort_index(axis=1, ascending=False)
print(sorted_df)

sortedv_df = unsorted_df.sort_values(by='pcs')

print(sortedv_df)





