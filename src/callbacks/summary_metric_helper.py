import dash_html_components as html
import dash_bootstrap_components as dbc

def summary_metrics(total_revenue, total_orders, total_customers):
    return [
        dbc.Row(
            [
                dbc.Col(
                    dbc.Card(
                        dbc.CardBody(
                            dbc.Container(
                                [
                                    html.H5("Total Revenue", className="card-title text-center"),
                                    html.H4(f"${total_revenue:,.0f}", className="card-text text-center"),
                                ],
                                className="centered-card-body"
                            )
                        ),
                        className="summary-card summary-card-primary h-100"
                    ),
                    width=4
                ),

                dbc.Col(
                    dbc.Card(
                        dbc.CardBody(
                            dbc.Container(
                                [
                                    html.H5("Total Orders", className="card-title text-center"),
                                    html.H4(f"{total_orders:,}", className="card-text text-center"),
                                ],
                                className="centered-card-body"
                            )
                        ),
                        className="summary-card summary-card-success h-100"
                    ),
                    width=4
                ),

                dbc.Col(
                    dbc.Card(
                        dbc.CardBody(
                            dbc.Container(
                                [
                                    html.H5("Total Customers", className="card-title text-center"),
                                    html.H4(f"{total_customers:,}", className="card-text text-center"),
                                ],
                                className="centered-card-body"
                            )
                        ),
                        className="summary-card summary-card-info h-100"
                    ),
                    width=4
                ),
            ],
            justify="center",
            className="w-100"
        )
    ]