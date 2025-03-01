import dash_html_components as html
import dash_bootstrap_components as dbc
from data.data import get_summary_metrics 

# Fetch summary statistics
metrics = get_summary_metrics()
total_revenue = metrics["total_revenue"]
total_orders = metrics["total_orders"]
total_customers = metrics["total_customers"]

def summary_metrics():
    return dbc.Row([
        dbc.Col(dbc.Card([
            dbc.CardBody([
                html.H4("Total Revenue", className="card-title"),
                html.H2(f"${total_revenue:,.0f}", className="card-text"),
            ])
        ], color="primary", inverse=True), width=4),

        dbc.Col(dbc.Card([
            dbc.CardBody([
                html.H4("Total Orders", className="card-title"),
                html.H2(f"{total_orders:,}", className="card-text"),
            ])
        ], color="success", inverse=True), width=4),

        dbc.Col(dbc.Card([
            dbc.CardBody([
                html.H4("Total Customers", className="card-title"),
                html.H2(f"{total_customers:,}", className="card-text"),
            ])
        ], color="info", inverse=True), width=4),
    ], className="mb-4")  # Adds space below metrics
