import dash_bootstrap_components as dbc
from dash import html

import dash_bootstrap_components as dbc
from dash import html

def footer():
    return dbc.Card(
        dbc.CardBody([
            # Top-aligned description
            html.P(
                "A real-time analytics tool providing insights into store operations.",
                className="text-left",
                style={"textAlign": "left", "color": "white", "marginBottom": "10px"}
            ),
            
            # List with bullet points
            html.Ul([
                html.Li(html.A("GitHub Repository", href="https://github.com/UBC-MDS/DSCI-532_2025_15_RetailPulse.git", 
                               target="_blank", style={"color": "white", "textDecoration": "underline"}), 
                        style={"color": "white", "marginBottom": "10px"}),

                html.Li("Creators: Dhruv, Farhan, Gilbert, & Jam",
                        style={"color": "white", "marginBottom": "10px"}),

                html.Li("Last Deployment: March 01, 2025",
                        style={"color": "white"})
            ], style={"textAlign": "left", "paddingLeft": "20px"})  # Indentation for bullets
        ]),
        className="mt-4 shadow",
        style={
            "backgroundColor": "#488a99",
            "border": "2px solid white", 
            "borderRadius": "10px",
            "padding": "10px"
        }
    )