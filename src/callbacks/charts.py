import pandas as pd
from dash import Input, Output
import plotly.express as px
from data.data import get_monthly_customer_retention, get_revenue_trends, get_country_sales, get_data, get_product_revenue
import altair as alt

df = get_data()
revenue_trends = get_revenue_trends()
monthly_retention = get_monthly_customer_retention(6)
country_sales = get_country_sales()
product_revenue = get_product_revenue()


def register_callbacks(app):

    @app.callback(
        Output('map', 'figure'),
        Input('toggle-metric', 'value'),
        Input('map', 'hoverData')
    )
    def create_map(metric, hoverData):
        fig = px.choropleth(
            country_sales,
            locations='iso_alpha',
            color=metric,
            hover_name='Country',
            title='🌍 Geographical Sales Distribution',
            color_continuous_scale=px.colors.sequential.Viridis,
            projection='mercator',
            custom_data=['Country', 'Revenue', 'Quantity']
        )

        # Resize map
        fig.update_layout(
            autosize=False,
            margin=dict(l=0, r=0, b=0, t=50, pad=4, autoexpand=True),
            width=700,
            height=400
        )


        fig.update_geos(lataxis_range=[-20, 90])

        # Custom hover template
        # Note the underscore
        fig.update_traces(
            hovertemplate="<b>%{customdata[0]}</b><br>Revenue: %{customdata[1]:,.2f}<br>Quantity: %{customdata[2]:,.0f}"
        )

        # Background colors
        fig.update_layout(
            paper_bgcolor='white',
            geo=dict(
                bgcolor='white',
                showframe=False,
                showcoastlines=True,
                showland=True,
                landcolor='gray'
            )
        )

        # Highlight selected country
        if hoverData:
            selected_country = hoverData['points'][0]['location']
            fig.update_traces(
                marker=dict(
                    line=dict(
                        color=['white' if c == selected_country else 'gray' for c in country_sales['iso_alpha']],
                        width=[2 if c == selected_country else 0 for c in country_sales['iso_alpha']]
                    )
                )
            )

        return fig


    @app.callback(
        Output('monthly-retention', 'figure'),
        Input('num-months', 'value')
    )
    def update_monthly_retention(num_months):
        filtered_retention = get_monthly_customer_retention(num_months)

        fig = px.line(
            filtered_retention, 
            x=filtered_retention['Month'].astype(str), 
            y='CustomerID',
            title=f'Returning Customers by Month (Last {num_months} Months)',
            labels={'CustomerID': 'Returning Customers', 'x': 'Month'}
        )

        fig.update_traces(mode='lines+markers', marker=dict(size=8, symbol='circle'))
        return fig

    @app.callback(
        Output('revenue-trends', 'spec'),
        Input('toggle-metric', 'value')
    )

    def create_revenue_trends(metric):
        fig = alt.Chart(revenue_trends, width='container', height='container').mark_line(point=True).encode(
            x=alt.X('InvoiceDate:T', title='Date', axis=alt.Axis(format='%b %Y')),  # Format dates
            y=alt.Y('Revenue:Q', title='Revenue ($)'),
            tooltip=['InvoiceDate', 'Revenue']
        ).properties(
            title='Monthly Revenue Trends',
            width="container",
            height="container"
        ).configure_axis(
            labelFontSize=16,
            titleFontSize=20
        ).configure_title(
            fontSize=20
        )
        
        return fig.to_dict()



    @app.callback(
        Output('revenue-by-product', 'spec'),
        Input('toggle-metric', 'value')
    )
    def create_revenue_by_product(metric):
        top_product_revenue = product_revenue.nlargest(10, 'Revenue')  # Ensure descending order
    
        fig = alt.Chart(top_product_revenue, width='container', height='container').mark_bar().encode(
            x=alt.X('Revenue:Q', title='Revenue ($)'),
            y=alt.Y('Description:N', sort='-x', title='Product'),  # Sort by Revenue in descending order
            tooltip=['Description', 'Revenue']
        ).configure_axis(
            labelFontSize=16,
            titleFontSize=20
        ).configure_title(
            fontSize=20
        ).properties(
            title='Revenue by Product'
        )
        
        return (fig.to_dict())