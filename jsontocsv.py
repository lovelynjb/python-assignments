# 7.Read from a json file and flatten into a csv file
from pathlib import Path
import json
import pandas as pd
#from pandas.io.json import json_normalize

with open('src/customer-data.json','r') as json_file:
    json_content = json.load(json_file)
    df = pd.json_normalize(json_content)
    print(df.columns)
    df.to_csv('target.csv', index=False)
