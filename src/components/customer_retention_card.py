import dash_bootstrap_components as dbc
from dash import dcc

from src.components.general import retention_slider

def customer_retention_card():
    return dbc.Card(
        dbc.CardBody([
            dcc.Graph(id='monthly-retention', style={'height': '100%', 'width': '100%'}),
            retention_slider()
        ], style={'display': 'flex', 'flex-direction': 'column', 'height': '100%', 'overflow': 'hidden'}), 
        className="shadow",
        style={'display': 'flex', 'flex-direction': 'column', 'height': '48vh', 'min-height': '400px'}
    )
