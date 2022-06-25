# Import libraries
import requests
from bs4 import BeautifulSoup
import pandas as pd
from openpyxl import Workbook
url = 'https://www.moneycontrol.com/stocks/marketstats/nsemact1/index.php'
page = requests.get(url)
#print(page)
data = pd.read_html(url)
table = data[0]
#print(table)
#soup = BeautifulSoup(page.text, 'lxml')
#print(soup)
#table1 = soup.find('table', id='data_table_ajax_loading')
#print(table1)
#table.to_excel('pandas_to_excel_no_index_header.xlsx', index=False, header=False)
table.to_excel("output.xlsx", sheet_name='Sheet_name_1')  