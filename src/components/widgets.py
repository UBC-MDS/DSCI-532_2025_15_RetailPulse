from dash import dcc, html
import dash_bootstrap_components as dbc

from data.data import (
    get_month_options,
    get_category_options,
    get_country_options
)

month_options = get_month_options()
category_options = get_category_options()
country_options = get_country_options()

# Metric toggle radio buttons
def metric_toggle():
    return dbc.Card(
        dbc.CardBody([
            html.H5("Metric Toggle", className="card-title", style={"color": "white", "textAlign": "center"}),
            dcc.RadioItems(
                id='toggle-metric', 
                options=[
                    {'label': html.Span("Quantity", style={'marginRight': '15px', 'color': 'white'}), 'value': 'Quantity'},
                    {'label': html.Span("Revenue", style={'marginRight': '15px', 'color': 'white'}), 'value': 'Revenue'}
                ],
                value='Quantity',
                inline=True,
                className="text-center"
            )
        ]),
        className="indv-widget"
    )

# Monthly retention slider
def month_slider():
    return dbc.Card(
        dbc.CardBody([
            html.H5("View Data for Last N Months", className="card-title", style={"color": "white", "textAlign": "center"}),
            dcc.Slider(id='num-months', min=1, max=12, step=1, value=6, 
                       marks={i: {'label': str(i), 'style': {'color': 'white'}} for i in range(1, 13)})
        ]),
        className="indv-widget"
    )

# Category dropdown
def category_dropdown():
    return dbc.Card(
        dbc.CardBody([
            html.H5("Select Category", className="card-title", style={"color": "white", "textAlign": "center"}),
            dcc.Dropdown(
                id="category-dropdown",
                options=[{"label": category, "value": category} for category in category_options],  
                value=["All"], 
                clearable=False,
                multi = True,
                style={"color": "black"} 
            )
        ]),
        className="indv-widget"
    )

# Country dropdown
def country_dropdown():
    return dbc.Card(
        dbc.CardBody([
            html.H5("Select Country", className="card-title", style={"color": "white", "textAlign": "center"}),
            dcc.Dropdown(
                id="country-dropdown",
                options=[{"label": country, "value": country} for country in country_options],  # Corrected options
                value=["All"], 
                clearable=False,
                multi = True,
                style={"color": "black"}
            )
        ]),
        className="indv-widget"
    )