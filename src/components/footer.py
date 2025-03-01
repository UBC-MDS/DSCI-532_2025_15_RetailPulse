import dash_bootstrap_components as dbc
from dash import html

def footer():
    return dbc.Container(
        dbc.Row(
            dbc.Col(
                html.P([
                    "© 2025 RetailPulse Dashboard | Built with Dash & Plotly",
                    html.Br(),
                    "Developed by: Dhruv, Farhan, Gilbert, & Jam"
                ],
                className="text-center",
                style={
                    "padding": "5px",
                    "fontSize": "1 vw",
                    "color": "white",
                    "textAlign": "center",
                    "backgroundColor": "#007BFF"
                }),
                width=12
            )
        ),
        fluid=True,
        className="footer"
    )