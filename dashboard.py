import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go

def create_dashboard(data):
    """Crée un dashboard à partir des données passées en paramètre."""
    app = dash.Dash(__name__)
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=data['date'], y=data['price'], mode='lines+markers', name='Prix'))
    app.layout = html.Div(children=[
        html.H1(children='Dashboard'),
        html.Div(children='''
            Evolution du prix dans le temps
        '''),
        dcc.Graph(
            id='graph',
            figure=fig
        )
    ])
    app.run_server(debug=True)
