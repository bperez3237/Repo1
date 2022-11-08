
import xlsxwriter as xl
import pandas as pd
from datetime import date
import pprint as pp
import json

cost_rprt_xls = pd.ExcelFile(r'C:\Users\bperez\Iovino Enterprises, LLC\M007-NYCHA-Coney Island Sites - Documents\General\08 - BUDGET & COST\Cost Codes\Contract Forecasting Spreadsheet\Period 7 Export 07.07.22.xlsx')
cost_rprt = pd.read_excel(cost_rprt_xls)

sov_map_xls = pd.ExcelFile(r'C:\Users\bperez\SOV Map.xlsx')
sov_map = pd.read_excel(sov_map_xls)


sov_dic = {}
for x in range(sov_map.shape[0]):
    cc = sov_map.loc[x,'Cost Code']
    if cc not in sov_dic:
        sov_dic[cc] = {
            'Area': {},
        }
    

    sov_dic[cc]['Area'][sov_map.loc[x,'Area']] = sov_map.iloc[x,7]




spent = 'Actual Cost'
commited = 'Spent/Committed Total'
pm_forecast = 'Projected Cost Forecast'
b_mhs = 'Input Projected Qty'
b_qty = 'Output Projected Qty'
c_mhs = 'Input Completed Qty'
c_qty = 'Output Completed Qty'
uom = 'Output WM Code'


cc_dic = {}
for x in range(cost_rprt.shape[0]):
    cc_dic[cost_rprt.loc[x,'Phase']] = 0



# j = {}
# for code in sov_dic:
#     for area in sov_dic[code]['Area'].keys():
#         if code not in j:
#             j[code] = {area: {'qty':0,'mhs':0}}
#         else:
#             j[code][area] = {
#                 'qty': 0,
#                 'mhs': 0
#             }

# with open('prod.json', 'w') as f:
#     json.dump(j, f, indent=4)


with open('prod.json') as f:
    d = json.load(f)

# pp.pprint(d)


workbook = xl.Workbook('Cost Codes '+str(date.today())+'.xlsx')
ws = workbook.add_worksheet('Code Codes')

title_format = workbook.add_format(
        {'bold': True,
        'font_size': 12}
    )

heading_format = workbook.add_format( 
        {'bold': True,
        'font_color': 'white',
        'bg_color': '#366092',
        'center_across': True,
        'text_wrap': True,
        'valign': 'vcenter',
        'border': 2}
    )

body_format_string1 = workbook.add_format(
    {'bg_color': 'white',
    'border': 1}
    )
body_format_num1 = workbook.add_format(
    {'bg_color': 'white', 
    'border': 1,
    'num_format': '_(* #,##0.00_);_(* (#,##0.00);_(* "-"??_);_(@_)'}
    )
body_format_curr1 = workbook.add_format(
    {'bg_color': 'white', 
    'border': 1,
    'num_format': '_($* #,##0.00_);_($* (#,##0.00);_($* "-"??_);_(@_)'}
    )


color1 = '#D9D9D9'

body_format_string2 = workbook.add_format(
    {'bg_color': color1,
    'border': 1}
    )
body_format_num2 = workbook.add_format(
    {'bg_color': color1,
    'border': 1,
    'num_format': '_(* #,##0.00_);_(* (#,##0.00);_(* "-"??_);_(@_)'}
    )
body_format_curr2 = workbook.add_format(
    {'bg_color': color1,
    'border': 1,
    'num_format': '_($* #,##0.00_);_($* (#,##0.00);_($* "-"??_);_(@_)'}
    )

color2 = '#DCE6F1'

body_format_string3 = workbook.add_format(
    {'bg_color': color2,
    'border': 1}
    )
body_format_num3 = workbook.add_format(
    {'bg_color': color2,
    'border': 1,
    'num_format': '_(* #,##0.00_);_(* (#,##0.00);_(* "-"??_);_(@_)'}
    )
body_format_curr3 = workbook.add_format(
    {'bg_color': color2,
    'border': 1,
    'num_format': '_($* #,##0.00_);_($* (#,##0.00);_($* "-"??_);_(@_)'}
    )

    
total_col = 6
mh_col = 10
table_row = 4
cat_col = 13



#SETUP TITLES AND COLUMNS
ws.write('A1','M007 - GR1904063 - Coney Island Sites', title_format)

ws.merge_range('E1:F1', 'Contract Value', heading_format)
ws.write('G1', 187311891.5, body_format_curr1)
ws.merge_range('E2:F2', 'Projected Cost', heading_format)
ws.merge_range('J1:K1', 'Total Mhs', heading_format)
ws.merge_range('J2:K2', 'Mhs to Date', heading_format)

ws.merge_range('N3:S3', 'Category Total', heading_format) 


ws.write(table_row,0, 'Code', heading_format)
ws.write(table_row,1, 'Name', heading_format)
ws.write(table_row,2, 'Qty', heading_format)
ws.write(table_row,3, 'UOM', heading_format)
ws.write(table_row,4, 'Mhs', heading_format)
ws.write(table_row,5, 'Qty/MH', heading_format)
ws.write(table_row,6, 'Projected Forecast', heading_format)

ws.write(table_row,8, 'Spent to Date', heading_format)
ws.write(table_row,9, 'Committed to Date', heading_format)
ws.write(table_row,10, 'Qty to Date', heading_format)
ws.write(table_row,11, 'Mhs to Date', heading_format)

ws.write(table_row,13, 'Labor', heading_format)
ws.write(table_row,14, 'Subcontract', heading_format)
ws.write(table_row,15, 'Consumable', heading_format)
ws.write(table_row,16, 'Permanent Material', heading_format)
ws.write(table_row,17, 'Equipment', heading_format)
ws.write(table_row,18, 'Other', heading_format)


#---------------------------------add Data to sheet --------------------------------------------

counter = 0
color_counter = 0
for code in cc_dic:

    if (color_counter%2 == 0):
        row_format_string = body_format_string1
        row_format_num = body_format_num1
        row_format_curr = body_format_curr1
    else:
        row_format_string = body_format_string2
        row_format_num = body_format_num2
        row_format_curr = body_format_curr2


    ws.write(table_row + 1 + counter, 0, str(code), row_format_string)
    code_df = cost_rprt[cost_rprt['Phase'] == code]
    inds = code_df.index
    l_ind, s_ind, c_ind, m_ind, e_ind = 'NA','NA','NA','NA','NA'

    for ind in inds:
        if (cost_rprt['Category'].iloc[ind] == 'L') | (cost_rprt['Category'].iloc[ind] == 'LAB'):
            l_ind = ind
            
        if (cost_rprt['Category'].iloc[ind] == 'S'):
            s_ind = ind
            
        if (cost_rprt['Category'].iloc[ind] == 'C'):
            c_ind = ind
            
        if (cost_rprt['Category'].iloc[ind] == 'M'):
            m_ind = ind
            
        if (cost_rprt['Category'].iloc[ind] == 'E'):
            e_ind = ind


    n = code_df['Name'].iloc[0]
    budget_qty = 0
    unit = 'NA'
    budget_mhs = 0
    current_qty = 0
    current_mhs = 0
    if (l_ind != 'NA'):
        budget_qty = cost_rprt[b_qty].iloc[l_ind]
        unit = cost_rprt[uom].iloc[l_ind]
        budget_mhs = cost_rprt[b_mhs].iloc[l_ind]
        current_qty = cost_rprt[c_qty].iloc[l_ind]
        current_mhs = cost_rprt[c_mhs].iloc[l_ind]

    prod = 1
    if budget_mhs != 0:
        prod = budget_qty/budget_mhs

    forecast = 0
    for x in code_df[pm_forecast]:
        forecast += x

    spent_to_date = 0
    for x in code_df[spent]:
        spent_to_date += x
    
    commit = 0
    for x in code_df[commited]:
        commit += x
        
    
    l_cat = 0
    if (l_ind != 'NA'):
        l_cat = code_df[pm_forecast].loc[l_ind]
    s_cat = 0
    if (s_ind != 'NA'):
        s_cat = code_df[pm_forecast].loc[s_ind]
    c_cat = 0
    if (c_ind != 'NA'):
        c_cat = code_df[pm_forecast].loc[c_ind]
    m_cat = 0
    if (m_ind != 'NA'):
        m_cat = code_df[pm_forecast].loc[m_ind]
    e_cat = 0
    if (e_ind != 'NA'):
        e_cat = code_df[pm_forecast].loc[e_ind]
    other_cat = forecast - l_cat - s_cat - c_cat - m_cat - e_cat

    
    ws.write(table_row + 1 + counter,1, str(n), row_format_string)
    ws.write(table_row + 1 + counter,2, budget_qty, row_format_num)
    ws.write(table_row + 1 + counter,3, str(unit), row_format_string)
    ws.write(table_row + 1 + counter,4, budget_mhs, row_format_num)
    ws.write(table_row + 1 + counter,5, prod, row_format_num)
    ws.write(table_row + 1 + counter,6, forecast, row_format_curr)

    ws.write(table_row + 1 + counter,8, spent_to_date, row_format_curr)
    ws.write(table_row + 1 + counter,9, commit, row_format_curr)
    ws.write(table_row + 1 + counter,10, current_qty, row_format_num)
    ws.write(table_row + 1 + counter,11, current_mhs, row_format_num)

    ws.write(table_row + 1 + counter,13, l_cat, row_format_curr)
    ws.write(table_row + 1 + counter,14, s_cat, row_format_curr)
    ws.write(table_row + 1 + counter,15, c_cat, row_format_curr)
    ws.write(table_row + 1 + counter,16, m_cat, row_format_curr)
    ws.write(table_row + 1 + counter,17, e_cat, row_format_curr)
    ws.write(table_row + 1 + counter,18, other_cat, row_format_curr)

    if code in sov_dic:
        for area in sov_dic[code]['Area'].keys():
            counter += 1
            area_qty = sov_dic[code]['Area'][area]

            ratio = 0
            if (budget_qty != 0 and area_qty != 0):
                ratio = (area_qty/budget_qty)
            labor_rate = 0
            if current_mhs != 0:
                labor_rate = float(spent_to_date)/float(current_mhs)

            ws.write(table_row + 1 + counter, 0, code, body_format_string3)
            ws.write(table_row + 1 + counter, 1, str(area), body_format_string3)
            ws.write(table_row + 1 + counter, 2, area_qty, body_format_num3)
            ws.write(table_row + 1 + counter, 3, str(unit), body_format_string3)
            ws.write(table_row + 1 + counter, 4, 0, body_format_num3)
            ws.write(table_row + 1 + counter, 5, 0, body_format_num3)
            ws.write(table_row + 1 + counter, 6, 0, body_format_curr3)

            ws.write(table_row + 1 + counter, 8, d[code][area]['qty']*labor_rate/prod, body_format_curr3)
            ws.write(table_row + 1 + counter, 9, 0, body_format_curr3)
            ws.write(table_row + 1 + counter, 10, d[code][area]['qty'], body_format_num3)
            ws.write(table_row + 1 + counter, 11, d[code][area]['qty']/prod, body_format_num3)

            ws.write(table_row + 1 + counter, 13, 0, body_format_curr3)
            ws.write(table_row + 1 + counter, 14, 0, body_format_curr3)
            ws.write(table_row + 1 + counter, 15, 0, body_format_curr3)
            ws.write(table_row + 1 + counter, 16, 0, body_format_curr3)
            ws.write(table_row + 1 + counter, 17, 0, body_format_curr3)
            ws.write(table_row + 1 + counter, 18, 0, body_format_curr3)

            ws.set_row(table_row + 1 + counter, None, None, {'level':1, 'hidden': True})


    counter += 1
    color_counter += 1
    

ws.write('G2', f"=SUM(G{table_row+2}:G{counter+5})", body_format_curr1)
ws.write('L1', f"=SUM(E{table_row+2}:E{counter+5})", body_format_num1)
ws.write('L2', f"=SUM(L{table_row+2}:L{counter+5})", body_format_num1)



ws.write('N4', f'=SUM(N{table_row+2}:N{counter+5})', body_format_curr1)
ws.write('O4', f'=SUM(O{table_row+2}:O{counter+5})', body_format_curr1)
ws.write('P4', f'=SUM(P{table_row+2}:P{counter+5})', body_format_curr1)
ws.write('Q4', f'=SUM(Q{table_row+2}:Q{counter+5})', body_format_curr1)
ws.write('R4', f'=SUM(R{table_row+2}:R{counter+5})', body_format_curr1)
ws.write('S4', f'=SUM(S{table_row+2}:S{counter+5})', body_format_curr1)


ws.set_column(1,1 ,45)
ws.set_column(2,2 ,14)
ws.set_column(3,3 ,5)
ws.set_column(4,5 ,11.5)
ws.set_column(6,6 ,17.5)

ws.set_column(7,7 ,2.5)

ws.set_column(8,9 ,16.5)
ws.set_column(10,11 ,14)

ws.set_column(12,12 ,2.5)

ws.set_column(13,18 ,20)



workbook.close()