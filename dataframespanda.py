import pandas as pd
import xlrd
excel_file = 'movies.xls'
movies = pd.read_excel(excel_file)
print(movies.head())
movies_sheet1 = pd.read_excel(excel_file, sheet_name=0, index_col=0)
print(movies_sheet1.head())
movies_sheet2 = pd.read_excel(excel_file, sheet_name=1, index_col=0)
print(movies_sheet2.head())
movies_sheet3 = pd.read_excel(excel_file, sheet_name=2, index_col=0)
print(movies_sheet3.head())
movies2 = pd.concat([movies_sheet1, movies_sheet2, movies_sheet3])
print(movies.shape)
print(movies2.tail())