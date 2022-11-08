
import pandas as pd
import numpy as np
from datetime import date, timedelta as td
import pprint as pp

start_date = date(2022, 7, 1)
end_date = date(2022, 7, 24)


xls = pd.ExcelFile(r'C:\Users\bperez\Benefit Cost.xlsx')
data = pd.read_excel(xls).dropna()

# data.columns = data.iloc[0]
# data = data.drop(data.index[0])

data['Date'] = pd.to_datetime(data['Date']).dt.date


emp_dic = {}
for y in range(data.shape[0]):
    if (data.iloc[y,11] <= end_date and data.iloc[y,11] >= start_date):
        name = data.iloc[y,7]
        union = data.iloc[y,5]
        eth = data.iloc[y,8]

        emp_dic[name] = {}
        emp_dic[name]['Union'] = union
        emp_dic[name]['Ethnicity'] = eth



        
labor = 0
mason = 0
op = 0
db = 0
carp = 0
cw = 0 
other = 0
minos = []

for emp in emp_dic:
    if (emp_dic[emp]['Union'] == '731' or emp_dic[emp]['Union'] == '1010'):
        labor += 1
        if (emp_dic[emp]['Ethnicity'] != 'W'):
            minos.append(str(emp)+' '+str(emp_dic[emp]['Ethnicity']))
    elif (emp_dic[emp]['Union'] == '14' or emp_dic[emp]['Union'] == '15'):
        op += 1
        if (emp_dic[emp]['Ethnicity'] != 'W'):
            minos.append(str(emp)+' '+str(emp_dic[emp]['Ethnicity']))
    elif (emp_dic[emp]['Union'] == '1556'):
        db += 1
        if (emp_dic[emp]['Ethnicity'] != 'W'):
            minos.append(str(emp)+' '+str(emp_dic[emp]['Ethnicity']))
    elif (emp_dic[emp]['Union'] == '780' or emp_dic[emp]['Union'] == '79'):
        mason += 1
        if (emp_dic[emp]['Ethnicity'] != 'W'):
            minos.append(str(emp)+' '+str(emp_dic[emp]['Ethnicity']))
    elif (emp_dic[emp]['Union'] == 'CARP'):
        carp += 1
        if (emp_dic[emp]['Ethnicity'] != 'W'):
            minos.append(str(emp)+' '+str(emp_dic[emp]['Ethnicity']))
    elif (emp_dic[emp]['Union'] == 'CWDC'):
        cw += 1
        if (emp_dic[emp]['Ethnicity'] != 'W'):
            minos.append(str(emp)+' '+str(emp_dic[emp]['Ethnicity']))
    else:
        other += 1


# print('db is '+str(db))
# print('lab is '+str(labor))
# print('carp is '+str(carp))
# print('op is '+str(op))
# print('cw is '+str(cw))
print('mason is '+str(mason))
# print('leftover is '+str(other))


# print('total emp',len(emp_dic))
# print('emp total:',len(minos))

# pp.pprint(minos)
# pp.pprint(emp_dic)


counter = 0
for emp in emp_dic:
    # print(emp_dic[emp])
    # if emp_dic[emp]['Ethnicity'] != 'W' and (emp_dic[emp]['Union'] == '731' or emp_dic[emp]['Union'] == '1010'):
    if emp_dic[emp]['Ethnicity'] != 'W' and (emp_dic[emp]['Union'] == '780' or emp_dic[emp]['Union'] == '79'):
    # if emp_dic[emp]['Ethnicity'] != 'W' and (emp_dic[emp]['Union'] == '15' or emp_dic[emp]['Union'] == '14'):
    # if emp_dic[emp]['Ethnicity'] != 'W' and (emp_dic[emp]['Union'] == 'CWDC'):
    # if emp_dic[emp]['Ethnicity'] != 'W' and (emp_dic[emp]['Union'] == '1556'):
    # if emp_dic[emp]['Ethnicity'] != 'W' and (emp_dic[emp]['Union'] == 'CARP'):
        print(emp, ' - ',emp_dic[emp]["Ethnicity"], 'Male')
        counter += 1
    
print(counter)