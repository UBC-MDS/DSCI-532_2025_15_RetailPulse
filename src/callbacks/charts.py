import pandas as pd
from dash import Input, Output
import plotly.express as px
from data.data import get_monthly_customer_retention, get_revenue_trends, get_country_sales, get_data


df = get_data()
revenue_trends = get_revenue_trends()
monthly_retention = get_monthly_customer_retention(6)
country_sales = get_country_sales()


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
            title='Geographical Sales Distribution',
            color_continuous_scale=px.colors.sequential.Viridis,
            projection='mercator',
            custom_data=['Country', 'Revenue', 'Quantity']
        )

        # Resize map
        fig.update_layout(
            autosize=False,
            margin=dict(l=0, r=0, b=0, t=0, pad=4, autoexpand=True),
            width=800,
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
        Output('revenue-trends', 'figure'),
        Input('toggle-metric', 'value')
    )
    def create_revenue_trends(metric):
        fig = px.line(
            revenue_trends,
            x='InvoiceDate',
            y='Revenue',
            title='Monthly Revenue Trends',
            labels={'Revenue': 'Revenue ($)', 'InvoiceDate': 'Date'}
        )
        fig.update_traces(mode='lines+markers', marker=dict(size=8, symbol='circle'))
        return fig
