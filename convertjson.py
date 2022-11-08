import json
import pandas as pd
import pprint as pp
import cost_code as cc

sov_map = pd.read_excel('./data/SOV Map.xlsx')
cmic = pd.read_excel('./data/Period 5 Export 05.19.22.xlsx')
cc_sheet = pd.read_excel('./data/M007 - Cost Code Sheet 2022-05-16 - Markup.xlsx')


sov_dic = {}
for x in range(sov_map.shape[0]):
    cc = sov_map.loc[x,'Cost Code']
    if cc not in sov_dic:
        sov_dic[cc] = {
            'Area': {},
        }
    

    sov_dic[cc]['Area'][sov_map.loc[x,'Area']] = sov_map.iloc[x,7]

with open('./data/prod.json') as f:
    prod_data = json.load(f)

j = []
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

# print(len(d),len(sov_dic))
# print(cmic['Bill Code'])

for index, bill_code in enumerate(cmic['Bill Code']):
    eng = ''
    for index2, code in enumerate(cc_sheet.iloc[:,2]):
        if code == bill_code[5:12]:
            eng = cc_sheet.iloc[index2,1]

    j.append({
        'bill_code': bill_code,
        'phase_code': bill_code[5:12],
        'name': cmic['Name'].loc[index],
        'engineer': eng,
        'category': cmic['Category'].loc[index],
        'uom': cmic['Output WM Code'].loc[index],
        'forecast_qty': cmic['Output Projected Qty'].loc[index],
        'forecast_mhs': cmic['Input Projected Qty'].loc[index],
        'current_qty': cmic['Output Completed Qty'].loc[index],
        'current_mhs': cmic['Input Completed Qty'].loc[index],
        'projected_forecast': cmic['Projected Cost Forecast'].loc[index],
        'spent_to_date': cmic['Actual Cost'].loc[index],
        'committed': cmic['Spent/Committed Total'].loc[index],
        'areas': None
    })

for cc_obj in j:
    cc = cc_obj['phase_code']
    if cc_obj['category'] == 'L' and cc_obj['phase_code'] in sov_dic:
        cc_obj['areas'] = []
        for area in sov_dic[cc]['Area']:
            eb_id = None
            for index2, code in enumerate(cc_sheet.iloc[:,2]):
                if code == cc and cc_sheet.iloc[index2,3] == area:
                    ebid = cc_sheet.iloc[index2,0]


            cc_obj['areas'].append({
                'name': area,
                'eb_id': ebid,
                'forecast_qty': sov_dic[cc]['Area'][area],
                'forecast_mhs': round(cc_obj['forecast_mhs']*(sov_dic[cc]['Area'][area]/cc_obj['forecast_qty']),2) if cc_obj['forecast_qty'] !=0 else 0,
                'current_qty': prod_data[cc][area]['qty'],
                'current_mhs': prod_data[cc][area]['mhs'],
            })
        
    

# print(cmic.columns)

f = filter(lambda x: x['engineer']=='Ksenofon', j)
for s in f:
    pp.pprint(s['phase_code'])

# pp.pprint(sov_dic)
# pp.pprint(prod_data)

# print(sov_dic['33-3100']['Area'])
# print(prod_data['33-3100'])


# print(cc_sheet.iloc[4,1])
# print(cc_sheet.iloc[4,2])
# print(cc_sheet.iloc[:,1])
# print(cc_sheet.iloc[:,2])

# pp.pprint(j)



# with open('ccdb.json', 'w') as f:
#     json.dump(j, f, indent=4)

