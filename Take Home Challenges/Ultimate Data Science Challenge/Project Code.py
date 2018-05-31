import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

''' Exploratory Data Analysis '''
########################################################################################################################
########################################################################################################################

raw_data = pd.read_json('logins.json')
data = pd.DataFrame(raw_data).set_index('login_time').sort_index()
data['Logins Count'] = 1

'Aggregate Data'
#######################################################################################################################
# Aggregate the data to include every 15 mins.
agg_data = data.resample('15T').count()


agg_data_month = data.resample('1M').count()
# We have 4 months worth of data.


agg_data_week = data.resample('1W').count()
# We have 16 weeks worth of data.

agg_data_days = data.resample('1D').count()
# We have 103 days worth of data.

agg_data_hour = data.resample('1H').count()

'Visualize the Aggregated Data'
#######################################################################################################################
# We plot the different timeframes to see if a clear pattern emerges.
fig, axes = plt.subplots(2, 2)
axes[0, 0].plot(agg_data_month, marker='o')
axes[0, 0].set_title('Month')
axes[0, 1].plot(agg_data_week, marker='o')
axes[0, 1].set_title('Week')
axes[1, 0].plot(agg_data_days, marker='o')
axes[1, 0].set_title('Day')
axes[1, 1].plot(agg_data)
axes[1, 1].set_title('Overall')

# It is clear that there is a weekly ebb and flow.

'Outlier Detection'
########################################################################################################################
# TODO: LOF on the dataset.


'Important Feature of Demand'
########################################################################################################################
# TODO: Heatmap of hour & day of the week.


data.to_excel('test.xlsx')




''' Data Issues '''
# The first day that data is collected only start from 20:00:00, the last day stops at 19:00:00
# Do a pivot table of hours & dates and we see that Jan 8th unexpected logged 0 log ins at hour 15