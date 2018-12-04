import pickle
import sqlite3
import os
import pprint
import pyodbc

#Setup database cursor in order for script to interact with SQL databse
sqlcnxn = pyodbc.connect('DSN=datawarehouse_ODS_CPS_STAGING')

cursor = sqlcnxn.cursor()

#OPTIONAL: Setup sqlite database cursor to test script in a safe environment
# cnxn = sqlite3.connect('testdb.sqlite')
# cursor = cnxn.cursor()

#Delete target table if it already exists, and then recreate it fresh for data entry.
cursor.execute("IF OBJECT_ID('DAT.TEKS') IS NOT NULL DROP TABLE DAT.TEKS;")
sqlcnxn.commit()
#cnxn.commit()

cursor.execute("""CREATE TABLE DAT.TEKS (
                    row_id INT IDENTITY(1,1)
                    ,tac_chapter INT NULL
                    ,academic_subject VARCHAR(200) NULL
                    ,item_type VARCHAR(100) NULL
                    ,reporting_category NVARCHAR(MAX) NULL
                    ,teks_number VARCHAR(75) NULL
                    ,teks_text NVARCHAR(MAX) NULL
                    ,grade_levels VARCHAR(50) NULL
                    ,TEA_last_updated DATE NULL);""")
sqlcnxn.commit()
#cnxn.commit()

#List of Global Variables for use in below function and loops.
reporting_cat = ' '
data_file_list = []
file_names = []
file_index = -1
sql = """INSERT INTO DAT.TEKS (
                   tac_chapter
                   ,academic_subject
                   ,item_type
                   ,reporting_category
                   ,teks_number
                   ,teks_text
                   ,grade_levels
                   ,TEA_last_updated
                ) VALUES (
                   ?
                   ,?
                   ,?
                   ,?
                   ,?
                   ,?
                   ,?
                   ,?
                );"""

#Creates lists of file paths and names to point loops at data sources
for files in os.walk('C:/TEKS_api/pickle'):
    for filename in files[2]:
        file_names.append(filename)
        data_file_list.append(files[0] + '/' + filename)

#Function to set appropriate parameters for each SQL insert statement
def set_params(item, file_name):
    tac_chapter = file_name[0:file_name.find('_')]
    academic_subject = file_name[file_name.find('_')+1:file_name.find('.')]
    item_type = item_item_type
    reporting_category = reporting_cat
    teks_number = tac_teks_num[1:]
    teks_text = item['abbreviatedStatement']
    grade_levels = item['educationLevel']
    TEA_last_updated = item['lastChangeDateTime']
    return (tac_chapter, academic_subject, item_type, reporting_category, teks_number, teks_text, grade_levels, TEA_last_updated)

#Loop that opens a data file, looks through it item-by-item, and then inserts the desired content into a SQL table
for file in data_file_list:
    data = pickle.load(open(f'{file}', 'rb'))
    file_index += 1
    for i, item in enumerate(data['CFItems']):

        if  item['CFItemType'] == 'Strand':
            item_item_type = 'Strand'
            rctext = item['abbreviatedStatement']
            reporting_cat = rctext[0:rctext.find('.')]
            tac_teks_num = item['humanCodingScheme']
            params = set_params(item, file_names[file_index])
            #pprint.pprint(params)
            cursor.execute(sql, params)

        elif item['CFItemType'] == 'Student Expectation':
            item_item_type = 'Student Expectation'
            tac_teks_num = item['humanCodingScheme']
            params = set_params(item, file_names[file_index])
            #pprint.pprint(params)
            cursor.execute(sql, params)

        else:
            continue

sqlcnxn.commit()
#cnxn.commit()
