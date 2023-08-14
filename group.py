import pandas as pd
import numpy as np
from pprint import pprint

ipl_data = dict(
    Team=['Riders', 'Riders', 'Devils', 'Devils', 'Kings', 'Kings', 'Kings', 'Kings', 'Riders', 'Royals', 'Royals',
          'Riders'],
    Rank=[1, 2, 2, 3, 3, 4, 1, 1, 2, 4, 1, 2],
    Year=[2014, 2015, 2014, 2015, 2014, 2015, 2016, 2017, 2016, 2014, 2015, 2017],
    Points=[876, 789, 863, 673, 741, 812, 756, 788, 694, 701, 804, 690])
df = pd.DataFrame(ipl_data)
print(df)
grouped = df.groupby('Year')

for data, group in grouped:
    print(data)
    print(group)

print(grouped.get_group(2014))

print(grouped['Points'].agg(np.mean))
print(grouped.agg(np.size))

group_data = df.groupby('Team')
for data, group in group_data:
    print(data)
    print(group)
print(group_data['Points'].agg([np.sum, np.mean, np.std]))
