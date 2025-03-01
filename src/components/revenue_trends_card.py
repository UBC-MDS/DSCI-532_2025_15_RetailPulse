import dash_bootstrap_components as dbc
from dash import dcc
import dash_vega_components as dvc

def revenue_trends_card():
    return dbc.Card(
        dbc.CardBody([
            dvc.Vega(id='revenue-trends', spec={}, style={'height': '100%', 'width': '100%', 'flex': '1'})
        ], style={'height': '100%', 'overflow': 'hidden'}),
        className="mb-4 shadow",
        style={'display': 'flex', 'flex-direction': 'column', 'height': '60vh', 'min-height': '400px'}
    )
