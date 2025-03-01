import dash_bootstrap_components as dbc
from dash import html


def dashboard_title():
    return dbc.Container(
        dbc.Row(
            dbc.Col(
                html.H1(
                    "Retail Pulse",
                    className="text-center",
                    style={
                        "padding": "2vh 0",
                        "fontSize": "3vw",  
                        "color": "white",
                        "textAlign": "center",
                        "backgroundColor": "#007BFF"
                    }
                ),
                width=12
            )
        ),
        fluid=True,
        className="header"
    )
