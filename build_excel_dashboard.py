"""
Create formatted Excel Dashboard Workbook: Retail_Sales_Dashboard.xlsx
Includes Clean Data sheet and Executive Dashboard sheet with dynamic formulas.
HCL Career Shaper Data Analyst Training Program
"""

import openpyxl
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
from openpyxl.utils import get_column_letter
import pandas as pd

df = pd.read_csv('cleaned_retail_sales_dataset.csv')
wb = openpyxl.Workbook()

# Sheet 1: Executive Dashboard
ws_dash = wb.active
ws_dash.title = 'Executive_Dashboard'
ws_dash.views.sheetView[0].showGridLines = True

# Sheet 2: Clean Data
ws_data = wb.create_sheet('Clean_Data')
ws_data.views.sheetView[0].showGridLines = True

# Write clean data
headers = list(df.columns)
ws_data.append(headers)

for row in df.values:
    ws_data.append(list(row))

# Style Clean Data header
header_fill = PatternFill(start_color='1B365D', end_color='1B365D', fill_type='solid')
header_font = Font(name='Segoe UI', size=11, bold=True, color='FFFFFF')
for col_idx in range(1, len(headers) + 1):
    cell = ws_data.cell(row=1, column=col_idx)
    cell.fill = header_fill
    cell.font = header_font
    cell.alignment = Alignment(horizontal='center', vertical='center')

# Format columns in Clean_Data
for r in range(2, len(df) + 2):
    ws_data[f'Q{r}'].number_format = '₹#,##0.00'
    ws_data[f'R{r}'].number_format = '₹#,##0.00'
    ws_data[f'S{r}'].number_format = '₹#,##0.00'
    ws_data[f'P{r}'].number_format = '0.0%'

# Adjust column widths in Clean_Data
for col_idx in range(1, len(headers) + 1):
    col_letter = get_column_letter(col_idx)
    ws_data.column_dimensions[col_letter].width = 16

# Dashboard Styles
dash_title_font = Font(name='Segoe UI', size=16, bold=True, color='1B365D')
dash_sub_font = Font(name='Segoe UI', size=10, italic=True, color='4A5568')
section_font = Font(name='Segoe UI', size=12, bold=True, color='1B365D')
kpi_title_font = Font(name='Segoe UI', size=9, bold=True, color='718096')
kpi_val_font = Font(name='Segoe UI', size=16, bold=True, color='1B365D')
kpi_sub_font = Font(name='Segoe UI', size=8, italic=True, color='2E7D32')

kpi_fill = PatternFill(start_color='F8FAFC', end_color='F8FAFC', fill_type='solid')
thin_border = Border(
    left=Side(style='thin', color='CBD5E1'),
    right=Side(style='thin', color='CBD5E1'),
    top=Side(style='thin', color='CBD5E1'),
    bottom=Side(style='thin', color='CBD5E1')
)

ws_dash['A1'] = 'RETAIL SALES EXECUTIVE DASHBOARD (2023–2024)'
ws_dash['A1'].font = dash_title_font
ws_dash['A2'] = 'HCL Career Shaper — Turning Retail Sales Data into a Visual Story'
ws_dash['A2'].font = dash_sub_font

# Top KPI Block
kpis = [
    ('B', 'C', 'TOTAL SALES', '=SUM(Clean_Data!Q2:Q7001)', '₹#,##0.00', 'Gross Revenue'),
    ('D', 'E', 'TOTAL PROFIT', '=SUM(Clean_Data!S2:S7001)', '₹#,##0.00', 'Operating Surplus'),
    ('F', 'G', 'PROFIT MARGIN', '=D5/B5', '0.00%', 'Gross Margin %'),
    ('H', 'I', 'AVG ORDER VALUE', '=AVERAGE(Clean_Data!Q2:Q7001)', '₹#,##0.00', 'Per Transaction'),
    ('J', 'K', 'TOTAL ORDERS', '=COUNTA(Clean_Data!A2:A7001)', '#,##0', 'Orders Completed')
]

for col_l, col_r, label, formula, num_fmt, subtext in kpis:
    ws_dash.merge_cells(f'{col_l}4:{col_r}4')
    ws_dash.merge_cells(f'{col_l}5:{col_r}5')
    ws_dash.merge_cells(f'{col_l}6:{col_r}6')
    
    cell_lbl = ws_dash[f'{col_l}4']
    cell_lbl.value = label
    cell_lbl.font = kpi_title_font
    cell_lbl.alignment = Alignment(horizontal='center', vertical='center')
    
    cell_val = ws_dash[f'{col_l}5']
    cell_val.value = formula
    cell_val.font = kpi_val_font
    cell_val.number_format = num_fmt
    cell_val.alignment = Alignment(horizontal='center', vertical='center')
    
    cell_sub = ws_dash[f'{col_l}6']
    cell_sub.value = subtext
    cell_sub.font = kpi_sub_font
    cell_sub.alignment = Alignment(horizontal='center', vertical='center')
    
    for r in range(4, 7):
        for c in [col_l, col_r]:
            ws_dash[f'{c}{r}'].fill = kpi_fill
            ws_dash[f'{c}{r}'].border = thin_border

# Section: Regional Performance Table
ws_dash['B8'] = 'Geographic Regional Performance'
ws_dash['B8'].font = section_font

reg_headers = ['Region', 'Order Count', 'Total Sales (₹)', 'Total Profit (₹)', 'Profit Margin %']
for idx, h in enumerate(reg_headers, start=2):
    cell = ws_dash.cell(row=9, column=idx)
    cell.value = h
    cell.fill = header_fill
    cell.font = Font(name='Segoe UI', size=10, bold=True, color='FFFFFF')
    cell.alignment = Alignment(horizontal='center')

regions = ['East', 'West', 'South', 'North']
for idx, reg in enumerate(regions, start=10):
    ws_dash.cell(row=idx, column=2, value=reg).font = Font(name='Segoe UI', size=10, bold=True)
    ws_dash.cell(row=idx, column=3, value=f'=COUNTIFS(Clean_Data!H2:H7001, "{reg}")').number_format = '#,##0'
    ws_dash.cell(row=idx, column=4, value=f'=SUMIFS(Clean_Data!Q2:Q7001, Clean_Data!H2:H7001, "{reg}")').number_format = '₹#,##0.00'
    ws_dash.cell(row=idx, column=5, value=f'=SUMIFS(Clean_Data!S2:S7001, Clean_Data!H2:H7001, "{reg}")').number_format = '₹#,##0.00'
    ws_dash.cell(row=idx, column=6, value=f'=E{idx}/D{idx}').number_format = '0.00%'
    for c in range(2, 7):
        ws_dash.cell(row=idx, column=c).border = thin_border

# Section: Product Category Table
ws_dash['B16'] = 'Product Category Contribution'
ws_dash['B16'].font = section_font

cat_headers = ['Product Category', 'Order Count', 'Total Sales (₹)', 'Total Profit (₹)', 'Profit Margin %']
for idx, h in enumerate(cat_headers, start=2):
    cell = ws_dash.cell(row=17, column=idx)
    cell.value = h
    cell.fill = header_fill
    cell.font = Font(name='Segoe UI', size=10, bold=True, color='FFFFFF')
    cell.alignment = Alignment(horizontal='center')

categories = ['Electronics', 'Furniture', 'Clothing', 'Grocery', 'Office Supplies']
for idx, cat in enumerate(categories, start=18):
    ws_dash.cell(row=idx, column=2, value=cat).font = Font(name='Segoe UI', size=10, bold=True)
    ws_dash.cell(row=idx, column=3, value=f'=COUNTIFS(Clean_Data!L2:L7001, "{cat}")').number_format = '#,##0'
    ws_dash.cell(row=idx, column=4, value=f'=SUMIFS(Clean_Data!Q2:Q7001, Clean_Data!L2:L7001, "{cat}")').number_format = '₹#,##0.00'
    ws_dash.cell(row=idx, column=5, value=f'=SUMIFS(Clean_Data!S2:S7001, Clean_Data!L2:L7001, "{cat}")').number_format = '₹#,##0.00'
    ws_dash.cell(row=idx, column=6, value=f'=E{idx}/D{idx}').number_format = '0.00%'
    for c in range(2, 7):
        ws_dash.cell(row=idx, column=c).border = thin_border

# Section: Customer Segment Table
ws_dash['H8'] = 'Customer Segment Contribution'
ws_dash['H8'].font = section_font

seg_headers = ['Customer Segment', 'Order Count', 'Total Sales (₹)', 'Revenue Share %']
for idx, h in enumerate(seg_headers, start=8):
    cell = ws_dash.cell(row=9, column=idx)
    cell.value = h
    cell.fill = header_fill
    cell.font = Font(name='Segoe UI', size=10, bold=True, color='FFFFFF')
    cell.alignment = Alignment(horizontal='center')

segments = ['Consumer', 'Corporate', 'Home Office']
for idx, seg in enumerate(segments, start=10):
    ws_dash.cell(row=idx, column=8, value=seg).font = Font(name='Segoe UI', size=10, bold=True)
    ws_dash.cell(row=idx, column=9, value=f'=COUNTIFS(Clean_Data!K2:K7001, "{seg}")').number_format = '#,##0'
    ws_dash.cell(row=idx, column=10, value=f'=SUMIFS(Clean_Data!Q2:Q7001, Clean_Data!K2:K7001, "{seg}")').number_format = '₹#,##0.00'
    ws_dash.cell(row=idx, column=11, value=f'=J{idx}/B$5').number_format = '0.00%'
    for c in range(8, 12):
        ws_dash.cell(row=idx, column=c).border = thin_border

# Adjust Column Widths for Dashboard
for c in range(1, 13):
    col_letter = get_column_letter(c)
    ws_dash.column_dimensions[col_letter].width = 18

ws_dash.column_dimensions['A'].width = 4
ws_dash.column_dimensions['B'].width = 22
ws_dash.column_dimensions['H'].width = 22

# Save workbook
wb.save('Retail_Sales_Dashboard.xlsx')
print('Excel Dashboard successfully created: Retail_Sales_Dashboard.xlsx')
