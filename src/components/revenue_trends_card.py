import dash_bootstrap_components as dbc
from dash import dcc

def revenue_trends_card():
    return dbc.Card(
        dbc.CardBody([
            dcc.Graph(id='revenue-trends', style={'height': '100%', 'width': '100%'}) 
        ], style={'height': '100%', 'overflow': 'hidden'}),
        style={'display': 'flex', 'flex-direction': 'column', 'height': '48vh', 'min-height': '400px'}
    )
