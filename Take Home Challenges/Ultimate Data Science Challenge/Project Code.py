import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

''' Exploratory Data Analysis '''
########################################################################################################################
########################################################################################################################

raw_data = pd.read_json('logins.json')
data = pd.DataFrame(raw_data).set_index('login_time').sort_index()
data['Logins Count'] = 1

agg_data = data.resample('15T').count()

len(data.resample('1M').count())

# plt.plot(agg_data)

# The data seems to follow a natural ebb and flow pattern.

# We resample the data to find out that the data contains 4 month worth of data.

agg_data_month = data.resample('1M').count()

# 16 weeks worth of data.
agg_data_week = data.resample('1W').count()

# 103 Days worth of data.
agg_data_days = data.resample('1D').count()

# We plot the different timeframes to see if a clear pattern emerges.
fig, axes = plt.subplots(2, 2)
axes[0, 0].plot(agg_data_month, marker='o')
axes[0, 0].set_title('Month')
axes[0, 1].plot(agg_data_week, marker='o')
axes[0, 1].set_title('Week')
axes[1, 0].plot(agg_data_days, marker='o')
axes[1, 0].set_title('Day')
axes[1, 1].plot(agg_data, marker='o')
axes[1, 1].set_title('Overall')

data.head(200)

data.to_excel('test.xlsx')