import pandas as pd
from openpyxl import load_workbook
df = pd.DataFrame(
    dict(AAA=[4, 5, 6, 6], BBB=[10, 25, 30, 40], CCC=[100, 50, -30, -50]))
df2 = pd.DataFrame(
    dict(CCC=[4, 5, 6, 6], BBB=[10, 21, 30, 40], AAA=[100, 50, -30, -50]))
print(df)
print(df2)
print(df -df2)
# print(df *df2)
# print(df /df2)
# print(df -+df2)