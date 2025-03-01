import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
from data.data import get_month_options 


month_options = get_month_options()

def monthly_sales_card():
    return dbc.Card(
        dbc.CardBody([
            html.Div(
                dcc.Dropdown(
                    id="month-dropdown",
                    options=[{"label": m["Month_Label"], "value": m["Month_Value"]} for m in month_options],
                    value=month_options[0]["Month_Value"],  # Default to most recent month
                    clearable=False
                ), 
                style={'margin-bottom': '10px'}
            ),

            # Bar chart below
            dcc.Graph(id="monthly-sales-bar-chart", 
                      figure={},  
                      style={'height': '100%', 'width': '100%', 'flex': '1'}),  
        ], 
        style={'display': 'flex', 'flex-direction': 'column', 'height': '100%', 'overflow': 'hidden'}), 
        
        className="mb-4 shadow",
        style={'display': 'flex', 'flex-direction': 'column', 'height': '60vh', 'min-height': '400px'}
    )
