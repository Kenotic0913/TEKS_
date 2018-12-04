import pyodbc
import csv

sqlcnxn = pyodbc.connect('DSN=datawarehouse_ODS_CPS')
cursor = sqlcnxn.cursor()

ela_path = 'C:/TEKS_api/TEKS_crosswalk/ELA_import.csv'
hist_path ='C:/TEKS_api/TEKS_crosswalk/History_import.csv'
math_path = 'C:/TEKS_api/TEKS_crosswalk/Math_import.csv'


data = []
with open(ela_path, 'r') as csvfile:
    reader = csv.reader(csvfile, delimiter = ',')
    for i, row in enumerate(reader):
        if i > 0:
            data.append(row)

with open(hist_path, 'r') as csvfile:
    reader = csv.reader(csvfile, delimiter = ',')
    for i, row in enumerate(reader):
        if i > 0:
            data.append(row)

with open(math_path, 'r') as csvfile:
    reader = csv.reader(csvfile, delimiter = ',')
    for i, row in enumerate(reader):
        if i > 0:
            data.append(row)

table_create = """CREATE TABLE DAT.aware_teks_lookup (
                    row_id BIGINT NULL
                    ,teks_id BIGINT NULL
                    );"""

cursor.execute(table_create)
sqlcnxn.commit()


table_insertion = f"""INSERT INTO DAT.aware_teks_lookup (
                                row_id
                                ,teks_id
                                ) VALUES (
                                ?
                                ,?);"""
                                

for row in data:
    cursor.execute(table_insertion, row)
    sqlcnxn.commit()
