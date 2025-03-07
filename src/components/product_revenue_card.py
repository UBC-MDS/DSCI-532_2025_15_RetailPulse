import dash_bootstrap_components as dbc
import dash_vega_components as dvc

def product_revenue_card():
    return dbc.Card(
        dbc.CardBody([
            dvc.Vega(id='revenue-by-product', spec={}, className="vega-chart")
        ], className="indv-graph-card-body"), 
        className="indv-graph-card",
    )