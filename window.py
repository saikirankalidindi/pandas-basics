# importing the necessary module.
import pandas as pd

# creating a timestamp data frame.
data = pd.DataFrame({"X": 1},
                    index=[
    pd.Timestamp("20130101 09:00:01"),
    pd.Timestamp("20130101 09:00:02"),
    pd.Timestamp("20130101 09:00:03"),
    pd.Timestamp("20130101 09:00:04"),
    pd.Timestamp("20130101 09:00:06"),
],
)
print(data)

data['Right'] = data.rolling('2s', closed='right').X.sum()
data['Both'] = data.rolling('2s', closed='both').X.sum()
data['Left'] = data.rolling('2s', closed='left').X.sum()
data['Neither'] = data.rolling('2s', closed='neither').X.sum()
print(data)
