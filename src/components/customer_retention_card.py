import dash_bootstrap_components as dbc
import dash_vega_components as dvc

from components.widgets import retention_slider

def customer_retention_card():
    return dbc.Card(
        dbc.CardBody([
            dvc.Vega(id='monthly-retention', spec={}, style={'height': '100%', 'width': '100%', 'flex': '1'})
        ], style={'display': 'flex', 'flex-direction': 'column', 'height': '100%', 'overflow': 'hidden'}), 
        className="indv-graph"
    )
