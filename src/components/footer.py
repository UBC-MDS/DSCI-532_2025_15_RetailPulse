import dash_bootstrap_components as dbc
from dash import html

def footer():
    return dbc.Card(
        dbc.CardBody([
            # Top-aligned description
            html.P(
                "A real-time analytics tool providing insights into store operations.",
                className="footer-text"
            ),
            
            # List with bullet points
            html.Ul([
                html.Li(html.A("GitHub Repository", 
                               href="https://github.com/UBC-MDS/DSCI-532_2025_15_RetailPulse.git",
                               target="_blank", 
                               className="footer-link"), 
                        className="footer-list-item"),

                html.Li("Creators: Dhruv, Farhan, Gilbert, & Jam",
                        className="footer-list-item"),

                html.Li("Last Deployment: March 01, 2025",
                        style={"color": "white"}) 
            ], className="footer-list")
        ]),
        className="footer shadow"
    )
