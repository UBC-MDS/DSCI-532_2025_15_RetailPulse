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
from components.footer import footer

from components.summary_metrics import summary_metrics
from components.monthly_sales_card import monthly_sales_card
from components.sidebar import sidebar

# Initialize Dash app
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP], title='Retail Pulse')
server = app.server


app.layout = dbc.Container(fluid=True, children=[

   
    dbc.Row([
        # Sidebar Column (Left on large screens, Top on extra-small screens)
        dbc.Col(sidebar(), lg=3, md=3, sm=12, xs=12, className="sidebar-column",
                style={'min-height': '100vh'}), 

        # Main Content Column
        dbc.Col([
            # Summary Metrics
            dbc.Row([
                dbc.Col(summary_metrics(), width=12, style={
                    'display': 'flex', 
                    'flex-direction': 'column', 
                    'height': '100%', 
                    'overflow': 'hidden',
                })
            ]),

            # Map Card
            dbc.Row([
                dbc.Col(map_card(), width=12)
            ]),

            dbc.Row([
                dbc.Col(revenue_trends_card(), lg=6, md=6, sm=6, xs=12, className="graph-card"),
                dbc.Col(customer_retention_card(), lg=6, md=6, sm=6, xs=12, className="graph-card"),
                dbc.Col(product_revenue_card(), lg=6, md=6, sm=6, xs=12, className="graph-card"),
                dbc.Col(monthly_sales_card(), lg=6, md=6, sm=6, xs=12, className="graph-card"),
            ], className="gx-3 gy-3") 
        ], lg=9, md=9, sm=12, xs=12, style={'padding-top': '10px'}) 
    ], className="align-items-stretch"),
])


# Register Callbacks
register_callbacks(app)

if __name__ == '__main__':
    app.run(debug=False)
