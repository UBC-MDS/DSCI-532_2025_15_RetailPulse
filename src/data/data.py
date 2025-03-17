import pandas as pd
import plotly.express as px
from flask_caching import Cache
from flask import Flask

# Initialize a Flask app (required for Flask-Caching)
flask_app = Flask(__name__)
cache = Cache(flask_app, config={'CACHE_TYPE': 'simple', 'CACHE_DEFAULT_TIMEOUT': 300})

# Load sales data
file_path = "data/processed/processed_parquet.parquet" 

@cache.memoize()
def get_data():
    """Loads dataset and caches it to avoid reloading"""
    df = pd.read_parquet(file_path, engine='pyarrow')
    df['Revenue'] = df['Quantity'] * df['UnitPrice']
    df['InvoiceDate'] = pd.to_datetime(df['InvoiceDate'])
    df['Month_Label'] = df['InvoiceDate'].dt.strftime('%Y - %B')
    df['Month_Value'] = df['InvoiceDate'].dt.strftime('%Y-%m')
    return df

@cache.memoize()
def filter_last_n_months(n_months):
    """
    Filters the dataset to include only the last `n_months` based on the `InvoiceDate` column.
    
    Args:
        n_months (int): Number of months to filter.
    
    Returns:
        DataFrame: Filtered dataset containing only the last `n_months` of data.
    """
    df = get_data()
    latest_date = df['InvoiceDate'].max()
    n_months_ago = latest_date - pd.DateOffset(months=n_months)
    return df[df['InvoiceDate'] >= n_months_ago].copy()


def get_country_sales(no_months=6, selected_country=['All'], selected_category=["All"]):
    """
    Computes total revenue and quantity sold per country within the 
    specified period and category filters.
    
    Args:
        no_months (int, optional): Number of months to filter. Defaults to 6.
        selected_country (list, optional): List of selected countries. Defaults to ['All'].
        selected_category (list, optional): List of selected categories. Defaults to ["All"].
    
    Returns:
        DataFrame: Aggregated country sales data including revenue, quantity, and country ISO codes.
    """
    my_df = filter_last_n_months(no_months)
    if selected_category and "All" not in selected_category:
        my_df = my_df[my_df["Category"].isin(selected_category)]

    if selected_country and "All" not in selected_country:
        my_df = my_df[my_df["Country"].isin(selected_country)]

    # Aggregate by country
    country_sales = my_df.groupby('Country', as_index=False).agg({'Revenue': 'sum', 'Quantity': 'sum'})
    
    # Load country coordinates for mapping
    geo_data = px.data.gapminder()[['country', 'iso_alpha']].drop_duplicates()
    all_countries = pd.DataFrame({'Country': geo_data['country'], 'iso_alpha': geo_data['iso_alpha']})
    country_sales = country_sales.merge(all_countries, on='Country', how='left').fillna({'Revenue': 0, 'Quantity': 0})
    country_sales = country_sales[country_sales['Country'] != 'Antarctica']

    return country_sales


def get_revenue_quantity_trends(no_months=6, selected_country=["All"], selected_category=["All"]):
    """
    Computes monthly revenue and quantity trends based on selected filters.
    
    Args:
        no_months (int, optional): Number of months to filter. Defaults to 6.
        selected_country (list, optional): List of selected countries. Defaults to ["All"].
        selected_category (list, optional): List of selected categories. Defaults to ["All"].
    
    Returns:
        DataFrame: Monthly revenue and quantity trends.
    """
    my_df = filter_last_n_months(no_months)

    if selected_category and "All" not in selected_category:
        my_df = my_df[my_df["Category"].isin(selected_category)]

    if selected_country and "All" not in selected_country:
        my_df = my_df[my_df["Country"].isin(selected_country)]

    my_df['InvoiceDate'] = pd.to_datetime(my_df['InvoiceDate']) 

    my_df['Month'] = my_df['InvoiceDate'].dt.strftime('%Y-%m') 

    my_df['Revenue'] = my_df['Quantity'] * my_df['UnitPrice']  
    
    monthly_revenue = my_df.groupby('Month')['Revenue', 'Quantity'].sum().reset_index()

    # print(monthly_revenue)
    return monthly_revenue


def get_monthly_customer_retention(no_months=6, selected_country=["All"], selected_category=["All"]):
    """
    Calculates monthly customer retention based on repeat purchases.
    
    Args:
        no_months (int, optional): Number of months to filter. Defaults to 6.
        selected_country (list, optional): List of selected countries. Defaults to ["All"].
        selected_category (list, optional): List of selected categories. Defaults to ["All"].
    
    Returns:
        DataFrame: Customer retention per month.
    """
    my_df = filter_last_n_months(no_months)


    if selected_category and "All" not in selected_category:
        my_df = my_df[my_df["Category"].isin(selected_category)]

    if selected_country and "All" not in selected_country:
        my_df = my_df[my_df["Country"].isin(selected_country)]

    my_df['Month'] = my_df['InvoiceDate'].dt.to_period('M')
    customer_months = my_df.groupby(['CustomerID', 'Month']).size().reset_index(name='Purchases')

    # Calculate previous month's purchases using shift
    customer_months['PreviousMonth'] = customer_months.groupby('CustomerID')['Month'].shift(1)

    # Merge to find returning customers
    returning_customers = customer_months.merge(
        customer_months, 
        left_on=['CustomerID', 'Month'], 
        right_on=['CustomerID', 'PreviousMonth'],
        suffixes=('_current', '_previous')
    )
    
    monthly_retention = returning_customers.groupby('Month_current').agg({'CustomerID': 'nunique'}).reset_index()
    monthly_retention.rename(columns={'Month_current': 'Month', 'CustomerID': 'Count'}, inplace=True)

    return monthly_retention


def get_product_revenue_quantity(no_months=6, selected_country=["All"], selected_category=["All"]):
    """
    Computes total revenue and quantity sold per product description 
    within a specified period and filters.
    
    Args:
        no_months (int, optional): Number of months to filter. Defaults to 6.
        selected_country (list, optional): List of selected countries. Defaults to ["All"].
        selected_category (list, optional): List of selected categories. Defaults to ["All"].
    
    Returns:
        DataFrame: Aggregated revenue and quantity sold per product description, sorted by revenue.
    """

    my_df = filter_last_n_months(no_months)

    if selected_category and "All" not in selected_category:
        my_df = my_df[my_df["Category"].isin(selected_category)]

    if selected_country and "All" not in selected_country:
        my_df = my_df[my_df["Country"].isin(selected_country)]

    my_df['Revenue'] = my_df['Quantity'] * my_df['UnitPrice']
    # Group by product and sum the revenue
    df_grouped = my_df.groupby('Description', as_index=False).agg({'Revenue': 'sum', 'Quantity': 'sum'})
    df_grouped = df_grouped.sort_values(by='Revenue', ascending=False)
    return df_grouped


def get_monthly_sales_data(no_months=6, selected_country=["All"], selected_category=["All"]):
    """
    Computes the total revenue and quantity sold per product category within the given timeframe.
    
    Args:
        no_months (int, optional): Number of months to filter. Defaults to 6.
        selected_country (list, optional): List of selected countries. Defaults to ["All"].
        selected_category (list, optional): List of selected categories. Defaults to ["All"].
    
    Returns:
        DataFrame: Monthly sales data aggregated by product category, sorted by quantity sold.
    """
    my_df = filter_last_n_months(no_months)

    if selected_category and "All" not in selected_category:
        my_df = my_df[my_df["Category"].isin(selected_category)]

    if selected_country and "All" not in selected_country:
        my_df = my_df[my_df["Country"].isin(selected_country)]

    # Compute revenue
    my_df['Revenue'] = my_df['Quantity'] * my_df['UnitPrice']  # Added Revenue column

    my_df['InvoiceDate'] = pd.to_datetime(my_df['InvoiceDate'])
    my_df['Month'] = my_df['InvoiceDate'].dt.strftime('%Y-%m') 

    # Aggregate by Category: Sum both Quantity and Revenue
    monthly_sales = my_df.groupby('Category', as_index=False)['Revenue', 'Quantity'].sum()
    monthly_sales = monthly_sales.sort_values(by="Quantity", ascending=False)
    
    return monthly_sales
    

def get_summary_metrics(no_months=6, selected_country=["All"], selected_category=["All"]):
    """
    Computes summary metrics including total revenue, total orders, and unique customers 
    within a specified period and filters.
    
    Args:
        no_months (int, optional): Number of months to filter. Defaults to 6.
        selected_country (list, optional): List of selected countries. Defaults to ["All"].
        selected_category (list, optional): List of selected categories. Defaults to ["All"].
    
    Returns:
        dict: Summary metrics including total revenue, total orders, and unique customers.
    """

    my_df = filter_last_n_months(no_months)

    if selected_category and "All" not in selected_category:
        my_df = my_df[my_df["Category"].isin(selected_category)]

    if selected_country and "All" not in selected_country:
        my_df = my_df[my_df["Country"].isin(selected_country)]

    total_revenue = my_df["Revenue"].sum()
    total_orders = my_df["Quantity"].sum()
    total_customers = my_df["CustomerID"].nunique() 

    return {
        "total_revenue": total_revenue,
        "total_orders": total_orders,
        "total_customers": total_customers
    }

@cache.memoize()
def get_month_options():
    """
    Returns 
        list: available months for the dropdown.
    """
    df = get_data()
    month_options = (
        df[['Month_Label', 'Month_Value']]
        .drop_duplicates()
        .sort_values('Month_Value', ascending=False)  # Most recent first
        .to_dict(orient="records")
    )
    
    return month_options

@cache.memoize()
def get_category_options():
    """
    Fetches unique product categories from the dataset and includes 'All' as an option.
    
    Returns:
        list: List of unique product categories with 'All' included.
    """
    df = get_data() 
    categories = df["Category"].unique().tolist()
    categories.sort()  
    return ["All"] + categories 

@cache.memoize()
def get_country_options():
    """
    Fetches unique countries from the dataset and includes 'All' as an option.
    
    Returns:
        list: List of unique countries with 'All' included.
    """
    df = get_data()
    countries = df["Country"].unique().tolist()
    countries.sort()  
    return ["All"] + countries 
