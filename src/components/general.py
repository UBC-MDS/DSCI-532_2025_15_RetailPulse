from dash import dcc, html
import dash_bootstrap_components as dbc

# Sales dashboard title
def dashboard_title():
    return html.H1("Retail Pulsess", className="text-center text-primary")

# Metric toggle radio buttons
def metric_toggle():
    return dbc.Row([
        dbc.Col(dcc.RadioItems(
            id='toggle-metric', 
            options=[
                {'label': 'Quantity', 'value': 'Quantity'},
                {'label': 'Revenue', 'value': 'Revenue'}
            ],
            value='Quantity',
            inline=True,
            className="text-center"
        ), width=6),
    ], justify="center", className="m-2")

# Monthly retention slider
def retention_slider():
    return dbc.Col([
            html.Label("# months:"),
            dcc.Slider(id='num-months', min=1, max=12, step=1, value=6, 
                       marks={i: str(i) for i in range(1, 13)})
      
    ], className="m-1")
