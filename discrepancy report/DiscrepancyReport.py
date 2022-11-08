from calendar import week
import pandas as pd
import numpy as np
from datetime import date, timedelta as td, datetime as dt
import pprint as pp
import xlsxwriter as xl

company = 'MLJ'
xls = pd.ExcelFile(r'C:\Users\bperez\Iovino Enterprises, LLC\M007-NYCHA-Coney Island Sites - Documents\General\10 - PROGRESS BILLING\Billing\21 - July 2022\14 - CPR Spreadsheet\MLJ CPR Spreadsheet July 2022.xlsx')

def check_days(df, row):
    '''given dataframe df and row of employee in data frame, returns
    days of the week with discrepancies'''
    discrep_dic = {}

    for x in range(3,10):
        cpr_hours = 0 if pd.isna(df.iloc[row,x]) else df.iloc[row,x]
        ss_hours = 0 if pd.isna(df.iloc[row+1,x]) else df.iloc[row+1,x]
        if cpr_hours != ss_hours:
            discrep_dic[df.columns[x]] = f'{cpr_hours} on the CPR and {ss_hours} on the Sign in Sheets'

    return discrep_dic

report_dic = {}
for sheet in xls.sheet_names:
    cpr_sheet = pd.read_excel(xls, sheet_name= sheet)
    report_dic[sheet] = {}

    if sheet != 'Summary':
        for y in range(cpr_sheet.shape[0]):
            employee = cpr_sheet.iloc[y,1]
            if pd.isna(employee) == False:
                employee_dic = check_days(cpr_sheet,y)
                if employee_dic != {}:
                    for day in employee_dic:
                        if day not in report_dic[sheet]:
                            report_dic[sheet][day] = {}
                            report_dic[sheet][day][employee] = employee_dic[day]
                        else:
                            report_dic[sheet][day][employee] = employee_dic[day]


def discrep_report(report_dic, company):

    wb = xl.Workbook(f'{company} Discrepancies July 2022.xlsx')
    ws = wb.add_worksheet('Discrepancies')
    ws.write(0,0,'Week Ending Date')
    ws.write(0,1,'Day of the Week')
    ws.write(0,2,'Employee Name')
    ws.write(0,3,'Description')
    row = 1
    for week_ending in report_dic:
        ws.write(row,0,week_ending)
        if report_dic[week_ending] != {}:
            for day_of_the_week in report_dic[week_ending]:
                ws.write(row,1,day_of_the_week)
                for employee in report_dic[week_ending][day_of_the_week]:
                    ws.write(row,2,employee)
                    ws.write(row,3,report_dic[week_ending][day_of_the_week][employee])
                    row +=1
                row +=1
        row +=1            
    wb.close()

discrep_report(report_dic, company)
        
