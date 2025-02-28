import pandas as pd
import plotly.express as px

# Load sales data
file_path = "./data/raw/online_retail.xlsx" 

df = pd.read_excel(file_path)
df['Revenue'] = df['Quantity'] * df['UnitPrice']
df['InvoiceDate'] = pd.to_datetime(df['InvoiceDate'])


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
    monthly_retention.rename(columns={'Month_current': 'Month'}, inplace=True)

    return monthly_retention