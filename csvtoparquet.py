# 4.3. Convert the single csv file to a parquet format in /tgt folder in your m/c
from pathlib import Path
import pandas as pd

for name in Path('src').iterdir():
    if name.match('*.csv'):
        with open(name) as csv_file:
            # csv_content = csv_file.read()
            # print(csv_content)

            df = pd.read_csv(csv_file)
            df.to_parquet("parquet.txt")
            print(df)
