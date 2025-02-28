import dash
import dash_bootstrap_components as dbc
from dash import dcc, html
from components.general import dashboard_title, metric_toggle, retention_slider
from callbacks.charts import register_callbacks

from components.map_card import map_card
from components.revenue_trends_card import revenue_trends_card
from components.customer_retention_card import customer_retention_card
from components.product_revenue_card import product_revenue_card


# Initialize Dash app
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

# Layout
app.layout = dbc.Container(fluid=True, children=[

    # Title
    dashboard_title(),

    # Row for Side-by-Side Charts
    dbc.Row([
        # Map Card
        dbc.Col(map_card(), width=6),

        # Product Revenue Card
        dbc.Col(product_revenue_card(), width=6)

    ], className="align-items-stretch"),  # Forces equal height for both cards

    # Row for Side-by-Side Charts
    dbc.Row([
        # Revenue Trends Card
        dbc.Col(revenue_trends_card(), width=6),

        # Customer Retention Card
        dbc.Col(customer_retention_card(), width=6)

    ], className="align-items-stretch")  # Forces equal height for both cards
])

# Register Callbacks
register_callbacks(app)

if __name__ == '__main__':
    app.run_server(debug=True, threaded=True)
