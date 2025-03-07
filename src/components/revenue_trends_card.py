import dash_bootstrap_components as dbc
import dash_vega_components as dvc

def revenue_trends_card():
    return dbc.Card(
        dbc.CardBody([
            dvc.Vega(id='revenue-trends', spec={}, className="vega-chart")
        ], className="indv-graph-card-body"), 
        className="indv-graph-card"
    )
