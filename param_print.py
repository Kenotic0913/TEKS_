import pickle
import os
import pprint
import re

reporting_cat = ' '
data_file_list = []
file_names = []
file_index = 1

for files in os.walk('C:/TEKS_api/pickle'):
    for filename in files[2]:
        file_names.append(filename)
        data_file_list.append(files[0] + '/' + filename)

file_name = file_names[1]
print(file_name)
print(file_name[0:file_name.find('_')])

def set_params(item, file_name):
    tac_chapter = file_name[0:file_name.find('_')]
    academic_subject = file_name[file_name.find('_')+1:file_name.find('.')]
    item_type = item_item_type
    reporting_category = reporting_cat
    teks_number = tac_teks_num[1:]
    teks_text = item['abbreviatedStatement']
    grade_levels = item['educationLevel']
    TEA_last_updated = item['lastChangeDateTime']

    if tac_chapter == '111':
        regex = r'(\.\D\.)'
        aware_teks_display = re.sub(regex, '.', item['humanCodingScheme'][1:])
        return (tac_chapter, academic_subject, item_type, reporting_category, teks_number, aware_teks_display, teks_text, grade_levels, TEA_last_updated)

    else:
        pass

data = pickle.load(open('C:/TEKS_api/pickle/111_Math.p', 'rb'))

for i, item in enumerate(data['CFItems']):
    if item['educationLevel'] == '05':
        if  item['CFItemType'] == 'Strand':
            item_item_type = 'Strand'
            rctext = item['abbreviatedStatement']
            reporting_cat = rctext[0:rctext.find('.')]
            tac_teks_num = item['humanCodingScheme']
            params = set_params(item, file_names[file_index])
            pprint.pprint(params)

        elif item['CFItemType'] == 'Student Expectation':
            item_item_type = 'Student Expectation'
            tac_teks_num = item['humanCodingScheme']
            params = set_params(item, file_names[file_index])
            pprint.pprint(params)

        else:
            continue
    else:
        continue
