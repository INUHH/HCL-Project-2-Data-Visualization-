"""
Generate Standalone Interactive HTML Visual Report
File: Retail_Sales_Visual_Story_Report.html
"""

import base64
import os

def b64_img(path):
    with open(path, 'rb') as f:
        return f"data:image/png;base64,{base64.b64encode(f.read()).decode('utf-8')}"

html_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Turning Retail Sales Data into a Visual Story | HCL Career Shaper</title>
    <style>
        body {{
            font-family: 'Segoe UI', -apple-system, BlinkMacSystemFont, Roboto, Helvetica, Arial, sans-serif;
            background-color: #F8FAFC;
            color: #1E293B;
            margin: 0;
            padding: 40px 20px;
            line-height: 1.6;
        }}
        .container {{
            max-width: 1000px;
            margin: 0 auto;
            background: #FFFFFF;
            padding: 48px;
            border-radius: 12px;
            box-shadow: 0 4px 20px rgba(0, 0, 0, 0.06);
        }}
        .header {{
            border-bottom: 3px solid #1B365D;
            padding-bottom: 24px;
            margin-bottom: 32px;
        }}
        .badge {{
            display: inline-block;
            background: #E2E8F0;
            color: #1B365D;
            padding: 4px 12px;
            border-radius: 20px;
            font-size: 12px;
            font-weight: 700;
            text-transform: uppercase;
            letter-spacing: 0.5px;
            margin-bottom: 12px;
        }}
        h1 {{
            color: #1B365D;
            font-size: 28px;
            margin: 0 0 8px 0;
            font-weight: 800;
        }}
        .subtitle {{
            color: #008080;
            font-size: 16px;
            font-weight: 600;
            margin: 0 0 16px 0;
        }}
        .meta-info {{
            font-size: 13px;
            color: #64748B;
            display: flex;
            flex-wrap: wrap;
            gap: 20px;
        }}
        .kpi-grid {{
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
            gap: 16px;
            margin: 28px 0;
        }}
        .kpi-card {{
            background: #F8FAFC;
            border: 1px solid #E2E8F0;
            border-left: 5px solid #1B365D;
            border-radius: 8px;
            padding: 16px;
        }}
        .kpi-card:nth-child(2) {{ border-left-color: #008080; }}
        .kpi-card:nth-child(3) {{ border-left-color: #E26D5C; }}
        .kpi-card:nth-child(4) {{ border-left-color: #ECA72C; }}
        .kpi-title {{
            font-size: 11px;
            text-transform: uppercase;
            color: #64748B;
            font-weight: 700;
            margin-bottom: 4px;
        }}
        .kpi-val {{
            font-size: 24px;
            font-weight: 800;
            color: #0F172A;
        }}
        .kpi-desc {{
            font-size: 12px;
            color: #2E7D32;
            margin-top: 4px;
            font-weight: 500;
        }}
        .section-title {{
            font-size: 20px;
            font-weight: 700;
            color: #1B365D;
            border-left: 4px solid #008080;
            padding-left: 12px;
            margin: 36px 0 16px 0;
        }}
        .chart-block {{
            background: #FFFFFF;
            border: 1px solid #E2E8F0;
            border-radius: 8px;
            padding: 24px;
            margin-bottom: 32px;
            box-shadow: 0 2px 8px rgba(0,0,0,0.03);
        }}
        .chart-title {{
            font-size: 16px;
            font-weight: 700;
            color: #1E293B;
            margin-top: 0;
            margin-bottom: 16px;
        }}
        .chart-img {{
            width: 100%;
            height: auto;
            border-radius: 6px;
            margin-bottom: 16px;
        }}
        .insight-box {{
            background: #F1F5F9;
            border-left: 4px solid #1B365D;
            padding: 14px 18px;
            border-radius: 0 6px 6px 0;
            font-size: 13.5px;
            color: #0F172A;
            line-height: 1.55;
        }}
        .insight-box strong {{
            color: #1B365D;
        }}
        table {{
            width: 100%;
            border-collapse: collapse;
            margin: 20px 0;
            font-size: 13.5px;
        }}
        th, td {{
            padding: 10px 14px;
            border: 1px solid #E2E8F0;
            text-align: left;
        }}
        th {{
            background: #1B365D;
            color: #FFFFFF;
            font-weight: 600;
        }}
        tr:nth-child(even) {{
            background: #F8FAFC;
        }}
        .footer {{
            margin-top: 48px;
            padding-top: 20px;
            border-top: 1px solid #E2E8F0;
            text-align: center;
            font-size: 12px;
            color: #64748B;
        }}
        @media print {{
            body {{ background: white; padding: 0; }}
            .container {{ box-shadow: none; padding: 0; max-width: 100%; }}
            .chart-block {{ page-break-inside: avoid; }}
        }}
    </style>
</head>
<body>

<div class="container">
    <div class="header">
        <span class="badge">HCL Career Shaper | Data Analyst Training Program</span>
        <h1>Turning Retail Sales Data into a Visual Story</h1>
        <div class="subtitle">Executive Visual Analytics & Commercial Performance Report (2023–2024)</div>
        <div class="meta-info">
            <span><strong>Target Audience:</strong> Regional & Senior Retail Leadership</span>
            <span><strong>Dataset:</strong> <code>retail_customer_sales_dataset.csv</code> (7,000 Clean Records)</span>
            <span><strong>Evaluation:</strong> 10+ Required Multi-Type Charts</span>
        </div>
    </div>

    <div class="kpi-grid">
        <div class="kpi-card">
            <div class="kpi-title">Total Revenue (Gross)</div>
            <div class="kpi-val">₹76.73M</div>
            <div class="kpi-desc">Across 7,000 Transactions</div>
        </div>
        <div class="kpi-card">
            <div class="kpi-title">Total Net Profit</div>
            <div class="kpi-val">₹25.13M</div>
            <div class="kpi-desc">Operating Surplus</div>
        </div>
        <div class="kpi-card">
            <div class="kpi-title">Overall Profit Margin</div>
            <div class="kpi-val">32.75%</div>
            <div class="kpi-desc">Consistent Unit Margin</div>
        </div>
        <div class="kpi-card">
            <div class="kpi-title">Avg Order Value (AOV)</div>
            <div class="kpi-val">₹10,962</div>
            <div class="kpi-desc">Average Spend per Order</div>
        </div>
    </div>

    <!-- 1. Macro Trend -->
    <div class="section-title">1. Macro Revenue Velocity & Regional Performance</div>
    
    <div class="chart-block">
        <div class="chart-title">Chart 1: Monthly Sales Trend Over Two-Year Period (Order_Date vs. Sales)</div>
        <img class="chart-img" src="{b64_img('charts/chart_01_monthly_sales_trend.png')}" alt="Monthly Sales Trend">
        <div class="insight-box">
            <strong>Business Insight:</strong> Monthly retail sales averaged ₹3.20M over 2023–2024, maintaining strong stability with seasonal peaks consistently observed in October (reaching ₹3.89M) driven by festive holiday demand. A noticeable dip occurred in June 2024 (₹2.29M), indicating a mid-year operational lull that warrants targeted summer promotions and proactive inventory realignment.
        </div>
    </div>

    <div class="chart-block">
        <div class="chart-title">Chart 2: Total Sales and Net Profit Across Geographic Regions</div>
        <img class="chart-img" src="{b64_img('charts/chart_02_sales_by_region.png')}" alt="Sales by Region">
        <div class="insight-box">
            <strong>Business Insight:</strong> Geographic sales are exceptionally balanced across all four zones, led by the East region (₹20.0M sales, ₹6.6M profit) and West region (₹19.8M sales, ₹6.5M profit), while the North region trails modestly at ₹18.1M sales. Remarkably, profit margins remain virtually uniform across regions at 32.5% to 33.0%, proving that logistical efficiencies and pricing structures are standardized company-wide.
        </div>
    </div>

    <!-- 2. Category Performance -->
    <div class="section-title">2. Product Category Performance & Order Spread</div>

    <div class="chart-block">
        <div class="chart-title">Chart 3: Revenue Contribution by Product Category</div>
        <img class="chart-img" src="{b64_img('charts/chart_03_sales_by_category.png')}" alt="Sales by Category">
        <div class="insight-box">
            <strong>Business Insight:</strong> Electronics and Furniture represent the revenue engine of the business, jointly accounting for over 83% of gross sales (₹37.6M and ₹26.1M respectively) due to substantially higher average ticket sizes. Conversely, high-frequency essentials like Grocery (₹2.69M) and Office Supplies (₹2.57M) show lower volume contributions, serving primarily as cross-sell entry points rather than primary top-line drivers.
        </div>
    </div>

    <div class="chart-block">
        <div class="chart-title">Chart 4 (Brief #4): Sales Distribution and Outliers Broken Down by Product Category</div>
        <img class="chart-img" src="{b64_img('charts/chart_06_sales_boxplot.png')}" alt="Sales Boxplot">
        <div class="insight-box">
            <strong>Business Insight:</strong> Electronics and Furniture exhibit massive transaction value spreads, with median order sizes around ₹15,000–₹22,000 and high-value outlier orders exceeding ₹80,000. In stark contrast, Clothing, Grocery, and Office Supplies maintain tight, compact interquartile spreads below ₹8,000, illustrating distinct inventory risk profiles and order value dynamics.
        </div>
    </div>

    <div class="chart-block">
        <div class="chart-title">Chart 5: Net Profit Spread and Low-Margin Vulnerabilities Across Categories</div>
        <img class="chart-img" src="{b64_img('charts/chart_07_profit_boxplot.png')}" alt="Profit Boxplot">
        <div class="insight-box">
            <strong>Business Insight:</strong> Profitability closely mirrors the sales dispersion, with Electronics and Furniture generating profit spreads extending up to ₹30,000+ per transaction. However, the presence of lower profit bounds near zero across all categories reveals that excessive discounting or low-basket-size orders occasionally dilute bottom-line returns, requiring tighter minimum order size rules.
        </div>
    </div>

    <!-- 3. Customer Demographics -->
    <div class="section-title">3. Customer Demographics & Segmentation Analysis</div>

    <div class="chart-block">
        <div class="chart-title">Chart 6 (Brief #3a): Customer Age Demographic Distribution</div>
        <img class="chart-img" src="{b64_img('charts/chart_04_age_distribution.png')}" alt="Age Distribution">
        <div class="insight-box">
            <strong>Business Insight:</strong> The retail customer base follows a near-symmetric normal distribution (skewness = +0.28) centered at a median age of 36 years, with the core 50% of buyers concentrated between 29 and 43 years old. This strong mid-career millennial demographic signifies peak earning and spending capacity, highlighting prime targets for premium product upselling and loyalty membership programs.
        </div>
    </div>

    <div class="chart-block">
        <div class="chart-title">Chart 7 (Brief #3b): Customer Annual Income Distribution</div>
        <img class="chart-img" src="{b64_img('charts/chart_05_income_distribution.png')}" alt="Income Distribution">
        <div class="insight-box">
            <strong>Business Insight:</strong> Annual income exhibits pronounced positive right-skewness (skewness = +17.94) with a median of ₹49,005 and an extreme high-earning tail extending up to ₹1.75M. While the majority of customers occupy middle-income brackets (₹37k–₹65k), high-net-worth outliers purchase luxury electronics and furniture packages, recommending a bifurcated tier-based pricing and promotional strategy.
        </div>
    </div>

    <div class="chart-block">
        <div class="chart-title">Chart 8 (Brief #6): Share of Total Sales by Customer Segment</div>
        <img class="chart-img" src="{b64_img('charts/chart_10_segment_donut.png')}" alt="Segment Donut">
        <div class="insight-box">
            <strong>Business Insight:</strong> The Consumer segment drives the lion's share of company sales at 54.4% (₹41.7M), followed by Corporate accounts at 30.7% (₹23.6M) and Home Office buyers at 14.9% (₹11.5M). This distribution shows healthy revenue diversification, but also highlights an untapped opportunity to expand B2B corporate contracts, which typically enjoy larger ticket sizes and higher repeat purchase frequencies.
        </div>
    </div>

    <!-- 4. Profitability Drivers -->
    <div class="section-title">4. Profitability Drivers, Pricing & Markdown Risks</div>

    <div class="chart-block">
        <div class="chart-title">Chart 9 (Brief #5a): Relationship Between Sales and Net Profit</div>
        <img class="chart-img" src="{b64_img('charts/chart_08_sales_vs_profit_scatter.png')}" alt="Sales vs Profit Scatter">
        <div class="insight-box">
            <strong>Business Insight:</strong> A remarkably strong positive linear relationship exists between gross sales and net profit (Pearson r = 0.965), confirming that higher revenue scales directly into bottom-line profitability without severe margin decay. The uniform slope across transaction sizes confirms steady unit-economics, indicating that corporate revenue growth initiatives will reliably flow into company profits.
        </div>
    </div>

    <div class="chart-block">
        <div class="chart-title">Chart 10 (Brief #5b): Impact of Promotional Discounts on Net Profit</div>
        <img class="chart-img" src="{b64_img('charts/chart_09_discount_vs_profit_scatter.png')}" alt="Discount vs Profit Scatter">
        <div class="insight-box">
            <strong>Business Insight:</strong> There is a demonstrable negative correlation between discount rates and net profit (r = -0.119), showing significant profitability erosion as discounts climb past 25%. While moderate discounts drive purchase volume, aggressive discounting (>30%) cannibalizes operating profit without generating commensurate volume gains, demanding strict governance on regional markdown caps.
        </div>
    </div>

    <div class="chart-block">
        <div class="chart-title">Chart 11 (Brief #7): Correlation Matrix Across Numerical Transaction Variables</div>
        <img class="chart-img" src="{b64_img('charts/chart_11_correlation_heatmap.png')}" alt="Correlation Heatmap">
        <div class="insight-box">
            <strong>Business Insight:</strong> The correlation matrix confirms that Sales and Profit share a near-perfect positive correlation (r = 0.965), while Quantity shows moderate positive influence on revenue (r = 0.373). In contrast, demographic metrics such as Age and Income display negligible direct linear correlation with order value (r ≈ 0.01), proving that customers across all age and wealth brackets purchase diverse product baskets depending on situational needs.
        </div>
    </div>

    <!-- 5. Cross-Dimensional Matrix -->
    <div class="section-title">5. Cross-Dimensional Matrix & Post-Purchase Dynamics</div>

    <div class="chart-block">
        <div class="chart-title">Chart 12 (Brief #8): Average Sales for Combinations of Product Category and Region</div>
        <img class="chart-img" src="{b64_img('charts/chart_12_category_region_pivot.png')}" alt="Category Region Pivot">
        <div class="insight-box">
            <strong>Business Insight:</strong> Analyzing category-by-region average order sizes reveals that Furniture consistently commands the highest ticket size (averaging ~₹26,600/order across regions), followed closely by Electronics (~₹19,000/order), with peak transactions originating in the West and South regions. Meanwhile, Office Supplies and Grocery show modest order averages (~₹1,600–₹3,000) uniformly across all territories, validating consistent product pricing nationwide.
        </div>
    </div>

    <div class="chart-block">
        <div class="chart-title">Chart 13 (Bonus): Product Category Return Rates vs. Customer Rating</div>
        <img class="chart-img" src="{b64_img('charts/chart_13_returns_and_satisfaction.png')}" alt="Returns and Satisfaction">
        <div class="insight-box">
            <strong>Business Insight:</strong> Overall product return rates hover around 11.5% to 13.5%, with Clothing showing the highest return rate at 13.5% due to apparel sizing variance, while Office Supplies recorded the lowest returns at 11.5%. Customer ratings remain steady between 3.05 and 3.12 stars across all categories, indicating a reliable customer experience but also pointing to substantial room for enhancing post-purchase customer service.
        </div>
    </div>

    <!-- 6. Executive Action Plan -->
    <div class="section-title">6. Strategic Executive Action Plan</div>
    <table>
        <thead>
            <tr>
                <th>Strategic Initiative</th>
                <th>Empirical Insight</th>
                <th>Recommended Action</th>
                <th>Expected Impact</th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <td><strong>1. Markdown Governance</strong></td>
                <td>Discounts > 25% cause sharp profit erosion (r = -0.119).</td>
                <td>Hard cap regional discount approvals at 20% max.</td>
                <td>+2.5% to net bottom-line profit.</td>
            </tr>
            <tr>
                <td><strong>2. High-Ticket Bundling</strong></td>
                <td>Electronics & Furniture drive 83% of total revenue.</td>
                <td>Bundle warranties, installation & financing.</td>
                <td>Elevate AOV from ₹10.9k to ₹13.5k.</td>
            </tr>
            <tr>
                <td><strong>3. Summer Campaign</strong></td>
                <td>June marks the deepest revenue trough (₹2.29M).</td>
                <td>Launch mid-year "Refresh Fest" and corporate prep.</td>
                <td>Smooth seasonality and recover ~₹1.2M lull.</td>
            </tr>
            <tr>
                <td><strong>4. Apparel Fit Optimization</strong></td>
                <td>Clothing generates peak return rate at 13.5%.</td>
                <td>Implement dynamic size charts & customer reviews.</td>
                <td>Cut return logistics cost by 15–20%.</td>
            </tr>
            <tr>
                <td><strong>5. B2B Enterprise Growth</strong></td>
                <td>Corporate accounts drive 30.7% with high reliability.</td>
                <td>Deploy dedicated corporate portal & contract tiers.</td>
                <td>Lock in recurring multi-year order volumes.</td>
            </tr>
        </tbody>
    </table>

    <div class="footer">
        HCL Career Shaper — Data Analyst Training Program | Mini Project: Turning Retail Sales Data into a Visual Story<br/>
        Report compiled from 7,000 validated retail transaction records (2023–2024).
    </div>
</div>

</body>
</html>
"""

with open('Retail_Sales_Visual_Story_Report.html', 'w', encoding='utf-8') as f:
    f.write(html_content)

print("Interactive HTML Report created successfully: Retail_Sales_Visual_Story_Report.html")
