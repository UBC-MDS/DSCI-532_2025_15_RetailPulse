from dash import Dash, dash_table, dcc, callback, Input, Output, html
import dash_bootstrap_components as dbc
import dash_vega_components as dvc
from components.header import dashboard_title
from components.widgets import retention_slider
from components.widgets import category_dropdown
from components.widgets import country_dropdown
from components.widgets import metric_toggle
from components.footer import footer


def sidebar():
    return dbc.Col(
        [
            # Top-aligned title
            dashboard_title(),
            html.Br(),
            
            # Middle section: Widgets are wrapped in a flex container for vertical centering
            html.Div(
                [
                    html.Div(retention_slider(), style={'margin-bottom': '20px'}),
                    html.Div(category_dropdown(), style={'margin-bottom': '20px'}),
                    html.Div(country_dropdown(), style={'margin-bottom': '20px'}),
                    metric_toggle(),
                ],
                className=".widget-group"
            ),

            # Footer is bottom-aligned
            html.Div(
                footer(),
                style={
                    'margin-top': 'auto',  # Pushes footer to the bottom
                }
            )
        ],
        style={
            'background-color': '#488a99',
            'margin': 2,
            'padding': 2,
            'margin-top': '10px',
            "border-radius": "10px",
            'height': '150vh',
            'display': 'flex',
            'flex-direction': 'column',
        }
    )
