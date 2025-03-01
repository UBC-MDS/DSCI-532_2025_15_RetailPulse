import dash
import dash_bootstrap_components as dbc
from src.callbacks.charts import register_callbacks

from src.components.map_card import map_card
from src.components.revenue_trends_card import revenue_trends_card
from src.components.customer_retention_card import customer_retention_card
from src.components.product_revenue_card import product_revenue_card
from src.components.dhruv_card import dhruv_card
from src.components.footer import footer
from src.components.header import dashboard_title


# Initialize Dash app
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])
server = app.server

# Layout
app.layout = dbc.Container(fluid=True, children=[

    # Title
    dashboard_title(),

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
            dhruv_card()
        ], width=6)
    ], className="align-items-stretch"),

    footer()
])

# Register Callbacks
register_callbacks(app)

if __name__ == '__main__':
    app.run_server(debug=False, threaded=True)
