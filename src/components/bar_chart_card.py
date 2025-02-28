import dash_bootstrap_components as dbc
from dash import dcc

def bar_chart_card():
    return dbc.Card(
        dbc.CardBody([
            dcc.Graph(id='plot', style={'height': '100%', 'width': '100%'}) 
        ], style={'height': '100%', 'overflow': 'hidden'}),
        style={'display': 'flex', 'flex-direction': 'column', 'height': '57.5vh', 'min-height': '400px'}
    )
