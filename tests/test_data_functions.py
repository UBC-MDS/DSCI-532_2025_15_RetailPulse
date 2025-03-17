import sys
import os
import pandas as pd

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


data = {
    "InvoiceDate": ["2024-01-01", "2024-02-15", "2024-03-10", "2024-04-20"],
    "Quantity": [10, 5, 15, 20],
    "UnitPrice": [2.5, 5.0, 1.0, 3.0],
    "Country": ["USA", "Canada", "UK", "Germany"],
    "Category": ["Electronics", "Clothing", "Electronics", "Clothing"],
    "Description": ["Phone", "Shirt", "Laptop", "Jeans"],
    "CustomerID": [1, 2, 3, 4]
}

df = pd.DataFrame(data)
df['InvoiceDate'] = pd.to_datetime(df['InvoiceDate'])
df['Revenue'] = df['Quantity'] * df['UnitPrice']

def test_get_data():
    result = get_data()
    assert isinstance(result, pd.DataFrame)
    assert not result.empty
    assert "Revenue" in result.columns

def test_get_country_sales():
    result = get_country_sales(no_months=3, selected_country=["USA"], selected_category=["All"])
    assert isinstance(result, pd.DataFrame)
    assert "Revenue" in result.columns
    assert "Country" in result.columns

def test_get_revenue_quantity_trends():
    result = get_revenue_quantity_trends(no_months=3, selected_country=["All"], selected_category=["All"])
    assert isinstance(result, pd.DataFrame)
    assert "Revenue" in result.columns
    assert "Quantity" in result.columns

def test_get_monthly_customer_retention():
    result = get_monthly_customer_retention(no_months=3, selected_country=["All"], selected_category=["All"])
    assert isinstance(result, pd.DataFrame)
    assert "Count" in result.columns

def test_get_product_revenue_quantity():
    result = get_product_revenue_quantity(no_months=3, selected_country=["All"], selected_category=["All"])
    assert isinstance(result, pd.DataFrame)
    assert "Revenue" in result.columns
    assert "Description" in result.columns

def test_get_monthly_sales_data():
    result = get_monthly_sales_data(no_months=3, selected_country=["All"], selected_category=["All"])
    assert isinstance(result, pd.DataFrame)
    assert "Revenue" in result.columns
    assert "Quantity" in result.columns

def test_get_summary_metrics():
    result = get_summary_metrics(no_months=3, selected_country=["All"], selected_category=["All"])
    assert isinstance(result, dict)
    assert "total_revenue" in result
    assert "total_orders" in result
    assert "total_customers" in result