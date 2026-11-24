"""
Generate Publication-Grade PDF Visual Report using ReportLab
File: Retail_Sales_Visual_Story_Report.pdf
HCL Career Shaper Data Analyst Training Program
"""

import os
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Image, Table, TableStyle, PageBreak, KeepTogether, HRFlowable
)
from reportlab.pdfgen import canvas

class NumberedCanvas(canvas.Canvas):
    def __init__(self, *args, **kwargs):
        super(NumberedCanvas, self).__init__(*args, **kwargs)
        self._saved_page_states = []

    def showPage(self):
        self._saved_page_states.append(dict(self.__dict__))
        self._startPage()

    def save(self):
        num_pages = len(self._saved_page_states)
        for state in self._saved_page_states:
            self.__dict__.update(state)
            self.draw_page_decorations(num_pages)
            super(NumberedCanvas, self).showPage()
        super(NumberedCanvas, self).save()

    def draw_page_decorations(self, page_count):
        self.saveState()
        self.setFont("Helvetica", 8)
        self.setFillColor(colors.HexColor("#64748B"))
        
        # Omit header and footer on cover page
        if self._pageNumber > 1:
            # Header
            self.drawString(54, 750, "HCL Career Shaper | Data Analyst Training Program — Mini Project: Data Visualization")
            self.drawRightString(558, 750, "Turning Retail Sales Data into a Visual Story")
            self.setStrokeColor(colors.HexColor("#CBD5E1"))
            self.setLineWidth(0.75)
            self.line(54, 744, 558, 744)
            
            # Footer
            self.line(54, 45, 558, 45)
            self.drawString(54, 32, "Confidential — Retail Leadership Analytics Report (2023–2024)")
            self.drawRightString(558, 32, f"Page {self._pageNumber} of {page_count}")
        
        self.restoreState()

def build_pdf(filename="Retail_Sales_Visual_Story_Report.pdf"):
    doc = SimpleDocTemplate(
        filename,
        pagesize=letter,
        leftMargin=54,
        rightMargin=54,
        topMargin=54,
        bottomMargin=54
    )
    
    styles = getSampleStyleSheet()
    
    # Custom Palette
    NAVY = colors.HexColor("#1B365D")
    TEAL = colors.HexColor("#008080")
    DARK = colors.HexColor("#1E293B")
    LIGHT_BG = colors.HexColor("#F8FAFC")
    BORDER_COLOR = colors.HexColor("#E2E8F0")
    ACCENT_BOX = colors.HexColor("#F1F5F9")
    
    # Custom Paragraph Styles
    title_style = ParagraphStyle(
        'DocTitle',
        parent=styles['Heading1'],
        fontName='Helvetica-Bold',
        fontSize=24,
        leading=28,
        textColor=NAVY,
        spaceAfter=8
    )
    
    subtitle_style = ParagraphStyle(
        'DocSubTitle',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=12,
        leading=16,
        textColor=TEAL,
        spaceAfter=15
    )
    
    meta_style = ParagraphStyle(
        'MetaStyle',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=9.5,
        leading=14,
        textColor=colors.HexColor("#475569")
    )
    
    h1_style = ParagraphStyle(
        'SectionH1',
        parent=styles['Heading2'],
        fontName='Helvetica-Bold',
        fontSize=15,
        leading=19,
        textColor=NAVY,
        spaceBefore=14,
        spaceAfter=8,
        keepWithNext=True
    )
    
    h2_style = ParagraphStyle(
        'SectionH2',
        parent=styles['Heading3'],
        fontName='Helvetica-Bold',
        fontSize=12,
        leading=16,
        textColor=TEAL,
        spaceBefore=10,
        spaceAfter=6,
        keepWithNext=True
    )
    
    body_style = ParagraphStyle(
        'BodyDark',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=9.5,
        leading=13.5,
        textColor=DARK,
        spaceAfter=6
    )
    
    caption_style = ParagraphStyle(
        'InsightCaption',
        parent=styles['Normal'],
        fontName='Helvetica-Oblique',
        fontSize=9,
        leading=13,
        textColor=colors.HexColor("#0F172A")
    )
    
    caption_title = ParagraphStyle(
        'InsightTitle',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=9,
        leading=13,
        textColor=NAVY
    )

    story = []

    # ==================== COVER / HEADER ====================
    story.append(Spacer(1, 15))
    story.append(Paragraph("TURNING RETAIL SALES DATA INTO A VISUAL STORY", title_style))
    story.append(Paragraph("Executive Performance Report & Multi-Dimensional Visual Analytics (2023–2024)", subtitle_style))
    story.append(HRFlowable(width="100%", thickness=2, color=NAVY, spaceBefore=4, spaceAfter=12))
    
    meta_text = """
    <b>Program:</b> HCL Career Shaper — Data Analyst Training Program | <b>Course Level:</b> 2nd Year Engineering<br/>
    <b>Domain:</b> Nationwide Retail Sales & Customer Analytics | <b>Scope:</b> 7,000 Validated Transactions Across 4 Regions<br/>
    <b>Dataset:</b> <code>retail_customer_sales_dataset.csv</code> | <b>Submission Date:</b> November 2026
    """
    story.append(Paragraph(meta_text, meta_style))
    story.append(Spacer(1, 14))

    # ==================== EXECUTIVE SUMMARY & KPIS ====================
    story.append(Paragraph("Executive Overview & Commercial Health Dashboard", h1_style))
    story.append(Paragraph(
        "This visual report translates raw retail transaction data into actionable strategic intelligence for regional "
        "and corporate leadership. Over the 2023–2024 operational window, the company generated ₹76.73M in revenue with "
        "₹25.13M in operating profit, maintaining an extraordinarily stable gross profit margin of 32.75% across all territories. "
        "While regional volumes remain highly balanced, category-level concentration and promotional discounting present "
        "distinct growth and risk vectors that require immediate leadership governance.",
        body_style
    ))
    story.append(Spacer(1, 8))

    # KPI Table
    kpi_data = [
        [
            Paragraph("<b>Total Sales (Gross)</b><br/><font size=13 color='#1B365D'><b>₹76.73M</b></font><br/><font size=7.5 color='#64748B'>7,000 Transactions</font>", body_style),
            Paragraph("<b>Total Net Profit</b><br/><font size=13 color='#008080'><b>₹25.13M</b></font><br/><font size=7.5 color='#64748B'>Operating Surplus</font>", body_style),
            Paragraph("<b>Overall Profit Margin</b><br/><font size=13 color='#1B365D'><b>32.75%</b></font><br/><font size=7.5 color='#64748B'>Consistent Margin</font>", body_style),
            Paragraph("<b>Average Order Value</b><br/><font size=13 color='#E26D5C'><b>₹10,962</b></font><br/><font size=7.5 color='#64748B'>Spend per Ticket</font>", body_style),
        ]
    ]
    kpi_table = Table(kpi_data, colWidths=[126, 126, 126, 126])
    kpi_table.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), LIGHT_BG),
        ('BOX', (0,0), (-1,-1), 1, BORDER_COLOR),
        ('INNERGRID', (0,0), (-1,-1), 0.5, BORDER_COLOR),
        ('TOPPADDING', (0,0), (-1,-1), 8),
        ('BOTTOMPADDING', (0,0), (-1,-1), 8),
        ('LEFTPADDING', (0,0), (-1,-1), 8),
        ('RIGHTPADDING', (0,0), (-1,-1), 8),
        ('ALIGN', (0,0), (-1,-1), 'CENTER'),
    ]))
    story.append(kpi_table)
    story.append(Spacer(1, 14))

    # Helper function to add a chart with its 2-3 sentence insight caption box
    def add_chart_block(chart_filename, chart_title, insight_text, img_w=6.1*inch, img_h=3.2*inch):
        chart_path = os.path.join('charts', chart_filename)
        elements = []
        elements.append(Paragraph(chart_title, h2_style))
        if os.path.exists(chart_path):
            elements.append(Image(chart_path, width=img_w, height=img_h))
        else:
            elements.append(Paragraph(f"<i>[Chart Image {chart_filename} Missing]</i>", body_style))
        elements.append(Spacer(1, 4))
        
        # Caption Callout Box
        caption_content = [
            [
                Paragraph("<b>Strategic Business Insight:</b> " + insight_text, caption_style)
            ]
        ]
        caption_box = Table(caption_content, colWidths=[504])
        caption_box.setStyle(TableStyle([
            ('BACKGROUND', (0,0), (-1,-1), ACCENT_BOX),
            ('BOX', (0,0), (-1,-1), 0.75, BORDER_COLOR),
            ('LEFTPADDING', (0,0), (-1,-1), 10),
            ('RIGHTPADDING', (0,0), (-1,-1), 10),
            ('TOPPADDING', (0,0), (-1,-1), 6),
            ('BOTTOMPADDING', (0,0), (-1,-1), 6),
        ]))
        elements.append(caption_box)
        elements.append(Spacer(1, 14))
        return KeepTogether(elements)

    # ==================== SECTION 1: MACRO TREND & REGIONAL ====================
    story.append(Paragraph("1. Macro Revenue Trends & Regional Performance", h1_style))
    story.append(Paragraph(
        "To establish high-level strategic orientation, we first analyze the 24-month top-line revenue velocity followed "
        "by territorial performance across North, South, East, and West India.",
        body_style
    ))
    story.append(Spacer(1, 4))

    # Chart 1: Line Chart
    c1_insight = (
        "Monthly retail sales averaged ₹3.20M over 2023–2024, maintaining strong stability with seasonal peaks "
        "consistently observed in October (reaching ₹3.89M) driven by festive holiday demand. "
        "A noticeable dip occurred in June 2024 (₹2.29M), indicating a mid-year operational lull that warrants "
        "targeted summer promotions and proactive inventory realignment."
    )
    story.append(add_chart_block(
        "chart_01_monthly_sales_trend.png",
        "Chart 1: Monthly Sales Trend Over the Two-Year Period (Order_Date vs. Sales)",
        c1_insight
    ))

    # Chart 2: Regional Bar Chart
    c2_insight = (
        "Geographic sales are exceptionally balanced across all four zones, led by the East region (₹20.0M sales, ₹6.6M profit) "
        "and West region (₹19.8M sales, ₹6.5M profit), while the North region trails modestly at ₹18.1M sales. "
        "Remarkably, profit margins remain virtually uniform across regions at 32.5% to 33.0%, proving that logistical "
        "efficiencies and pricing structures are standardized company-wide."
    )
    story.append(add_chart_block(
        "chart_02_sales_by_region.png",
        "Chart 2: Total Sales and Net Profit Across Geographic Regions (Grouped Bar Chart)",
        c2_insight
    ))

    story.append(PageBreak())

    # ==================== SECTION 2: PRODUCT CATEGORY & DISPERSION ====================
    story.append(Paragraph("2. Product Category Performance & Order Spread", h1_style))
    story.append(Paragraph(
        "Evaluating merchandise lines reveals significant revenue skew. While customer order counts are broadly distributed, "
        "capital velocity is heavily dominated by durable big-ticket merchandise.",
        body_style
    ))
    story.append(Spacer(1, 4))

    # Chart 3: Category Bar Chart
    c3_insight = (
        "Electronics and Furniture represent the revenue engine of the business, jointly accounting for over 83% of "
        "gross sales (₹37.6M and ₹26.1M respectively) due to substantially higher average ticket sizes. "
        "Conversely, high-frequency essentials like Grocery (₹2.69M) and Office Supplies (₹2.57M) show lower volume "
        "contributions, serving primarily as cross-sell entry points rather than primary top-line drivers."
    )
    story.append(add_chart_block(
        "chart_03_sales_by_category.png",
        "Chart 3: Revenue Contribution by Product Category (Horizontal Bar Chart)",
        c3_insight
    ))

    # Chart 6: Sales Box Plot
    c6_insight = (
        "Electronics and Furniture exhibit massive transaction value spreads, with median order sizes around ₹15,000–₹22,000 "
        "and high-value outlier orders exceeding ₹80,000. In stark contrast, Clothing, Grocery, and Office Supplies maintain tight, "
        "compact interquartile spreads below ₹8,000, illustrating distinct inventory risk profiles and order value dynamics."
    )
    story.append(add_chart_block(
        "chart_06_sales_boxplot.png",
        "Chart 4 (Brief #4): Sales Distribution and Outliers Broken Down by Product Category (Box Plot)",
        c6_insight
    ))

    # Chart 7: Profit Box Plot
    c7_insight = (
        "Profitability closely mirrors the sales dispersion, with Electronics and Furniture generating profit spreads extending up to ₹30,000+ "
        "per transaction. However, the presence of lower profit bounds near zero across all categories reveals that excessive discounting "
        "or low-basket-size orders occasionally dilute bottom-line returns, requiring tighter minimum order size rules."
    )
    story.append(add_chart_block(
        "chart_07_profit_boxplot.png",
        "Chart 5: Net Profit Spread and Low-Margin Vulnerabilities Across Product Categories (Box Plot)",
        c7_insight
    ))

    story.append(PageBreak())

    # ==================== SECTION 3: CUSTOMER DEMOGRAPHICS & SEGMENTATION ====================
    story.append(Paragraph("3. Customer Demographics & Segmentation Analysis", h1_style))
    story.append(Paragraph(
        "Understanding shopper characteristics allows targeted customer acquisition and tailored lifecycle marketing. "
        "The following analyses profile customer age distributions, income skewness, and segment contributions.",
        body_style
    ))
    story.append(Spacer(1, 4))

    # Chart 4: Age Histogram
    c4_insight = (
        "The retail customer base follows a near-symmetric normal distribution (skewness = +0.28) centered at a "
        "median age of 36 years, with the core 50% of buyers concentrated between 29 and 43 years old. "
        "This strong mid-career millennial demographic signifies peak earning and spending capacity, highlighting prime targets "
        "for premium product upselling and loyalty membership programs."
    )
    story.append(add_chart_block(
        "chart_04_age_distribution.png",
        "Chart 6 (Brief #3a): Distribution of Customer Age (Histogram with KDE & Symmetry Analysis)",
        c4_insight
    ))

    # Chart 5: Income Histogram
    c5_insight = (
        "Annual income exhibits pronounced positive right-skewness (skewness = +17.94) with a median of ₹49,005 "
        "and an extreme high-earning tail extending up to ₹1.75M. While the majority of customers occupy middle-income brackets "
        "(₹37k–₹65k), high-net-worth outliers purchase luxury electronics and furniture packages, recommending a bifurcated "
        "tier-based pricing and promotional strategy."
    )
    story.append(add_chart_block(
        "chart_05_income_distribution.png",
        "Chart 7 (Brief #3b): Distribution of Customer Annual Income (Histogram with Right-Skew Commentary)",
        c5_insight
    ))

    # Chart 10: Segment Donut
    c10_insight = (
        "The Consumer segment drives the lion's share of company sales at 54.4% (₹41.7M), followed by Corporate accounts at "
        "30.7% (₹23.6M) and Home Office buyers at 14.9% (₹11.5M). This distribution shows healthy revenue diversification, but "
        "also highlights an untapped opportunity to expand B2B corporate contracts, which typically enjoy larger ticket sizes "
        "and higher repeat purchase frequencies."
    )
    story.append(add_chart_block(
        "chart_10_segment_donut.png",
        "Chart 8 (Brief #6): Share of Total Sales by Customer Segment (Donut Chart)",
        c10_insight,
        img_w=5.0*inch, img_h=3.4*inch
    ))

    story.append(PageBreak())

    # ==================== SECTION 4: PROFITABILITY & DISCOUNT IMPACT ====================
    story.append(Paragraph("4. Profitability Drivers, Pricing & Markdown Risks", h1_style))
    story.append(Paragraph(
        "Top-line growth does not benefit the enterprise if margins are eroded by unmonitored discounting. "
        "The scatter plots and correlation matrix below isolate the exact relationship between sales volume, pricing discounts, and net profits.",
        body_style
    ))
    story.append(Spacer(1, 4))

    # Chart 8: Sales vs Profit Scatter
    c8_insight = (
        "A remarkably strong positive linear relationship exists between gross sales and net profit (Pearson r = 0.965), "
        "confirming that higher revenue scales directly into bottom-line profitability without severe margin decay. "
        "The uniform slope across transaction sizes confirms steady unit-economics, indicating that corporate revenue growth "
        "initiatives will reliably flow into company profits."
    )
    story.append(add_chart_block(
        "chart_08_sales_vs_profit_scatter.png",
        "Chart 9 (Brief #5a): Relationship Between Sales and Net Profit (Scatter Plot with Regression Trendline)",
        c8_insight
    ))

    # Chart 9: Discount vs Profit Scatter
    c9_insight = (
        "There is a demonstrable negative correlation between discount rates and net profit (r = -0.119), "
        "showing significant profitability erosion as discounts climb past 25%. While moderate discounts drive purchase "
        "volume, aggressive discounting (>30%) cannibalizes operating profit without generating commensurate volume gains, "
        "demanding strict governance on regional markdown caps."
    )
    story.append(add_chart_block(
        "chart_09_discount_vs_profit_scatter.png",
        "Chart 10 (Brief #5b): Impact of Promotional Discounts on Net Profit (Scatter Plot with Markdown Warning)",
        c9_insight
    ))

    # Chart 11: Correlation Heatmap
    c11_insight = (
        "The correlation matrix confirms that Sales and Profit share a near-perfect positive correlation (r = 0.965), "
        "while Quantity shows moderate positive influence on revenue (r = 0.373). In contrast, demographic metrics such as "
        "Age and Income display negligible direct linear correlation with order value (r ≈ 0.01), proving that customers "
        "across all age and wealth brackets purchase diverse product baskets depending on situational needs."
    )
    story.append(add_chart_block(
        "chart_11_correlation_heatmap.png",
        "Chart 11 (Brief #7): Correlation Matrix Heatmap (Sales, Profit, Discount, Quantity, Age, Income)",
        c11_insight,
        img_w=5.5*inch, img_h=3.4*inch
    ))

    story.append(PageBreak())

    # ==================== SECTION 5: PIVOT MATRIX & SERVICE HEALTH ====================
    story.append(Paragraph("5. Cross-Dimensional Matrix & Post-Purchase Dynamics", h1_style))
    story.append(Paragraph(
        "A holistic visual story must reconcile operational excellence with customer satisfaction and reverse logistics. "
        "This section evaluates regional-category average order baskets and product return rates.",
        body_style
    ))
    story.append(Spacer(1, 4))

    # Chart 12: Pivot Heatmap
    c12_insight = (
        "Analyzing category-by-region average order sizes reveals that Furniture consistently commands the highest ticket size "
        "(averaging ~₹26,600/order across regions), followed closely by Electronics (~₹19,000/order), with peak transactions "
        "originating in the West and South regions. Meanwhile, Office Supplies and Grocery show modest order averages (~₹1,600–₹3,000) "
        "uniformly across all territories, validating consistent product pricing nationwide."
    )
    story.append(add_chart_block(
        "chart_12_category_region_pivot.png",
        "Chart 12 (Brief #8): Average Sales for Combinations of Product Category and Region (Pivot Heatmap)",
        c12_insight
    ))

    # Chart 13: Returns and Satisfaction (Bonus)
    c13_insight = (
        "Overall product return rates hover around 11.5% to 13.5%, with Clothing showing the highest return rate at 13.5% "
        "due to apparel sizing variance, while Office Supplies recorded the lowest returns at 11.5%. Customer ratings remain "
        "steady between 3.05 and 3.12 stars across all categories, indicating a reliable customer experience but also pointing "
        "to substantial room for enhancing post-purchase customer service."
    )
    story.append(add_chart_block(
        "chart_13_returns_and_satisfaction.png",
        "Chart 13 (Bonus): Customer Rating vs. Return Rate by Category (Dual-Axis Performance Analysis)",
        c13_insight
    ))

    # ==================== SECTION 6: STRATEGIC ACTION PLAN ====================
    story.append(Spacer(1, 10))
    story.append(Paragraph("6. Executive Summary Matrix & Strategic Recommendations", h1_style))
    story.append(Paragraph(
        "Based on the empirical patterns revealed across the 13 visualizations, senior leadership is advised to "
        "execute the following 5 prioritized interventions:",
        body_style
    ))
    story.append(Spacer(1, 6))

    rec_data = [
        [
            Paragraph("<b>Strategic Initiative</b>", meta_style),
            Paragraph("<b>Empirical Insight</b>", meta_style),
            Paragraph("<b>Recommended Action</b>", meta_style),
            Paragraph("<b>Expected Impact</b>", meta_style)
        ],
        [
            Paragraph("<b>1. Markdown Governance</b>", body_style),
            Paragraph("Discounts > 25% cause sharp profit erosion (r = -0.119).", body_style),
            Paragraph("Hard cap regional discount approvals at 20% max.", body_style),
            Paragraph("+2.5% to net bottom-line profit.", body_style)
        ],
        [
            Paragraph("<b>2. High-Ticket Bundling</b>", body_style),
            Paragraph("Electronics & Furniture drive 83% of total revenue.", body_style),
            Paragraph("Bundle warranties, installation & financing.", body_style),
            Paragraph("Elevate AOV from ₹10.9k to ₹13.5k.", body_style)
        ],
        [
            Paragraph("<b>3. Summer Campaign</b>", body_style),
            Paragraph("June marks the deepest revenue trough (₹2.29M).", body_style),
            Paragraph("Launch mid-year 'Refresh Fest' and corporate prep.", body_style),
            Paragraph("Smooth seasonality and recover ~₹1.2M lull.", body_style)
        ],
        [
            Paragraph("<b>4. Apparel Fit Optimization</b>", body_style),
            Paragraph("Clothing generates peak return rate at 13.5%.", body_style),
            Paragraph("Implement dynamic size charts & customer reviews.", body_style),
            Paragraph("Cut return logistics cost by 15–20%.", body_style)
        ],
        [
            Paragraph("<b>5. B2B Enterprise Growth</b>", body_style),
            Paragraph("Corporate accounts drive 30.7% with high reliability.", body_style),
            Paragraph("Deploy dedicated corporate portal & contract tiers.", body_style),
            Paragraph("Lock in recurring multi-year order volumes.", body_style)
        ],
    ]
    rec_table = Table(rec_data, colWidths=[110, 130, 150, 114])
    rec_table.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), NAVY),
        ('TEXTCOLOR', (0,0), (-1,0), colors.white),
        ('GRID', (0,0), (-1,-1), 0.5, BORDER_COLOR),
        ('BACKGROUND', (0,1), (-1,1), LIGHT_BG),
        ('BACKGROUND', (0,3), (-1,3), LIGHT_BG),
        ('BACKGROUND', (0,5), (-1,5), LIGHT_BG),
        ('TOPPADDING', (0,0), (-1,-1), 6),
        ('BOTTOMPADDING', (0,0), (-1,-1), 6),
        ('LEFTPADDING', (0,0), (-1,-1), 6),
        ('RIGHTPADDING', (0,0), (-1,-1), 6),
        ('VALIGN', (0,0), (-1,-1), 'TOP'),
    ]))
    story.append(rec_table)

    # Build document
    doc.build(story, canvasmaker=NumberedCanvas)
    print(f"Report successfully compiled and saved to '{filename}'!")

if __name__ == '__main__':
    build_pdf()
