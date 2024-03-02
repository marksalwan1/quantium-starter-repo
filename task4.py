from dash import Dash, html, dcc, Input, Output
import plotly.express as px
import pandas as pd

app = Dash(__name__)

df = pd.read_csv('data/pink_morsel_final.csv')

app.layout = html.Div(children=[
    html.H1(children='Soul Foods', style={'textAlign': 'center', 'color': '#007BFF'}),
    
    html.Div(children='''
        Were sales higher before or after the Pink Morsel price increase on the 15th of January, 2021?
    ''', style={'textAlign': 'center', 'margin': '20px'}),
    
    dcc.RadioItems(
        id='region-selector',
        options=[
            {'label': 'North', 'value': 'north'},
            {'label': 'East', 'value': 'east'},
            {'label': 'South', 'value': 'south'},
            {'label': 'West', 'value': 'west'},
            {'label': 'All', 'value': 'all'}
        ],
        value='all',
        labelStyle={'display': 'inline-block', 'margin': '10px'},
        style={'textAlign': 'center'}
    ),
    
    dcc.Graph(id='sales-graph')
])

@app.callback(
    Output('sales-graph', 'figure'),
    Input('region-selector', 'value')
)
def update_graph(selected_region):
    if selected_region == 'all':
        filtered_df = df
    else:
        filtered_df = df[df['region'] == selected_region]
    
    fig = px.line(filtered_df, x="date", y="sales", color="region", title='Pink Morsel Sales over Time')
    return fig

if __name__ == '__main__':
    app.run_server(debug=True)
