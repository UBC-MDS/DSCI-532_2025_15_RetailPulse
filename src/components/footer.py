import dash_bootstrap_components as dbc
from dash import html

def footer():
    return dbc.Card(
        dbc.CardBody([
            html.P(
                "RetailPulse - A real-time retail analytics tool providing insights into store operations.",
                className="text-center",
                style={"fontSize": "1.5vw", "color": "white", "marginBottom": "1px"}
            ),
            dbc.Row([
                dbc.Col(
                    html.P([
                        html.A("GitHub Repository", href="https://github.com/UBC-MDS/DSCI-532_2025_15_RetailPulse.git", target="_blank",
                               style={"color": "white", "textDecoration": "underline"})
                    ], style={"textAlign": "left"}), 
                    width=4
                ),
                dbc.Col(
                    html.P(
                        "Developed by: Dhruv, Farhan, Gilbert, & Jam",
                        style={"textAlign": "center", "color": "white"}
                    ),
                    width=4
                ),
                dbc.Col(    
                    html.P("Last Deployment: March 01, 2025",
                           style={"textAlign": "right", "color": "white"}),
                    width=4            
                )
            ])
        ]),
        className="mt-4 shadow",
        style={
            "backgroundColor": "#007BFF",
            "border": "2px solid white", 
            "borderRadius": "10px"
        }
    )
