import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
from data.data import get_month_options 
import dash_vega_components as dvc

month_options = get_month_options()

def monthly_sales_card():
    return dbc.Card(
        dbc.CardBody([

            # Bar chart below
            dvc.Vega(id='monthly-sales-bar-chart', spec={}, style={'height': '100%', 'width': '100%', 'flex': '1'})
            
        ], 
        style={'display': 'flex', 'flex-direction': 'column', 'height': '100%', 'overflow': 'hidden'}), 
        
        className="mb-4 shadow",
        style={'display': 'flex', 'flex-direction': 'column', 'height': '30vh', 'min-height': '400px'}
    )
