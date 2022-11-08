from dis import code_info
import xlsxwriter as xl
import pandas as pd
from datetime import date
import pprint as pp
import json
from CostCodeSheet import phase_codes
from formats import *



def get_current_data():
    cost_rprt_xls = pd.ExcelFile(r'C:\Users\bperez\Iovino Enterprises, LLC\M007-NYCHA-Coney Island Sites - Documents\General\08 - BUDGET & COST\Cost Codes\Contract Forecasting Spreadsheet\Period 9 Export 09.08.22.xlsx')
    cost_report_df = pd.read_excel(cost_rprt_xls)
    # new_df = cost_report_df[cost_report_df['Actual Cost'] > cost_report_df['Projected Cost Forecast']*0.5]
    return cost_report_df


def filter_eng(codes_list,person):
    with open('engineer_codes.json') as f:
        eng_codes = json.load(f)

    new_array = []
    for code in eng_codes:
        if eng_codes[code] == person and code in codes_list:
            new_array.append(code)
    
    return new_array

#-----------------------------------------------------------------------------------

def write_sheet(wb,ws,person):

    with open('cc_db.json') as f:
        cc_db = json.load(f)

    cost_report_df = get_current_data()
    codes_list = cost_report_df['Phase'].tolist()
    # codes_list = ['03-1400', '03-2500', '03-6000', '31-1000', '31-1100']
    codes_list = filter_eng(codes_list,person)

    row = 0
    for code in codes_list:
        if code in cc_db:
            row+=1
            # print(cost_report_df[cost_report_df['Phase'] == code]['Name'] == [])
            ws.merge_range(f"A{row}:E{row}", f"Cost Code {code} - {cost_report_df[cost_report_df['Phase'] == code]['Name'].iloc[0]}" , string_format(wb,'#366092',True))
            ws.write_string(row,0,"Area",string_format(wb,'white'))
            ws.write_string(row,1,"Estimated Qty",string_format(wb,'white'))
            ws.write_string(row,2,"Qty to Date",string_format(wb,'white'))
            ws.write_string(row,3,"New Qty to Date",string_format(wb,'white'))
            ws.write_string(row,4,"Percent Complete",string_format(wb,'white'))

            row +=1
            for area in cc_db[code]:
                ws.write(row,0,area,string_format(wb,'white'))
                ws.write(row,1,cc_db[code][area]['forecast_qty'], number_format(wb,'white'))
                ws.write(row,2,cc_db[code][area]['current_qty'], number_format(wb,'white'))
                ws.write(row,3,0, number_format(wb,'white'))
                ws.write(row,4,f"=D{row+1}/B{row+1}", number_format(wb,'white'))
                row+=1

def create_report(person):

    
    wb = xl.Workbook(f"{person} Forecasting Update.xlsx")
    ws = wb.add_worksheet('Cost Codes')
    write_sheet(wb,ws,person)


    wb.close()


create_report("Kurston")