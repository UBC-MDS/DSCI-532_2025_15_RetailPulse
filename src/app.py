import dash
from dash import dcc, html
import plotly.express as px
import pandas as pd

# Initialize Dash app
app = dash.Dash(__name__)

# Sample dataset (Replace this with actual data processing logic)
df = pd.DataFrame({
    "Date": pd.date_range(start="2021-01-01", periods=5, freq='M'),
    "Revenue": [4000, 4500, 5000, 5200, 5400]
})

# Basic revenue trend line chart
fig_revenue = px.line(df, x="Date", y="Revenue", title="Revenue Over Time")

# Layout of the app
app.layout = html.Div([
    html.H1("RetailPulse Dashboard", style={'textAlign': 'center'}),
    
    # Summary Board
    html.Div([
        html.Div([
            html.H3("Revenue (Last 30 Days)"),
            html.H2("$5,113", style={"color": "green"}),
            html.P("▲ 3.67%")
        ], style={"display": "inline-block", "width": "30%", "padding": "10px", "border": "1px solid #ddd"}),

        html.Div([
            html.H3("Number of Customers (Last 30 Days)"),
            html.H2("90", style={"color": "green"}),
            html.P("▲ 50%")
        ], style={"display": "inline-block", "width": "30%", "padding": "10px", "border": "1px solid #ddd"}),

        html.Div([
            html.H3("Total Returning Customers (Last 30 Days)"),
            html.H2("60", style={"color": "green"})
        ], style={"display": "inline-block", "width": "30%", "padding": "10px", "border": "1px solid #ddd"})
    ], style={"textAlign": "center", "marginBottom": "20px"}),
    
    # Revenue Chart
    dcc.Graph(figure=fig_revenue),
    
    # Placeholder for future components
    html.Div("More charts and interactivity will be added here...", style={"textAlign": "center", "marginTop": "20px"})
])

# Run the app
if __name__ == "__main__":
    app.run_server(debug=True)
