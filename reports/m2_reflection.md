# Milestone 2 Reflection

## Summary Cards
We implemented summary cards as planned, displaying key business metrics:

- **Total Revenue** – Total sales revenue from the dataset.
- **Total Orders** – The total quantity of items purchased.
- **Total Customers** – The unique number of customers who made purchases.

These statistics provide quick insights into overall business performance, enabling managers to assess key metrics at a glance.

## Visualization Board
We successfully implemented all proposed visualizations, providing valuable insights into sales trends and business performance:

- **Top-Selling Products** – A horizontal bar chart showcasing the highest revenue-generating products.
- **Revenue Trends Over Time** – A line chart displaying revenue patterns across different months.
- **Geographic Sales Distribution** – An interactive map visualizing revenue and quantity by country.
- **Customer Retention Analysis** – A line chart illustrating returning customer trends over time.
- **Product Category Performance** – A bar chart displaying quantities sold by product category.

Each visualization includes interactive tooltips, allowing users to hover over data points for additional insights.

## User Filters
All proposed filter widgets have been implemented. Filters dynamically generate unique options from the dataset, ensuring they reflect any data updates.

We implemented the following filters:

- **Quantity and Revenue Selector** – A radio button allowing users to filter the map by revenue or quantity sold per country. The legend dynamically updates to reflect the selected metric.
- **Time Range Slider** – Filters the returning customer graph, displaying the number of customers who returned within the selected time frame.
- **Dropdown Selector for Month** – Allows users to view sales quantities for different product categories in a selected month.

**Default Filtering Behavior:**
- The **Quantity and Revenue Selector** defaults to quantity.
- The **Time Range Slider** is set to 6 months by default, enabling long-term trend analysis.
- The **Dropdown Selector** defaults to December 2011 but allows users to select other months.

## Challenges and Adjustments

### Handling Large Data Size
Processing the full dataset was inefficient and created issues when deploying to Render, so we opted for a representative data sample. This resolved our deployment issues while maintaining analytical integrity.

### Modularization Challenges
We followed a modularization approach in this milestone, but Render had difficulty reading all the files properly. We resolved this by using the `sys` package to determine absolute file paths.

### Visualization Adjustments
We initially planned to use a word cloud but replaced it with a bar chart, which provides a clearer and more interpretable representation of the data. This deviation from the proposal was agreed upon by the team to improve the dashboard's analytical capabilities.

## Additional Component (Challenging Question)
We introduced a **month selection dropdown** with a corresponding bar chart showing quantity sold per category. This enhancement improves user interaction by allowing dynamic filtering based on month. Users can quickly compare different months without overwhelming the interface, making the dashboard more interactive and user-friendly.

## Strengths
Our dashboard features several strengths:
1. Interactive elements like tooltips and filters enhance user engagement by allowing deeper data exploration.
2. Dynamically generated filter options ensure accuracy as the dataset evolves.
3. Summary cards provide a concise overview of essential business metrics.
4. Using a representative sample instead of the full dataset maintains responsiveness while preserving analytical accuracy.

## Limitations
Some limitations exist within our current implementation:
1. The summary cards remain static and do not update dynamically based on selected filters.
2. The dashboard focuses solely on historical data, lacking predictive analytics that could provide future insights.
3. Limited contextual analysis when examining specific data subsets.

## Future Improvements
We've identified several potential improvements:
1. Making summary cards dynamic so they update based on selected filters.
2. Enhancing cross-filtering functionality between visualizations.
3. Using a pre-trained ML model for identifying product categories.

These improvements would significantly enhance usability and provide a more powerful analytical experience for users.