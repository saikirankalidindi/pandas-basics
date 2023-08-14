import pandas as pd

data = dict(name=['sai', 'suresh', 'gopi', 'jhansi'],
            company=['WIPRO', 'DELOITTE', 'TCS', 'INFOSYS'],
            salary=[25000, 47000, 28000, 21850])


def adder(ele1, ele2):
    return ele1+ele2


df = pd.DataFrame(data)
print(df.describe())


df['salary'].pipe(adder, 1500)
print(df.describe())
