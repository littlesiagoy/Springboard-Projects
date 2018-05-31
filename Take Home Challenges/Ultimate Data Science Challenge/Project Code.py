import pandas as pd
import seaborn as sns

''' Exploratory Data Analysis '''
########################################################################################################################
########################################################################################################################

raw_data = pd.read_json('logins.json')
data = pd.DataFrame(raw_data).set_index('login_time').sort_index()
data['Logins Count'] = 1

agg_data = data.resample('15T').count()


