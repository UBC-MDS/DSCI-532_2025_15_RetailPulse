import dash_bootstrap_components as dbc
import dash_vega_components as dvc

def monthly_sales_card():
    return dbc.Card(
        dbc.CardBody([
            dvc.Vega(id='monthly-sales-bar-chart', spec={}, className="vega-chart")
        ], className="indv-graph-card-body"), 
        className="indv-graph-card"
    )
