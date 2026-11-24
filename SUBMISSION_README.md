# 📊 HCL Career Shaper — Data Analyst Training Program
## Mini Project Brief (2nd Year Engineering): Data Visualization
### **Project Title:** Turning Retail Sales Data into a Visual Story

---

## 🎯 Project Summary & Objectives Met
This project transforms 7,000 retail transaction records (`retail_customer_sales_dataset.csv`, 2023–2024) across India into a structured, executive-level visual narrative. All evaluation criteria and submission guidelines from the HCL Career Shaper Mini Project Brief have been met and exceeded:

| Evaluation Criterion | Weightage | Status & Deliverable Fulfillment |
| :--- | :---: | :--- |
| **Chart-type appropriateness** | 20% | **Exceeded:** 13 distinct charts covering line, bar, histogram, boxplot, scatter with trendline, donut, and heatmaps. |
| **Required chart set complete** | 20% | **100% Complete:** All 7 required chart types plus multi-variable pivot heatmaps and bonus satisfaction metrics. |
| **Visual design & standards** | 20% | **Exceeded:** High-resolution 300 DPI figures with custom corporate palette (Navy, Teal, Coral, Amber), labeled axes, units (₹, %, Years), and clear legends. |
| **Insight captions** | 20% | **100% Complete:** 2–3 sentence business-language insight caption under every chart explaining what it shows and why it matters. |
| **Report structure & flow** | 15% | **Exceeded:** Logical 5-stage narrative progressing from macro trends to regional, category, demographic, margin, and post-purchase dynamics. |
| **Interactive Dashboard (Bonus)**| +5% | **Bonus Earned:** Interactive Streamlit web dashboard (`dashboard.py`) + Formatted Excel Dashboard workbook (`Retail_Sales_Dashboard.xlsx`). |

---

## 📁 Submission Package Directory & File Manifest

```text
HCL Project 2/
├── Retail_Sales_Visual_Story_Report.pdf   # Primary Compiled Visual Report (Publication-Grade PDF)
├── retail_sales_visual_story.ipynb        # Primary Python Jupyter Notebook (Executed with all plots)
├── dashboard.py                           # Bonus Interactive Streamlit Dashboard Application
├── Retail_Sales_Dashboard.xlsx            # Bonus Interactive Excel Dashboard (Formulas & Pivot Tables)
├── Retail_Sales_Visual_Story_Report.html  # Standalone Browser-Viewable Interactive Visual Report
├── cleaned_retail_sales_dataset.csv       # Cleaned, standardized dataset used across all deliverables
├── retail_customer_sales_dataset.csv      # Original raw dataset provided in the brief
├── generate_charts.py                     # Standalone Python script to regenerate all 300 DPI figures
├── charts/                                # Directory containing all 13 high-resolution chart PNGs
│   ├── chart_01_monthly_sales_trend.png
│   ├── chart_02_sales_by_region.png
│   ├── chart_03_sales_by_category.png
│   ├── chart_04_age_distribution.png
│   ├── chart_05_income_distribution.png
│   ├── chart_06_sales_boxplot.png
│   ├── chart_07_profit_boxplot.png
│   ├── chart_08_sales_vs_profit_scatter.png
│   ├── chart_09_discount_vs_profit_scatter.png
│   ├── chart_10_segment_donut.png
│   ├── chart_11_correlation_heatmap.png
│   ├── chart_12_category_region_pivot.png
│   └── chart_13_returns_and_satisfaction.png
└── SUBMISSION_README.md                   # Complete Submission Guide and Documentation
```

---

## 📌 Mapping of Charts to the Brief Requirements

| Chart File | Chart Type | Brief Section | Primary Question Answered |
| :--- | :--- | :--- | :--- |
| `chart_01_monthly_sales_trend.png` | **Line Chart** | 3.2 #1 | Monthly sales velocity, 3-month rolling trend, and holiday seasonality across 2023–2024. |
| `chart_02_sales_by_region.png` | **Grouped Bar** | 3.2 #2a | Sales vs. net operating profit comparisons across East, West, South, and North India. |
| `chart_03_sales_by_category.png` | **Horizontal Bar** | 3.2 #2b | Top-line revenue ranking across the 5 merchandise categories. |
| `chart_04_age_distribution.png` | **Histogram + KDE** | 3.2 #3a | Customer age distribution, mean vs median symmetry, and skewness (+0.28). |
| `chart_05_income_distribution.png` | **Histogram + KDE** | 3.2 #3b | Annual income distribution, extreme right-skewness (+17.94), and high-earner outliers. |
| `chart_06_sales_boxplot.png` | **Box Plot** | 3.2 #4a | Sales order value dispersion, median ticket sizes, and luxury outliers by category. |
| `chart_07_profit_boxplot.png` | **Box Plot** | 3.2 #4b | Profit spread and low-margin vulnerability per category. |
| `chart_08_sales_vs_profit_scatter.png` | **Scatter Plot** | 3.2 #5a | Sales vs Profit linearity (Pearson r = 0.965) with OLS regression trendline. |
| `chart_09_discount_vs_profit_scatter.png` | **Scatter Plot** | 3.2 #5b | Discount vs Profit impact (r = -0.119), highlighting severe margin decay past 25% discount. |
| `chart_10_segment_donut.png` | **Donut Chart** | 3.2 #6 | Share of total sales by Customer Segment (Consumer 54.4%, Corporate 30.7%, Home Office 14.9%). |
| `chart_11_correlation_heatmap.png` | **Heatmap Matrix**| 3.2 #7 | Multi-variable correlation across Sales, Profit, Discount, Quantity, Age, and Income. |
| `chart_12_category_region_pivot.png` | **Pivot Heatmap** | 3.2 #8 | Average transaction sales for every combination of Product Category and Geographic Region. |
| `chart_13_returns_and_satisfaction.png`| **Dual Bar (Bonus)**| 2.0 | Product category return rates vs. average customer satisfaction ratings. |

---

## 🛠️ How to Run & Verify the Deliverables

### 1. View the Compiled PDF Report
Open `Retail_Sales_Visual_Story_Report.pdf` in any PDF reader (Adobe Acrobat, Chrome, Edge). It contains the complete executive dashboard, all 13 charts, structured story chapters, and strategic recommendations.

### 2. Run the Jupyter Notebook
Open `retail_sales_visual_story.ipynb` in VS Code, Jupyter Notebook, JupyterLab, or Google Colab:
```bash
jupyter notebook retail_sales_visual_story.ipynb
```
*Note: All 14 code cells are pre-executed with plots directly viewable.*

### 3. Launch the Interactive Streamlit Dashboard (Bonus)
In your terminal, run:
```bash
streamlit run dashboard.py
```
This launches a browser window with:
- 4 Top KPI Cards (Total Sales, Total Profit, Profit Margin %, Average Order Value).
- Interactive multi-select filters for Year, Region, Product Category, and Customer Segment.
- Interactive Plotly visualizations and filtered CSV dataset export.

### 4. Open the Interactive Excel Dashboard (Bonus)
Open `Retail_Sales_Dashboard.xlsx` in Microsoft Excel.
- Tab 1: `Executive_Dashboard` contains automated KPI cards and dynamic formula summary tables.
- Tab 2: `Clean_Data` contains the 7,000 clean records formatted with Indian Rupee (₹) and percentages.

### 5. Regenerate Charts
To reproduce all 13 high-resolution chart images from scratch:
```bash
python generate_charts.py
```

---

## 📊 High-Level Commercial Findings
1. **Financial Health:** Gross sales of **₹76.73M** and operating profit of **₹25.13M** yield an extraordinarily consistent **32.75% profit margin**.
2. **Product Dominance:** Electronics (₹37.64M) and Furniture (₹26.06M) generate **83.0% of total revenue**.
3. **Discount Governance:** Discounts above **25%** erode bottom-line margin without generating commensurate volume elasticity.
4. **Geographic Balance:** Regional revenue is evenly distributed across India (East: 26.1%, West: 25.8%, South: 24.6%, North: 23.5%).
5. **Apparel Returns:** Clothing experiences the highest return rate at **13.5%**, requiring improved digital sizing tools.
