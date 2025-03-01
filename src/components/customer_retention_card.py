import dash_bootstrap_components as dbc
from dash import dcc, html

from components.general import retention_slider
import dash_vega_components as dvc

def customer_retention_card():
    return dbc.Card(
        dbc.CardBody([
            dvc.Vega(id='monthly-retention', spec={}, style={'height': '100%', 'width': '100%', 'flex': '1'}),
            html.Div(retention_slider(), style={'margin-top': 'auto', 'height': '15%'})
        ], style={'display': 'flex', 'flex-direction': 'column', 'height': '100%', 'overflow': 'hidden'}), 
        className="mb-4 shadow",
        style={'display': 'flex', 'flex-direction': 'column', 'height': '60vh', 'min-height': '400px'}
    )
