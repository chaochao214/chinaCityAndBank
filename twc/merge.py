import pandas as pd;
import xlsxwriter;



data1 = pd.read_excel('C:/Users/Administrator/Desktop/全国银行excel/ori01.xls',encoding = 'utf-8')
data2 = pd.read_excel('C:/Users/Administrator/Desktop/全国银行excel/ori02.xls',encoding = 'utf-8')
all_data =pd.merge(data1,data2,left_on='code',right_on='code',how='left')
all_data.to_excel('result.xlsx',engine='xlsxwriter')