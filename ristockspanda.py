import pandas as pd
from openpyxl import Workbook

wb = Workbook()
ws = wb.active
ws = wb.create_sheet("variance") #An empty sheet

excel_file = 'ripublic.xls' #We load data from an excel file with last year's earnings
quarters = 'Sep_2018','Jun_2018','Mar_2018', 'Dec_2017'
ripublic1 = pd.read_excel(excel_file, names = quarters, index_col= 'ID' )

excel_file2 = 'ripublic2.xls' #This file was slightly altered on purpose from the original
ripublic2 = pd.read_excel(excel_file2, names = quarters, index_col= 'ID')

ripubliccsv = 'ripublic2.csv' # same data but from a CSV format
csvdata = pd.read_csv(ripubliccsv)
print(csvdata) # Let's see what CSV looks like

dupedri = (ripublic1 + ripublic1) #Here I've duplicated the data for comparison to the original list
print(dupedri)

print(ripublic2) # The altered list
recon = (ripublic2 - ripublic1)
print(recon) #Let see the differences
recon2 = ((ripublic2 - ripublic1)*10100000)
print(recon2) #Let see the differences

variance = recon.loc[(recon!=0).any(axis=1)] #you could also use column
print(variance)

writer1 = pd.ExcelWriter('recon.xlsx')
recon.to_excel(writer1)
writer1.save()
writer = pd.ExcelWriter('output.xlsx')

variance.to_excel(writer)
writer.save()
writer3 = pd.ExcelWriter('dupeddata.xlsx')
dupedri.to_excel(writer3)
writer3.save()

exceptions = pd.ExcelWriter('exceptions.xlsx')
variance.to_excel(exceptions)
exceptions.save()

first = ripublic1.iloc[0]
print(first)

second = ripublic1.iloc[1]
print(second)

third = ripublic1.iloc[2]
print(third)

fourth = ripublic1.iloc[3]
print(fourth)