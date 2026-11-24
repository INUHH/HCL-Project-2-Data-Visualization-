"""
Interactive Retail Analytics Dashboard
HCL Career Shaper Data Analyst Training Program
Mini Project: Turning Retail Sales Data into a Visual Story
"""

import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go

# ----------------- PAGE CONFIGURATION -----------------
st.set_page_config(
    page_title="Retail Sales Executive Dashboard",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom Corporate CSS Styling
st.markdown("""
<style>
    .main-header {
        font-size: 26px;
        font-weight: 700;
        color: #1B365D;
        margin-bottom: 2px;
    }
    .sub-header {
        font-size: 14px;
        color: #4A5568;
        margin-bottom: 20px;
    }
    .kpi-card {
        background-color: #FFFFFF;
        border-radius: 8px;
        padding: 16px 20px;
        box-shadow: 0 1px 3px rgba(0,0,0,0.1);
        border-left: 5px solid #1B365D;
    }
    .kpi-title {
        font-size: 13px;
        color: #718096;
        font-weight: 600;
        text-transform: uppercase;
        margin-bottom: 4px;
    }
    .kpi-value {
        font-size: 24px;
        font-weight: 700;
        color: #1A202C;
    }
    .kpi-sub {
        font-size: 12px;
        color: #48BB78;
        margin-top: 4px;
    }
</style>
""", unsafe_allow_html=True)

# ----------------- DATA LOADING & CACHING -----------------
@st.cache_data
def load_data():
    df = pd.read_csv('cleaned_retail_sales_dataset.csv')
    df['Order_Date'] = pd.to_datetime(df['Order_Date'])
    df['Delivery_Date'] = pd.to_datetime(df['Delivery_Date'])
    return df

try:
    df = load_data()
except Exception as e:
    st.error(f"Error loading dataset: {e}. Please ensure 'cleaned_retail_sales_dataset.csv' exists.")
    st.stop()

# ----------------- SIDEBAR FILTERS -----------------
st.sidebar.image("https://img.icons8.com/fluency/96/combo-chart.png", width=64)
st.sidebar.title("🎛️ Filter Controls")
st.sidebar.markdown("Refine transaction views across dimensions:")

# Filter 1: Year
all_years = sorted(df['Year'].unique().tolist())
selected_years = st.sidebar.multiselect("Select Year(s):", all_years, default=all_years)

# Filter 2: Region
all_regions = sorted(df['Region'].dropna().unique().tolist())
selected_regions = st.sidebar.multiselect("Select Region(s):", all_regions, default=all_regions)

# Filter 3: Product Category
all_categories = sorted(df['Product_Category'].unique().tolist())
selected_categories = st.sidebar.multiselect("Select Product Category:", all_categories, default=all_categories)

# Filter 4: Customer Segment
all_segments = sorted(df['Customer_Segment'].unique().tolist())
selected_segments = st.sidebar.multiselect("Select Customer Segment:", all_segments, default=all_segments)

# Filter 5: Discount Range
discount_range = st.sidebar.slider(
    "Discount Range (%)",
    min_value=0.0,
    max_value=50.0,
    value=(0.0, 50.0),
    step=1.0
)

# Apply Filters
filtered_df = df[
    (df['Year'].isin(selected_years)) &
    (df['Region'].isin(selected_regions)) &
    (df['Product_Category'].isin(selected_categories)) &
    (df['Customer_Segment'].isin(selected_segments)) &
    (df['Discount'] >= discount_range[0] / 100.0) &
    (df['Discount'] <= discount_range[1] / 100.0)
]

# ----------------- MAIN DASHBOARD HEADER -----------------
st.markdown('<div class="main-header">📊 Retail Sales Executive Dashboard (2023–2024)</div>', unsafe_allow_html=True)
st.markdown('<div class="sub-header">HCL Career Shaper — Turning Retail Sales Data into a Visual Story | Interactive Decision Platform</div>', unsafe_allow_html=True)

if filtered_df.empty:
    st.warning("⚠️ No transactions match the selected filter criteria. Please broaden your selection.")
    st.stop()

# ----------------- TOP KPI METRICS (4 REQUIRED KPIS) -----------------
total_sales = filtered_df['Sales'].sum()
total_profit = filtered_df['Profit'].sum()
profit_margin = (total_profit / total_sales * 100) if total_sales > 0 else 0
avg_order_value = filtered_df['Sales'].mean()
order_count = len(filtered_df)

col1, col2, col3, col4, col5 = st.columns(5)

with col1:
    st.markdown(f"""
    <div class="kpi-card" style="border-left-color: #1B365D;">
        <div class="kpi-title">Total Sales</div>
        <div class="kpi-value">₹{total_sales/1e6:.2f}M</div>
        <div class="kpi-sub">Gross Revenue</div>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown(f"""
    <div class="kpi-card" style="border-left-color: #008080;">
        <div class="kpi-title">Total Profit</div>
        <div class="kpi-value">₹{total_profit/1e6:.2f}M</div>
        <div class="kpi-sub">Operating Income</div>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown(f"""
    <div class="kpi-card" style="border-left-color: #E26D5C;">
        <div class="kpi-title">Profit Margin</div>
        <div class="kpi-value">{profit_margin:.2f}%</div>
        <div class="kpi-sub">Margin on Sales</div>
    </div>
    """, unsafe_allow_html=True)

with col4:
    st.markdown(f"""
    <div class="kpi-card" style="border-left-color: #ECA72C;">
        <div class="kpi-title">Avg Order Value (AOV)</div>
        <div class="kpi-value">₹{avg_order_value:,.0f}</div>
        <div class="kpi-sub">Per Ticket Spend</div>
    </div>
    """, unsafe_allow_html=True)

with col5:
    st.markdown(f"""
    <div class="kpi-card" style="border-left-color: #4A5568;">
        <div class="kpi-title">Order Volume</div>
        <div class="kpi-value">{order_count:,}</div>
        <div class="kpi-sub">Transactions</div>
    </div>
    """, unsafe_allow_html=True)

st.markdown("<br/>", unsafe_allow_html=True)

# ----------------- TABS FOR DEEP-DIVE ANALYTICS -----------------
tab1, tab2, tab3, tab4, tab5 = st.tabs([
    "📈 Revenue Trends & Regional",
    "📦 Product Category Analysis",
    "👥 Customer Demographics",
    "💰 Pricing & Margin Impact",
    "📋 Raw Data & Export"
])

# ----------------- TAB 1: REVENUE TRENDS & REGIONAL -----------------
with tab1:
    col_t1, col_t2 = st.columns([3, 2])
    
    with col_t1:
        # Monthly Trend Line Chart
        monthly = filtered_df.groupby('Year_Month').agg(
            Sales=('Sales', 'sum'),
            Profit=('Profit', 'sum')
        ).reset_index()
        
        fig_trend = go.Figure()
        fig_trend.add_trace(go.Scatter(
            x=monthly['Year_Month'], y=monthly['Sales'],
            mode='lines+markers', name='Monthly Sales (₹)',
            line=dict(color='#1B365D', width=3),
            marker=dict(size=6)
        ))
        fig_trend.add_trace(go.Scatter(
            x=monthly['Year_Month'], y=monthly['Profit'],
            mode='lines+markers', name='Monthly Profit (₹)',
            line=dict(color='#008080', width=2.5, dash='dash'),
            marker=dict(size=5)
        ))
        fig_trend.update_layout(
            title="<b>Monthly Revenue & Profit Trajectory</b>",
            xaxis_title="Period (Year-Month)",
            yaxis_title="Amount (₹)",
            template="plotly_white",
            legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1),
            hovermode="x unified"
        )
        st.plotly_chart(fig_trend, use_container_width=True)
    
    with col_t2:
        # Regional Bar Chart
        reg_summary = filtered_df.groupby('Region').agg(
            Sales=('Sales', 'sum'),
            Profit=('Profit', 'sum')
        ).reset_index()
        
        fig_reg = go.Figure()
        fig_reg.add_trace(go.Bar(
            x=reg_summary['Region'], y=reg_summary['Sales'],
            name='Sales (₹)', marker_color='#1B365D'
        ))
        fig_reg.add_trace(go.Bar(
            x=reg_summary['Region'], y=reg_summary['Profit'],
            name='Profit (₹)', marker_color='#008080'
        ))
        fig_reg.update_layout(
            title="<b>Sales & Profit Across Regions</b>",
            barmode='group',
            xaxis_title="Region",
            yaxis_title="Amount (₹)",
            template="plotly_white",
            legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1)
        )
        st.plotly_chart(fig_reg, use_container_width=True)

# ----------------- TAB 2: PRODUCT CATEGORY ANALYSIS -----------------
with tab2:
    col_c1, col_c2 = st.columns(2)
    
    with col_c1:
        cat_summary = filtered_df.groupby('Product_Category').agg(
            Sales=('Sales', 'sum'),
            Profit=('Profit', 'sum'),
            Orders=('Transaction_ID', 'count')
        ).sort_values('Sales', ascending=True).reset_index()
        
        fig_cat = px.bar(
            cat_summary, x='Sales', y='Product_Category',
            orientation='h',
            title="<b>Revenue by Product Category</b>",
            labels={'Sales': 'Total Sales (₹)', 'Product_Category': 'Category'},
            color='Sales',
            color_continuous_scale=['#4A5568', '#1B365D']
        )
        fig_cat.update_layout(template="plotly_white", showlegend=False)
        st.plotly_chart(fig_cat, use_container_width=True)
        
    with col_c2:
        # Box plot of category sales distribution
        fig_box = px.box(
            filtered_df, x='Product_Category', y='Sales',
            color='Product_Category',
            title="<b>Sales Spread & Ticket Size Outliers by Category</b>",
            labels={'Sales': 'Order Value (₹)', 'Product_Category': 'Category'}
        )
        fig_box.update_layout(template="plotly_white", showlegend=False)
        st.plotly_chart(fig_box, use_container_width=True)

# ----------------- TAB 3: CUSTOMER DEMOGRAPHICS -----------------
with tab3:
    col_d1, col_d2 = st.columns(2)
    
    with col_d1:
        fig_age = px.histogram(
            filtered_df, x='Age', nbins=25,
            marginal='box',
            title=f"<b>Customer Age Distribution (Median = {filtered_df['Age'].median():.0f} yrs)</b>",
            color_discrete_sequence=['#008080']
        )
        fig_age.update_layout(template="plotly_white")
        st.plotly_chart(fig_age, use_container_width=True)
        
    with col_d2:
        seg_summary = filtered_df.groupby('Customer_Segment')['Sales'].sum().reset_index()
        fig_donut = px.pie(
            seg_summary, values='Sales', names='Customer_Segment',
            hole=0.45,
            title="<b>Sales Contribution by Customer Segment</b>",
            color_discrete_sequence=['#1B365D', '#008080', '#E26D5C']
        )
        fig_donut.update_layout(template="plotly_white")
        st.plotly_chart(fig_donut, use_container_width=True)

# ----------------- TAB 4: PRICING & MARGIN IMPACT -----------------
with tab4:
    col_p1, col_p2 = st.columns(2)
    
    with col_p1:
        sample_df = filtered_df.sample(min(1200, len(filtered_df)), random_state=42)
        fig_scat1 = px.scatter(
            sample_df, x='Sales', y='Profit',
            trendline='ols',
            title="<b>Sales vs. Net Profit (Strong Linear Relationship)</b>",
            labels={'Sales': 'Sales Value (₹)', 'Profit': 'Profit Value (₹)'},
            color_discrete_sequence=['#1B365D'],
            opacity=0.6
        )
        fig_scat1.update_layout(template="plotly_white")
        st.plotly_chart(fig_scat1, use_container_width=True)
        
    with col_p2:
        fig_scat2 = px.scatter(
            sample_df, x='Discount', y='Profit',
            trendline='ols',
            title="<b>Discount Rate vs. Profit (Margin Erosion Past 25%)</b>",
            labels={'Discount': 'Discount Proportion', 'Profit': 'Profit (₹)'},
            color_discrete_sequence=['#E26D5C'],
            opacity=0.6
        )
        fig_scat2.update_layout(template="plotly_white")
        st.plotly_chart(fig_scat2, use_container_width=True)

# ----------------- TAB 5: RAW DATA & EXPORT -----------------
with tab5:
    st.subheader("Filtered Transaction Records")
    st.dataframe(
        filtered_df[['Transaction_ID', 'Customer_ID', 'Order_Date', 'Region', 'State', 'Product_Category', 'Sales', 'Cost', 'Profit', 'Discount', 'Returned']],
        use_container_width=True,
        height=320
    )
    
    csv = filtered_df.to_csv(index=False).encode('utf-8')
    st.download_button(
        label="📥 Download Filtered Dataset as CSV",
        data=csv,
        file_name='filtered_retail_sales.csv',
        mime='text/csv'
    )

st.markdown("---")
st.markdown("<div style='text-align: center; color: #718096; font-size: 12px;'>HCL Career Shaper — Data Analyst Training Program | Mini Project: Turning Retail Sales Data into a Visual Story</div>", unsafe_allow_html=True)
