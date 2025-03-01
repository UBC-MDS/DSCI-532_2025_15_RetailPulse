**Milestone 2 Reflection**  

### **Visualization Board**  
We successfully implemented all proposed visualizations, providing valuable insights into sales trends and business performance:  

- **Revenue Trends Over Time** – A line chart displaying revenue trends across different months.
- **Customer Retention Analysis** – A bar chart illustrating returning customer trends over time (in months).
- **Geographic Sales Distribution** – An interactive map visualizing revenue and quantity by country.
- **Top-Selling Products** – A horizontal bar chart showcasing the highest revenue-generating products.
- **Product Category Performance** – A bar chart displaying quantities sold by product category.  

Each visualization includes interactive tooltips, allowing users to hover over data points for additional insights.  

### **Summary Cards**  
We implemented summary cards as planned, displaying key business metrics:  

- **Total Revenue** – Total sales revenue from the dataset.  
- **Total Orders** – The total quantity of items purchased.  
- **Total Customers** – The unique number of customers who made purchases.  

These summary statistics provide quick insights into overall business performance, enabling managers to assess key metrics at a glance.  

### **User Filters**  
All proposed filter widgets have been implemented. Filters dynamically generate unique options from the dataset, ensuring they reflect any data updates.  

The following filters were implemented:  

- **Quantity and Revenue Selector** – A radio button that allows users to filter the map by revenue or quantity sold per country. The legend dynamically updates to reflect the selected metric.  
- **Time Range Slider** – Filters the returning customer graph, displaying the number of customers who returned within the selected time frame.  
- **Dropdown Selector for Month** – Allows users to view sales quantities for different product categories in a selected month.  

**Default Filtering Behavior:**  
- The **Quantity and Revenue Selector** defaults to quantity.  
- The **Time Range Slider** is set to 6 months by default, enabling long-term trend analysis.  
- The **Dropdown Selector** defaults to December but allows users to select other months.  

### **Challenges and Adjustments**  

#### **Handling Large Data Size**  
- Processing the full dataset was inefficient, so we opted for a representative sample. This maintained accuracy while optimizing performance.  

#### **Modularization Challenges**  
- To improve code structure and maintainability, we used the `sys` package for better modularization, making debugging and updates more manageable.  

#### **Visualization Adjustments**  
- We initially planned to use a word map but replaced it with a bar chart, which provided a clearer and more interpretable representation of the data

Note that changing from a word cloud to the bar chart is the major deviation from the proposal, but the team agreed that this would improve the analytical aspects of the dashboard. 

### **Additional Component (Challenging question)**  
We introduced a **month selection dropdown**, enhancing user interaction by allowing dynamic filtering. This feature improves usability, making trend analysis more intuitive and efficient. Users can quickly compare different months without overwhelming the interface with excessive data, making the dashboard more interactive and user-friendly.  

### **Strengths**  
The dashboard has several strengths. Interactive elements, such as tooltips and filters, enhance user engagement by allowing deeper data exploration. Additionally, dynamically generated filter options ensure accuracy and adaptability as the dataset evolves. The summary cards provide a concise overview of essential business metrics, enabling decision-makers to assess performance quickly. Furthermore, by using a representative sample instead of the full dataset, the dashboard maintains responsiveness while preserving analytical accuracy.  

### **Limitations**  
Some limitations exist within the dashboard. One key issue is that the summary cards remain static, meaning they do not update dynamically based on selected filters. This restricts contextual insights when analyzing specific data subsets. Additionally, the dashboard focuses solely on historical data, lacking predictive analytics that could provide future insights, such as revenue forecasts or anomaly detection.  

### **Improvements**  
The dashboard's visualizations could be refined by implementing **Vega**, which offers more flexibility and cleaner data representation. Another key enhancement would be making the summary cards dynamic so they update based on selected filters, ensuring more relevant and contextual insights. These improvements would enhance usability and provide a more powerful analytical experience.  

