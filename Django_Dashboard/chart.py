 import pandas as pd
import bokeh
from bokeh.plotting import figure
from bokeh.io import show

def chart_func():
    df = pd.read_csv('../datasets/appstore_games_march_2021.csv', low_memory=False)
    df = df.dropna()
    df.loc[df['price'].str.contains('Free'), 'price'] = '0'
    df['price']= df['price'].str.replace('$', '')
    df['price'] = pd.to_numeric(df['price'],errors='coerce')
    df['release_date'] = pd.to_datetime(df['release_date'], format = '%Y/%m/%d')
    df_date = pd.DataFrame({'price':df['price']})
    df_date = df_date.set_index(df['release_date'])
    df_date = df_date.sort_values(by=['release_date'])
    fig = figure(x_axis_type='datetime',
             plot_height=650, plot_width=1350,
             title='Date vs App Price')
	fig.line(y='price', x='release_date', source=df_date)
	return fig

chart_func()
