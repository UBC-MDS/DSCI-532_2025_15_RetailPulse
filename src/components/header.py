import dash_bootstrap_components as dbc
from dash import html


def dashboard_title():
    return dbc.Card(
        dbc.CardBody([
            html.H1("Retail Pulse", className="dashboard-title-text")
        ]), 
        className="dashboard-title shadow"
    )