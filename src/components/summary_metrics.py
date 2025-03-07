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
        dbc.CardBody([
            dbc.Row(
                [
                    dbc.Col(
                        dbc.Card(
                            dbc.CardBody([
                                html.H5("Total Revenue", className="card-title text-center"),
                                html.H4(f"${total_revenue:,.0f}", className="card-text text-center"),
                            ]),
                            color="primary", inverse=True, className="shadow",
                            style={"margin": "1px", "padding": "2px", "height": "11vh"}  # Adjusted margins and padding
                        ), width=4
                    ),

                    dbc.Col(
                        dbc.Card(
                            dbc.CardBody([
                                html.H5("Total Orders", className="card-title text-center"),
                                html.H4(f"{total_orders:,}", className="card-text text-center"),
                            ]),
                            color="success", inverse=True, className="shadow",
                            style={"margin": "1px", "padding": "2px", "height": "11vh"}  # Adjusted margins and padding
                        ), width=4
                    ),

                    dbc.Col(
                        dbc.Card(
                            dbc.CardBody([
                                html.H5("Total Customers", className="card-title text-center"),
                                html.H4(f"{total_customers:,}", className="card-text text-center"),
                            ]),
                            color="info", inverse=True, className="shadow",
                            style={"margin": "1px", "padding": "2px", "height": "11vh"}  # Adjusted margins and padding
                        ), width=4
                    ),
                ],
                justify="center",
                
            )
        ]),
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
