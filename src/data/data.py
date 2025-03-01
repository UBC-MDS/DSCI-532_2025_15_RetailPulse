import pandas as pd
import plotly.express as px

# Load sales data
file_path = "data/processed/sample.csv" 

df = pd.read_csv(file_path)
df['Revenue'] = df['Quantity'] * df['UnitPrice']
df['InvoiceDate'] = pd.to_datetime(df['InvoiceDate'])

# Extract Year and Month Name
df['Month_Label'] = df['InvoiceDate'].dt.strftime('%Y - %B') 
df['Month_Value'] = df['InvoiceDate'].dt.strftime('%Y-%m')  # Format: "YYYY-MM" (for filtering)

# Get unique month values for dropdown (sorted in descending order)
month_options = (
    df[['Month_Label', 'Month_Value']]
    .drop_duplicates()
    .sort_values('Month_Value', ascending=False)  # Most recent first
    .to_dict(orient="records")
)

def get_data():
    return df

def get_country_sales():
    # Aggregate by country
    country_sales = df.groupby('Country', as_index=False).agg({'Revenue': 'sum', 'Quantity': 'sum'})
    # Load country coordinates for mapping
    geo_data = px.data.gapminder()[['country', 'iso_alpha']].drop_duplicates()
    all_countries = pd.DataFrame({'Country': geo_data['country'], 'iso_alpha': geo_data['iso_alpha']})
    country_sales = country_sales.merge(all_countries, on='Country', how='left').fillna({'Revenue': 0, 'Quantity': 0})
    country_sales = country_sales[country_sales['Country'] != 'Antarctica']

    return country_sales

def get_revenue_trends():
    return df.resample('M', on='InvoiceDate').agg({'Revenue': 'sum'}).reset_index()

def get_monthly_customer_retention(no_months):
        
    # Customer Retention Metrics
    latest_date = df['InvoiceDate'].max()
    n_months_ago = latest_date - pd.DateOffset(months=no_months)
    df_last_n_months = df[df['InvoiceDate'] >= n_months_ago].copy()

    df_last_n_months['Month'] = df_last_n_months['InvoiceDate'].dt.to_period('M')
    customer_months = df_last_n_months.groupby(['CustomerID', 'Month']).size().reset_index(name='Purchases')

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

def get_product_revenue():
    df['Revenue'] = df['Quantity'] * df['UnitPrice']
    # Group by product and sum the revenue
    df_grouped = df.groupby('Description', as_index=False)['Revenue'].sum()
    df_grouped = df_grouped.sort_values(by='Revenue', ascending=False)
    return df_grouped

def get_summary_metrics():
    """Returns total revenue, total orders, and unique customers"""
    total_revenue = df["Revenue"].sum()
    total_orders = df["Quantity"].sum()
    total_customers = df["CustomerID"].nunique()  # Count unique customers

    return {
        "total_revenue": total_revenue,
        "total_orders": total_orders,
        "total_customers": total_customers
    }
  
def get_monthly_sales_data(selected_month):
    """Returns the quantity sold per category for a given month."""
    df['InvoiceDate'] = pd.to_datetime(df['InvoiceDate'])
    
    df['Month'] = df['InvoiceDate'].dt.strftime('%Y-%m') 
    filtered_df = df[df['Month'] == selected_month]

    monthly_sales = filtered_df.groupby('Category', as_index=False)['Quantity'].sum()
    monthly_sales = monthly_sales.sort_values(by="Quantity", ascending=False)
    
    return monthly_sales

def get_month_options():
    """Returns available months for the dropdown."""
    return month_options
