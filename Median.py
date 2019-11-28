from pprint import pprint
import numpy as np
import pandas as pd
import csv
import json 
import requests
from datetime import datetime
from collections import Counter
from datetime import date
from my_dictionary import my_dictionary
from notify_run import Notify
import os
import xlrd
import xlsxwriter
import utils
from openpyxl import load_workbook



def main():
	#main function
	print 'Running median'
	
	#read list of all stock
	ratioList = ['Net Profit Margin(%)','Return on Assets Excluding Revaluations', 'Return On Net Worth(%)', 'Return On Capital Employed(%)', 'Net Interest Income / Total Funds', 'Dividend Yield', 'PE Ratio']
	count = 0
	
	df = utils.readExcel('Ratios.xlsx')
	# Replace the column with the converted values
	df['PE Ratio'] = pd.to_numeric(df['PE Ratio'], errors='coerce')
	df['Net Profit Margin(%)'] = pd.to_numeric(df['Net Profit Margin(%)'], errors='coerce')
	df['Return On Net Worth(%)'] = pd.to_numeric(df['Return On Net Worth(%)'], errors='coerce')
	df['Return On Capital Employed(%)'] = pd.to_numeric(df['Return On Capital Employed(%)'], errors='coerce')
	df['Net Interest Income / Total Funds'] = pd.to_numeric(df['Net Interest Income / Total Funds'], errors='coerce')
	df['Dividend Yield'] = pd.to_numeric(df['Dividend Yield'], errors='coerce')
	df['Return on Assets Excluding Revaluations'] = pd.to_numeric(df['Return on Assets Excluding Revaluations'], errors='coerce')
	
	
	for item in ratioList:
		try:
			# Drop NA values, listing the converted columns explicitly
			#   so NA values in other columns aren't dropped
			df.dropna(subset = ['Net Profit Margin(%)', 'Return On Net Worth(%)', 'Return On Capital Employed(%)', 'Net Interest Income / Total Funds', 'Dividend Yield', 'Return on Assets Excluding Revaluations', 'PE Ratio'])
			df2 = df.groupby(['Industry', 'Year', 'Month'], as_index=False)[item].median()
			df2.to_excel(str(item).replace('/','-')+'.xlsx', sheet_name=str(count))
			print item + " done"
			count = count + 1
		except Exception as e:
			print e 

if __name__ == "__main__":
    main()
	
