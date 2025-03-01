import dash_bootstrap_components as dbc
from dash import dcc

from components.general import metric_toggle

def map_card():
    return dbc.Card(
        dbc.CardBody([
            metric_toggle(),
            dcc.Graph(id='map', style={'height': '50vh', 'width': '20vw'}) 
        ]),
        className="mb-4 shadow",
        style={'display': 'flex', 'flex-direction': 'column', 'height': '60vh', 'min-height': '400px'}
    )
