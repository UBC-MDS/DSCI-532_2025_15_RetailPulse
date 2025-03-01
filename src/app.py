import dash
import dash_bootstrap_components as dbc
import os
import sys
sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))
from callbacks.charts import register_callbacks

from components.map_card import map_card
from components.revenue_trends_card import revenue_trends_card
from components.customer_retention_card import customer_retention_card
from components.product_revenue_card import product_revenue_card
from components.dhruv_card import dhruv_card
from components.footer import footer
from components.header import dashboard_title
from components.summary_metrics import summary_metrics
from components.monthly_sales_card import monthly_sales_card

# Initialize Dash app
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])
server = app.server

# Layout
app.layout = dbc.Container(fluid=True, children=[

    # Title
    dashboard_title(),

    summary_metrics(),
    dbc.Row([
        dbc.Col(product_revenue_card(), width=12)
    ], className="mb-4"),  # Adds margin below the row

    dbc.Row([
        dbc.Col([
            revenue_trends_card(),
            customer_retention_card()
        ], width=6),

        # Right Column: Choropleth Map & Another Chart Stacked
        dbc.Col([
            map_card(),
            monthly_sales_card()
        ], width=6)
    ], className="align-items-stretch"),

    footer()
])

# Register Callbacks
register_callbacks(app)

if __name__ == '__main__':
    app.run_server(debug=False)
