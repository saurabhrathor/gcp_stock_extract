from alpha_vantage.timeseries import TimeSeries
import pandas as pd
#from google.cloud import bigquery
from pandas.io import gbq
import pdb
import datetime

#pdb.set_trace()

ALPHA_VANTAGE_API_KEY = '47MP5C3EGNFQ177U'
yesterday = (datetime.datetime.today() - datetime.timedelta(days=1)).strftime('%Y-%m-%d')

ts = TimeSeries(key=ALPHA_VANTAGE_API_KEY, output_format='pandas')

intraday_data, data_info = ts.get_intraday('GOOGL', outputsize='full', interval='1min')

intraday_data_sort = intraday_data.sort_index()

intraday_data_sort.columns = ['volume', 'open', 'high', 'close', 'low']
intraday_data_sort.reset_index(level=0, inplace=True)

intraday_data_filter = intraday_data_sort[intraday_data_sort['date'] >= yesterday]

intraday_data_filter.to_csv('dump.csv')

# Construct a BigQuery client object.
intraday_data_filter.to_gbq(destination_table = 'stock_data.google_stock_raw', project_id = 'fifth-listener-285620', if_exists='append')
