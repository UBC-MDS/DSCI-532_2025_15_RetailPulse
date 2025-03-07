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
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])
server = app.server


app.layout = dbc.Container(fluid=True, children=[

    dbc.Row([
        dbc.Col(sidebar(), width=3), 

        dbc.Col([
            dbc.Row([
                dbc.Col(summary_metrics(), width=12, style={
                    'display': 'flex', 
                    'flex-direction': 
                    'column', 'height': '100%', 
                    'overflow': 'hidden',
                    })
            ]),
            dbc.Row([
                dbc.Col(map_card(), width=12)
            ]),

            dbc.Row([
                dbc.Col([
                    dbc.Row([
                        dbc.Col(revenue_trends_card(), width=6),
                        dbc.Col(customer_retention_card(), width=6)
                    ]),

                    dbc.Row([
                        dbc.Col(product_revenue_card(), width=6),
                        dbc.Col(monthly_sales_card(), width=6)
                    ])
                ], width=12)
            ])
        ], width=9, style={'padding-top': '10px'}) 
    ], className="align-items-stretch"),
])


# Register Callbacks
register_callbacks(app)

if __name__ == '__main__':
    app.run_server(debug=False)
