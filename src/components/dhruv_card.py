import dash_bootstrap_components as dbc
from dash import dcc

def dhruv_card():
    return dbc.Card(
        dbc.CardBody([
            dcc.Graph(id='xxx', style={'height': '100%', 'width': '100%'})
        ], style={'display': 'flex', 'flex-direction': 'column', 'height': '100%', 'overflow': 'hidden'}), 
        className="mb-4 shadow",
        style={'display': 'flex', 'flex-direction': 'column', 'height': '60vh', 'min-height': '400px'}
    )