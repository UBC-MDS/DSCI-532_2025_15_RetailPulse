import dash_bootstrap_components as dbc

def summary_metrics():
    return dbc.Card(
        dbc.CardBody(id="summary-metrics-container", children=[]),
        className="summary-container ",
    )
