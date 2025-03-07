import dash_html_components as html
import dash_bootstrap_components as dbc
from data.data import get_summary_metrics 

# Fetch summary statistics
metrics = get_summary_metrics()
total_revenue = metrics["total_revenue"]
total_orders = metrics["total_orders"]
total_customers = metrics["total_customers"]

def summary_metrics():
    return dbc.Card(
        dbc.CardBody(id="summary-metrics-container", children=[]),
        className="shadow",
        style={
            "backgroundColor": "#488a99", 
            "borderRadius": "10px", 
            "padding": "1px",
            "border": "2px solid white",
            "margin": "1px",
            "marginBottom": "10px", 
            "height": "15vh"

        }
    )
