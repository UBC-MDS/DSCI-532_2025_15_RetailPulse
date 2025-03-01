import dash_bootstrap_components as dbc
import dash_vega_components as dvc

from dash import dcc, html
from components.general import retention_slider

def revenue_trends_card():
    return dbc.Card(
        dbc.CardBody([
            html.Div(retention_slider(), style={'margin-top': 'auto', 'height': '10%'}),
            dvc.Vega(id='revenue-trends', spec={}, style={'height': '85%', 'width': '100%', 'flex': '1'})
        ], style={'height': '100%', 'overflow': 'hidden'}),
        className="mb-4 shadow",
        style={'display': 'flex', 'flex-direction': 'column', 'height': '60vh', 'min-height': '400px'}
    )
