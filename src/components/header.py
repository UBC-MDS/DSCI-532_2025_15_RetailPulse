import dash_bootstrap_components as dbc
from dash import html


def dashboard_title():
    return dbc.Card(
        dbc.CardBody([
            html.H1(
                "Retail Pulse",
                className="text-center",
                style={
                    "padding": "2vh 0",
                    "fontSize": "3vw",  
                    "color": "white",
                    "textAlign": "center"
                }
            )
        ]), 
        className="mb-4 shadow",
        style={
            "backgroundColor": "#007BFF",
            "border": "2px solid white", 
            "borderRadius": "10px"      
        }
    )
