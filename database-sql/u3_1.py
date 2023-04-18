import pandas
from openpyxl import Workbook  # для чтения таблицы
# OpenPyXL поддерживает новые форматы MS Excel (.xlsx) 

exelDataDF = pandas.read_excel('flowers.xlsx', sheet_name='winter')
print(exelDataDF)