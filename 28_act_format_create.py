import csv
import pyodbc
import pprint

with open('act_28_format.csv', 'r') as rd:
    raw_data = rd.read()

pprint.pprint(raw_data)
