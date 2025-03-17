import pandas as pd
import altair as alt
import plotly.express as px

from dash import Input, Output

import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from data.data import (
    get_monthly_customer_retention, 
    get_revenue_quantity_trends,
    get_country_sales,
    get_data,
    get_product_revenue_quantity,
    get_monthly_sales_data,
    get_summary_metrics 
)

from callbacks.summary_metric_helper import summary_metrics


df = get_data()

def register_callbacks(app):
    """
    Registers all Dash callbacks for dynamic updates in the dashboard.
    
    Args:
        app (Dash): Dash application instance.
    """

    @app.callback(
        Output("summary-metrics-container", "children"),
        Input("num-months", "value"),
         Input('country-dropdown', 'value'),
        Input('category-dropdown', 'value')
    )
    def update_summary_metrics(num_months, selected_country, selected_category):
        """
        Updates the summary metrics displayed on the dashboard.
        
        Args:
            num_months (int): Number of months to filter.
            selected_country (list): Selected countries.
            selected_category (list): Selected categories.
        
        Returns:
            HTML components: Updated summary metrics.
        """

        if not isinstance(selected_country, list):
            selected_country = ["All"]
        if not isinstance(selected_category, list):
            selected_category = ["All"]

        # Fetch updated statistics based on user selections
        metrics = get_summary_metrics(num_months, selected_country, selected_category)
        
        return summary_metrics(
            metrics["total_revenue"],
            metrics["total_orders"],
            metrics["total_customers"]
        )


    @app.callback(
        Output('map', 'figure'),
        Input('toggle-metric', 'value'),
        Input('map', 'hoverData'),
        Input('num-months', 'value'),
        Input('country-dropdown', 'value'),
        Input('category-dropdown', 'value')
    )
    def create_map(metric, hoverData, num_months, selected_country, selected_category):
        """
        Creates a geographical sales (revenue/quantity) distribution map.
        
        Args:
            metric (str): The metric to display (Revenue or Quantity).
            hoverData (dict): Data of hovered region.
            num_months (int): Number of months to filter.
            selected_country (list): Selected countries.
            selected_category (list): Selected categories.
        
        Returns:
            plotly.figure: Choropleth map displaying sales data.
        """

        if not isinstance(selected_country, list):
            selected_country = ["All"]
        if not isinstance(selected_category, list):
            selected_category = ["All"]

        country_sales = get_country_sales(num_months, selected_country, selected_category)
        fig = px.choropleth(
            country_sales,
            locations='iso_alpha',
            color=metric,
            hover_name='Country',
            title='🌍 Geographical Sales Distribution',
            color_continuous_scale=px.colors.sequential.Viridis,
            custom_data=['Country', 'Revenue', 'Quantity'],
            projection="natural earth"
        )

        # Resize map
        fig.update_layout(
            autosize=True,
            margin=dict(l=0, r=0, b=0, t=30, pad=2, autoexpand=True)
        )

        fig.update_geos(
            lataxis_range=[-20, 90],
            lonaxis_range=[-200, 200], 
            projection_scale=1,
            showframe=True,
            framecolor="black",
            framewidth=2 
        )

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
        Output('monthly-retention', 'spec'),
        Input('num-months', 'value'),
        Input('country-dropdown', 'value'),
        Input('category-dropdown', 'value')
    )
    def update_monthly_retention(num_months, selected_country, selected_category):
        """
        Updates the monthly customer retention chart.
        
        Args:
            num_months (int): Number of months to filter.
            selected_country (list): Selected countries.
            selected_category (list): Selected categories.
        
        Returns:
            dict: Altair chart JSON specification.
        """

        if not isinstance(selected_country, list):
            selected_country = ["All"]
        if not isinstance(selected_category, list):
            selected_category = ["All"]

        filtered_retention = get_monthly_customer_retention(num_months, selected_country, selected_category)

        if filtered_retention.empty:
            # Create a default DataFrame with zero values
            filtered_retention = pd.DataFrame({
                'Month': pd.date_range(end='2011-12', periods=num_months, freq='M').strftime('%Y-%m'),
                'Count': [0] * num_months
            })
        if isinstance(filtered_retention['Month'].iloc[0], pd.Period):
            filtered_retention['Month'] = filtered_retention['Month'].dt.strftime('%b-%Y')
        else:
            filtered_retention['Month'] = filtered_retention['Month'].astype(str)

        fig = alt.Chart(filtered_retention, width='container', height='container').mark_line(point=True, color="#488a99").encode(
            x=alt.X('Month:N', title='Month', sort=None, axis=alt.Axis(labelAngle=45)), 
            y=alt.Y('Count:Q', title=None),
            tooltip=['Month', 'Count']
        ).properties(
            title=f'Returning Customers by Month (Last {num_months} Months)',
        ).configure_axis(
            labelFontSize=12,
            titleFontSize=14
        ).configure_title(
            fontSize=16
        )

        return fig.to_dict()


    @app.callback(
        Output('revenue-trends', 'spec'),
        Input('toggle-metric', 'value'),
        Input('num-months', 'value'),
        Input('country-dropdown', 'value'),
        Input('category-dropdown', 'value')
    )
    def create_revenue_quantity_trends(metric, num_months, selected_country, selected_category):
        """
        Generates a line chart displaying revenue or quantity trends over time.
        
        Args:
            metric (str): The selected metric (Revenue or Quantity).
            num_months (int): Number of months to filter.
            selected_country (list): Selected countries.
            selected_category (list): Selected categories.
        
        Returns:
            dict: Altair chart JSON specification.
        """

        if not isinstance(selected_country, list):
            selected_country = ["All"]
        if not isinstance(selected_category, list):
            selected_category = ["All"]

        revenue_trends = get_revenue_quantity_trends(num_months, selected_country, selected_category)
        revenue_trends['Month'] = pd.to_datetime(revenue_trends['Month'], format='%Y-%m')
        print(revenue_trends)
        revenue_trends['Month'] = revenue_trends['Month'].dt.strftime('%b %Y')
        print(revenue_trends)


        fig = alt.Chart(revenue_trends, width='container', height='container').mark_line(point=True, color="#488a99").encode(
            x=alt.X('Month:N', title='Date', sort=None, axis=alt.Axis(labelAngle=45)),
            y=alt.Y(f'{metric}:Q', title=metric, sort=None),  # Dynamically update Y-axis
            tooltip=[
                alt.Tooltip('Month:N', title='Date:'),
                alt.Tooltip(f'{metric}:Q', title=f'{metric} ($):' if metric == 'Revenue' else f'{metric}', format="$.2f" if metric == 'Revenue' else ",.0f")
            ]
        ).properties(
            title=f'Monthly {metric} Trends'  # Dynamically update title
        ).configure_axis(
            labelFontSize=12,
            titleFontSize=14
        ).configure_title(
            fontSize=16
        )

        return fig.to_dict()


    @app.callback(
        Output('revenue-by-product', 'spec'),
        Input('toggle-metric', 'value'),
        Input('num-months', 'value'),
        Input('country-dropdown', 'value'),
        Input('category-dropdown', 'value')
    )
    def create_revenue_quantity_by_product(metric, num_months, selected_country, selected_category):
        """
        Generates a bar chart displaying revenue/quantity by product.
        
        Args:
            metric (str): The selected metric (Revenue or Quantity).
            num_months (int): Number of months to filter.
            selected_country (list): Selected countries.
            selected_category (list): Selected categories.
        
        Returns:
            dict: Altair chart JSON specification.
        """
        if not isinstance(selected_country, list):
            selected_country = ["All"]
        if not isinstance(selected_category, list):
            selected_category = ["All"]
            
        product_revenue = get_product_revenue_quantity(num_months, selected_country, selected_category)
        top_product_revenue = product_revenue.nlargest(10, metric)
        
        fig = alt.Chart(top_product_revenue, width='container', height='container').mark_bar(color="#488a99").encode(
            x=alt.X(f"{metric}:Q", title=metric),
            y=alt.Y("Description:N", sort="-x", title=None, axis=alt.Axis(labelAngle=0)), 
            tooltip=[
                alt.Tooltip('Description', title='Product:'),
                alt.Tooltip(f"{metric}:Q", title=f"{metric} ($)" if metric == 'Revenue' else metric, format="$.2f" if metric == 'Revenue' else ",.0f")
            ]
        ).configure_axis(
            labelFontSize=12,
            titleFontSize=14
        ).configure_title(
            fontSize=16
        ).properties(
            title=f"{metric} by Product"
        )
        
        return fig.to_dict()
    

    @app.callback(
        Output("monthly-sales-bar-chart", "spec"),
        Input('toggle-metric', 'value'),
        Input('num-months', 'value'),
        Input('country-dropdown', 'value'),
        Input('category-dropdown', 'value')
    )
    def update_monthly_sales_chart(metric, num_months, selected_country, selected_category):
        """
        Generates a bar chart displaying sales data (revenue/quantity) by category.
        
        Args:
            metric (str): The selected metric (Revenue or Quantity).
            num_months (int): Number of months to filter.
            selected_country (list): Selected countries.
            selected_category (list): Selected categories.
        
        Returns:
            dict: Altair chart JSON specification.
        """

        # Get filtered data from data.py
        df_filtered = get_monthly_sales_data(num_months, selected_country, selected_category)

        # Create bar chart dynamically based on the selected metric
        chart = alt.Chart(df_filtered, width='container', height='container').mark_bar(color="#488a99").encode(
            x=alt.X(f"{metric}:Q", title=metric),  # Updated dynamically
            y=alt.Y("Category", sort="-x", title=None),
            tooltip=[
                alt.Tooltip(f'{metric}:Q', title=f'{metric}'),
                alt.Tooltip('Category', title='Category')
            ]
        ).configure_axis(
            labelFontSize=12,
            titleFontSize=14
        ).configure_title(
            fontSize=16
        ).properties(
            title=f"{metric} Sold per Category",
            background="white"
        )

        return chart.to_dict()
    

    # Callback to prevent empty selection
    @app.callback(
        Output("country-dropdown", "value"),
        Input("country-dropdown", "value"),
        prevent_initial_call=True
    )
    def enforce_country_selection(selected_values):
        if not selected_values:  # If empty, keep the last known selection
            return ["All"]
        
        if "All" in selected_values and len(selected_values) > 1:
            return [val for val in selected_values if val != "All"]
        
        return selected_values 
    
    # Callback to prevent empty selection
    @app.callback(
        Output("category-dropdown", "value"),
        Input("category-dropdown", "value"),
        prevent_initial_call=True
    )
    def enforce_category_selection(selected_values):
        if not selected_values:  # If empty, keep the last known selection
            return ["All"]
        
        if "All" in selected_values and len(selected_values) > 1:
            return [val for val in selected_values if val != "All"]

        return selected_values 