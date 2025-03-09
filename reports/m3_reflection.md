## Milestone 3 Reflection

### Summary Cards
In Milestone 3, we enhanced the summary cards to include dynamic updates based on user-selected filters. This improvement allows users to see real-time changes in key metrics such as **Total Revenue**, **Total Orders**, and **Total Customers** as they interact with the dashboard. This feature provides a more responsive and insightful user experience.

### Visualization Board
We continued to refine our visualizations to ensure they are both informative and user-friendly. The **Top-Selling Products** bar chart and **Revenue Trends Over Time** line chart now include more detailed tooltips and smoother transitions. The **Geographic Sales Distribution** map has been improved to include interactive dropdowns for country and category filters, making it easier for users to explore data by specific regions and product types.

### User Filters
We implemented several global filter functionalities to enhance user interaction:
- **Category and Country Dropdowns**: These dropdowns allow users to filter data by specific categories and countries, providing a more granular view of the data.
- **Revenue/Quantity Filter**: This filter enables users to switch between viewing revenue and quantity metrics across different visualizations.
- **All Functionality in Dropdowns**: We added an "All" option to the dropdowns, allowing users to reset filters and view the complete dataset.

### Challenges and Adjustments
- **Dropdown Implementation**: Integrating the dropdown filters required careful handling of state management to ensure that all visualizations updated correctly based on user selections.
- **Slider to Calendar Range**: We initially planned to change the slider to a calendar range but faced technical challenges. Instead, we enhanced the existing slider to provide more precise control over the time range. This change can be revisited as a future improvement.
- **Modularization**: We further modularized our code to improve readability and maintainability, ensuring that each component is self-contained and easier to debug.

### Additional Component (Challenging Question)
Inspired by our peers, we introduced a **sidebar** to the dashboard. This sidebar consolidates all filter controls and key information in one accessible location, improving the overall user experience. The sidebar includes dropdowns for category and country filters, a revenue/quantity selector, and a time range slider. This addition not only enhances the dashboard's functionality but also makes it more intuitive and easier to navigate.

### Major Changes Implemented
1. **Make All Widgets Global**: We ensured that all widgets are global, allowing them to interact seamlessly across different visualizations.
2. **Add Two More Widgets**: We added a **category dropdown** and a **country dropdown** to provide more specific filtering options. In the future, we plan to implement map clicks to further enhance the country filter functionality.

### Minor Changes Implemented
1. **Center Text in Cards**: We centered the text in the summary cards for better visual alignment.
2. **Put Cards on Top Again**: The summary cards were repositioned to the top of the dashboard for easier access and visibility.
3. **Remove Redundant Title**: We removed redundant titles to streamline the interface and reduce clutter.
4. **Move Map on Top**: The map was moved to the top of the visualization board to highlight geographic data more prominently.
5. **Remove Footer and Put Info in Sidebar**: We removed the footer and integrated its information into the sidebar, creating a cleaner and more organized layout.
6. **Remove Outline of Title in Sidebar**: The outline of the title in the sidebar was removed to improve the aesthetic appeal.

### Strengths
Our dashboard continues to excel in several areas:
1. **Interactivity**: Enhanced filters and dynamic updates make the dashboard more engaging and useful.
2. **User-Friendly Design**: Clear visualizations and intuitive controls improve the overall user experience.
3. **Data Accuracy**: Dynamically generated filters ensure that the data presented is always up-to-date and relevant.
4. **Dynamic Summary Statistics**: The summary statistics update dynamically based on user-selected filters, providing real-time insights into key metrics.

### Limitations
Despite these improvements, some limitations remain:
1. **Complex Filters**: The addition of multiple filters can sometimes overwhelm users, especially those unfamiliar with the dataset.
2. **Performance**: With the increased interactivity, we noticed slight performance issues when handling large datasets.

### Future Improvements
To address these limitations and further enhance the dashboard, we plan to:
1. **Cross-Filtering**: Implement cross-filtering between visualizations to provide a more cohesive analytical experience.
2. **Predictive Analytics**: Introduce predictive analytics to offer insights into future trends based on historical data.
3. **Performance Optimization**: Optimize the dashboard's performance to handle larger datasets more efficiently.
4. **Calendar Range Slider**: Revisit the implementation of a calendar range slider for more precise time-based filtering.

### Reflection
In this milestone, we successfully implemented several new features and refined existing ones to improve the dashboard's functionality and user experience. The introduction of the sidebar, inspired by our peers, has significantly enhanced the dashboard's usability. While we faced some technical challenges, the adjustments we made have resulted in a more robust and interactive tool. We remain committed to continuous improvement and look forward to addressing the identified limitations in future iterations.