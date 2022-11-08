
import xlsxwriter as xl
import pandas as pd
from datetime import date
import pprint as pp
import json
from CostCodeSheet import phase_codes

with open('cc_db.json') as f:
    cc_db = json.load(f)


def get_lb():
    xls = pd.ExcelFile(r'C:\Users\bperez\Iovino Enterprises, LLC\M007-NYCHA-Coney Island Sites - Documents\General\08 - BUDGET & COST\Jobcost\Look Ahead Look Back\Look Ahead Look Back 22-06-26.xlsx')
    df = pd.read_excel(xls, sheet_name='Look Back')
    # print(df.shape[0])
    print(df.iloc[1,3])
    pass

def get_activities():
    pass

def filter_eng():
    pass

def write_code(code):
    pass

def write_sheet(wb,ws,person):
    #get codes & hours from lb
    get_lb()
    #get activity descriptions from timesheet
    get_activities()
    #filter codes for engineer for this report
    eng_codes = filter_eng()
    #write in form of activitys to the left, areas/qtys to the right
    #for code of eng_codes, write_code()
    # for code in eng_codes:
    #     write_code(code)



def create_report(person):

    wb = xl.Workbook(f"{person} Update.xlsx")
    ws = wb.add_worksheet('Cost Codes')
    write_sheet(wb,ws,person)


    wb.close()


create_report("BP")