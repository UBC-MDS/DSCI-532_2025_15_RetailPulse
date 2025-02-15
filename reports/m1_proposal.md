# **Online Retail Dashboard Proposal**

## **1. Motivation and Purpose**  

As a **data analytics team**, we are creating this dashboard for **retail operations managers** like **Long Nyugen**, who struggle to make quick, data-driven decisions about inventory, marketing, and business expansion.  

Currently, managers rely on **basic tools like Excel** and spend excessive time **manually analyzing** sales data across different countries, products, and time periods. This makes it difficult to efficiently identify **market trends, optimize inventory, and improve customer retention strategies**.  

Our interactive dashboard will provide **real-time insights** on:
- **Geographical sales distribution** (identifying top-performing countries)
- **Revenue trends over time** (detecting seasonal patterns)
- **Customer retention metrics** (understanding repeat buyers)
- **Product performance** (highlighting top-selling and high-revenue products)
- **Product categories contributing to revenue** (to guide inventory decisions)

Through **intuitive visualizations**, our dashboard will enable managers to make **faster, data-driven decisions**, helping them **maximize profits, optimize stock levels, and refine marketing efforts**.  

---

## **2. About the Online Retail Dataset**  

### **Context**  
This dataset contains **transactional data from an online retail store**, capturing **sales information** across various customers and products from **December 2010 to June 2011**. Each row represents a **purchase transaction**, with details such as:  
- **Time of purchase**  
- **Customer ID**  
- **Countries** (where the purchases were made)  
- **Unit Price** of products  
- **Sales Quantity** (number of items bought)  
- **Product Descriptions**  
- **Stock Codes** (unique product identifiers)  
- **Invoice Numbers**  

Retail businesses often seek to **optimize inventory, understand purchasing patterns, and improve marketing strategies**. By analyzing this dataset, we can uncover **valuable insights** that help businesses enhance **customer engagement and sales performance**.  

### **Content**  
The dataset consists of **5,000 retail transactions** with the following key attributes:

#### **Transaction Details**  
- `InvoiceNo`: Unique transaction number  
- `InvoiceDate`: Date and time of the purchase  

#### **Product Information**  
- `StockCode`: Unique identifier for each product  
- `Description`: Name of the product  
- `UnitPrice`: Price per unit of the item  

#### **Purchase Details**  
- `Quantity`: Number of units purchased in a transaction  
- **Derived Variable**: `TotalSales = Quantity × UnitPrice` (Total purchase value)  

#### **Customer & Location Information**  
- `CustomerID`: Unique identifier for customers (**some transactions lack this value**)  
- `Country`: Country where the purchase was made  

### **Derived Variables**  
To enhance analysis, we will create new features such as:
✅ **TotalSales** (Revenue per transaction)  
✅ **Repeat Customer Flag** (Tracking customer retention)  
✅ **Sales Per Country** (Aggregating sales by location)  
✅ **Product Category Revenue Contribution** (Grouping products by category)  

---

## **3. Research Questions & Usage Scenarios**  

### **Key Questions We Aim to Answer**  
1. **How many customers/sales do we have in each country?**  
   - 📊 **Chart**: **Interactive Map** showing **customer/sales count per country**  
   - 🎯 **Benefit**: Identifies **high-performing regions** and helps in **targeted marketing & expansion strategies**.  

2. **What is the total revenue generated in the past few months?**  
   - 📊 **Chart**: **Line Chart** showing **revenue trends over time**  
   - 🎯 **Benefit**: Tracks **sales performance**, identifies **seasonality**, and supports **sales forecasting**.  

3. **What is the mean number of returning customers per month?**  
   - 📊 **Chart**: **Line/Bar Chart** tracking **repeat customer counts**  
   - 🎯 **Benefit**: Helps **analyze customer retention** and guide **targeted advertisements**.  

4. **What are the top 5 products that generate the most revenue?**  
   - 📊 **Chart**: **Horizontal Bar Chart** listing **highest revenue-generating products**  
   - 🎯 **Benefit**: Helps **optimize inventory decisions** and **identify key products for marketing**.  

5. **Which product categories generate the most revenue?**  
   - 📊 **Chart**: **Word Cloud with Tooltip** displaying **top revenue-generating categories**  
   - 🎯 **Benefit**: Guides **inventory expansion decisions** based on **high-performing product categories**.  

### **Usage Scenario**  
📌 **Persona**: Long Nyugen, a retail operations manager, needs to track sales performance and optimize inventory for multiple regions.  

🔍 **Goals & Tasks:**  
- Identify **top-performing products** and understand **customer demand trends**.  
- Compare **sales across different countries** to optimize **regional marketing strategies**.  
- Track **repeat customers** and explore opportunities for loyalty programs.  
- Ensure **inventory is aligned with sales trends** to reduce overstocking or shortages.  

🛠️ **How the Dashboard Helps:**  
- Long logs into the dashboard and **views total revenue trends** in an interactive **line chart**.  
- He filters sales data by **country and time period** to **identify key markets**.  
- Using a **heatmap**, he spots **seasonal spikes** in sales.  
- He checks the **customer retention panel** to see which customers **purchase frequently**.  
- He downloads **a report with sales insights** to share with the marketing team.  

🎯 **Outcome**:  
Long can now **quickly assess sales patterns**, leading to **better inventory planning, targeted promotions, and improved customer retention strategies**.  

---

## **4. User Persona**  

| Attribute | Details |
|-----------|---------|
| **Name** | Long Nyugen |
| **Age** | 27 |
| **Job Title** | Retail Operations Manager |
| **Industry** | Consumer Goods / Retail |
| **Experience Level** | Mid-Senior Level |
| **Tools Familiarity** | Excel, Power BI, basic dashboards – but relies on visual tools for quick insights |
| **Primary Goal** | Drive sales growth, optimize product inventory, expand market reach, create a marketing strategy |

---

