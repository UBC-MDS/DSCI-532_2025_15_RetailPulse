import os
import sys
import pytest
import pandas as pd
import altair as alt
import plotly.graph_objects as go
from dash import Dash, dcc, html
from flask_caching import Cache

# Add the src directory to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from src.data.data import (
    get_monthly_customer_retention,
    get_revenue_quantity_trends,
    get_country_sales,
    get_data,
    get_product_revenue_quantity,
    get_monthly_sales_data,
    get_summary_metrics,
)

from src.callbacks.charts import register_callbacks
from src.callbacks.summary_metric_helper import summary_metrics


@pytest.fixture
def dash_app():
    """Fixture to create a Dash test application instance."""
    app = Dash()
    register_callbacks(app)
    return app


def test_update_summary_metrics():
    """Tests the update_summary_metrics function independently."""
    output = get_summary_metrics(6, ["USA"], ["Electronics"])
    assert "total_revenue" in output
    assert "total_orders" in output
    assert "total_customers" in output