import dash_bootstrap_components as dbc
from dash import dcc

def map_card():
    return dbc.Card(
        dbc.CardBody([
            dcc.Graph(id='map', style={'height': '100%', 'width': '15vw'}) 
        ]),
        className="map-graph"
    )
