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


def get_data():
    return df

def filter_last_n_months(n_months):
    latest_date = df['InvoiceDate'].max()
    n_months_ago = latest_date - pd.DateOffset(months=n_months)
    return df[df['InvoiceDate'] >= n_months_ago].copy()


def get_country_sales(no_months=6, selected_country='All', selected_category="All"):
    my_df = filter_last_n_months(no_months)
    if selected_category != "All":
        my_df = my_df[my_df["Category"] == selected_category]

    if selected_country != "All":
        my_df = my_df[my_df["Country"] == selected_country]
    
    # Aggregate by country
    country_sales = my_df.groupby('Country', as_index=False).agg({'Revenue': 'sum', 'Quantity': 'sum'})
    
    # Load country coordinates for mapping
    geo_data = px.data.gapminder()[['country', 'iso_alpha']].drop_duplicates()
    all_countries = pd.DataFrame({'Country': geo_data['country'], 'iso_alpha': geo_data['iso_alpha']})
    country_sales = country_sales.merge(all_countries, on='Country', how='left').fillna({'Revenue': 0, 'Quantity': 0})
    country_sales = country_sales[country_sales['Country'] != 'Antarctica']

    return country_sales

def get_revenue_trends(no_months=6, selected_country="All", selected_category="All"):
    my_df = filter_last_n_months(no_months)

    if selected_category != "All":
        my_df = my_df[my_df["Category"] == selected_category]

    if selected_country != "All":
        my_df = my_df[my_df["Country"] == selected_country]

    my_df['InvoiceDate'] = pd.to_datetime(my_df['InvoiceDate']) 
    my_df['Month'] = my_df['InvoiceDate'].dt.to_period('M').astype(str)
    monthly_revenue = my_df.groupby('Month', as_index=False)['Revenue'].sum()
    return monthly_revenue

def get_monthly_customer_retention(no_months=6, selected_country="All", selected_category="All"):
    my_df = filter_last_n_months(no_months)

    if selected_category != "All":
        my_df = my_df[my_df["Category"] == selected_category]

    if selected_country != "All":
        my_df = my_df[my_df["Country"] == selected_country]

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

def get_product_revenue(no_months=6, selected_country="All", selected_category="All"):
    my_df = filter_last_n_months(no_months)

    if selected_category != "All":
        my_df = my_df[my_df["Category"] == selected_category]

    if selected_country != "All":
        my_df = my_df[my_df["Country"] == selected_country]

    my_df['Revenue'] = my_df['Quantity'] * my_df['UnitPrice']
    # Group by product and sum the revenue
    df_grouped = my_df.groupby('Description', as_index=False)['Revenue'].sum()
    df_grouped = df_grouped.sort_values(by='Revenue', ascending=False)
    return df_grouped

def get_summary_metrics(no_months=6, selected_country="All", selected_category="All"):
    """Returns total revenue, total orders, and unique customers"""

    my_df = filter_last_n_months(no_months)

    if selected_category != "All":
        my_df = my_df[my_df["Category"] == selected_category]

    if selected_country != "All":
        my_df = my_df[my_df["Country"] == selected_country]

    total_revenue = my_df["Revenue"].sum()
    total_orders = my_df["Quantity"].sum()
    total_customers = my_df["CustomerID"].nunique()  # Count unique customers

    return {
        "total_revenue": total_revenue,
        "total_orders": total_orders,
        "total_customers": total_customers
    }
  
def get_monthly_sales_data(no_months=6, selected_country="All", selected_category="All"):
    """Returns the quantity sold per category for a given month."""
    my_df = filter_last_n_months(no_months)

    if selected_category != "All":
        my_df = my_df[my_df["Category"] == selected_category]

    if selected_country != "All":
        my_df = my_df[my_df["Country"] == selected_country]

    my_df['InvoiceDate'] = pd.to_datetime(my_df['InvoiceDate'])
    my_df['Month'] = my_df['InvoiceDate'].dt.strftime('%Y-%m') 

    monthly_sales = my_df.groupby('Category', as_index=False)['Quantity'].sum()
    monthly_sales = monthly_sales.sort_values(by="Quantity", ascending=False)
    
    return monthly_sales


def get_month_options():
    """Returns available months for the dropdown."""
    month_options = (
        df[['Month_Label', 'Month_Value']]
        .drop_duplicates()
        .sort_values('Month_Value', ascending=False)  # Most recent first
        .to_dict(orient="records")
    )
    
    return month_options


def get_category_options():
    """Fetch unique categories from the dataset and add 'All'."""
    categories = df["Category"].unique().tolist()
    categories.sort()  
    return ["All"] + categories 



def get_country_options():
    """Fetch unique countries from the dataset and add 'All'."""
    countries = df["Country"].unique().tolist()
    countries.sort()  
    return ["All"] + countries 
