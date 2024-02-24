# Run this app with `python app.py` and
# visit http://127.0.0.1:8050/ in your web browser.


from dash import Dash, html, dcc
import plotly.express as px
import pandas as pd

app = Dash(__name__)


df = pd.read_csv('data/pink_morsel_final.csv')

fig = px.line(df, x="date", y="sales", color="region", title= 'Pink Morsel Sales over Time')

app.layout = html.Div(children=[
    html.H1(children='Soul Foods'),

    html.Div(children='''
        Were sales higher before or after the Pink Morsel price increase on the 15th of January, 2021?
    '''),

    dcc.Graph(
        id='example-graph',
        figure=fig
    )
])

if __name__ == '__main__':
    app.run(debug=True)
