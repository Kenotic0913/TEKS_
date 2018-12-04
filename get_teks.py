import requests
import json
import pickle
from pathlib import Path

CFPackage_links = {
                    '110_English': 'https://teks-api.texasgateway.org/ims/case/v1p0/CFPackages/c22d9405-c1f7-51e6-9883-b3c807e67e6c'
                   ,'111_Math': 'https://teks-api.texasgateway.org/ims/case/v1p0/CFPackages/bc997e24-7f3b-5df0-a0cd-3a8ac9cf0e2e'
                   ,'112_Science': 'https://teks-api.texasgateway.org/ims/case/v1p0/CFPackages/2ccca18f-b9cf-5710-8e66-13be2b1b71ba'
                   ,'113_Humanities': 'https://teks-api.texasgateway.org/ims/case/v1p0/CFPackages/a5db260d-f0b9-5315-9adb-6b41f7e18947'
                   ,'114_Languages_Other_Than_English': 'https://teks-api.texasgateway.org/ims/case/v1p0/CFPackages/f72881dd-9796-57da-a12a-f649e03f4c92'
                   ,'115_Health': 'https://teks-api.texasgateway.org/ims/case/v1p0/CFPackages/a22d0672-8316-5eec-b72e-a3664b091c41'
                   ,'116_Phys_Ed': 'https://teks-api.texasgateway.org/ims/case/v1p0/CFPackages/09876a91-a9a1-50a8-a99f-6a1dd0435b91'
                   ,'117_Art': 'https://teks-api.texasgateway.org/ims/case/v1p0/CFPackages/13fce3da-d993-5a21-9beb-c7958e9345c7'
                   ,'118_Economics': 'https://teks-api.texasgateway.org/ims/case/v1p0/CFPackages/11a9d541-3f03-552d-a03c-064e92f7325c'
                   ,'126_Technology': 'https://teks-api.texasgateway.org/ims/case/v1p0/CFPackages/0b4fa3a5-934a-586a-b300-8a56d0cf0a3d'
                   ,'127_Career_Dev': 'https://teks-api.texasgateway.org/ims/case/v1p0/CFPackages/f9132300-bcc2-502d-b181-cb289bd4024c'
                   ,'128_Spanish_Language_Arts': 'https://teks-api.texasgateway.org/ims/case/v1p0/CFPackages/927efa98-1add-5134-8b15-c5c988cf4d7e'
                   ,'130_CTE': 'https://teks-api.texasgateway.org/ims/case/v1p0/CFPackages/bcca35a9-269a-54aa-ac3b-2883e7ab9f1f'
                   ,'PreK_PreK': 'https://teks-api.texasgateway.org/ims/case/v1p0/CFPackages/bb580de0-2a00-5612-b3a2-26a419dfedd1'
                  }

datadir_path = Path.home() / 'C:/TEKS_api/pickle'

for file in datadir_path.glob('*.p'):
    if file.is_file() == True:
        print(f'removing {file}')
        file.unlink()
    else:
        print('No Files in Directory')

for x in CFPackage_links:
    r = requests.get(CFPackage_links[x])
    data = r.json()
    with open(f'pickle/{x}.p', 'wb') as f:
        pickle.dump(data, f)
