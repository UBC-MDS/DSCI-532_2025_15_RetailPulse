from dash import html
import dash_bootstrap_components as dbc
from components.header import dashboard_title
from components.widgets import month_slider
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
                    html.Div(category_dropdown(), style={'margin-bottom': '20px'}),
                    html.Div(country_dropdown(), style={'margin-bottom': '20px'}),
                    html.Div(month_slider(), style={'margin-bottom': '20px'}),
                    metric_toggle(),
                ],
                className=".widget-group"
            ),

            # Footer is bottom-aligned
            html.Div(
                footer(),
                style={
                    'margin-top': 'auto',
                }
            )
        ],
        className="sidebar-container"
    )
