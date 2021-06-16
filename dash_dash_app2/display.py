import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import dash_table
import modin.pandas as pd

data_url = 'https://raw.githubusercontent.com/plotly/datasets/master/2014_usa_states.csv'
df = pd.read_csv("displaydata.csv",index_col=[0])
#df.columns = ['Countries','Gender','Age group','Size Count']


app = dash.Dash(__name__)


colors = {
    'background': '#111111',
    'text': '#7FDBFF'
}




app.layout = html.Div([
	html.H1("Users Interactive Plot", style={
            'textAlign': 'center',
            'color': colors['background']
        }),
    dash_table.DataTable(
        id='table',
        columns=[{"name": i, "id": i} 
                 for i in df.columns],
        data=df.to_dict('records'),
        style_cell=dict(textAlign='center', font_family = "cursive",font_size= '16px'),
        style_header=dict(backgroundColor="#879CD9",font_family='sans-serif',
                font_size= '20px'),
        style_data=dict(backgroundColor="lavender")
    )
])

app.run_server(debug=True,host='0.0.0.0',port='8050')