#1. Read from multiple csv files with same structure from /src folder in your m/c

from pathlib import Path

for name in Path('src').iterdir():
    if name.match('*.csv'):
        with open(name) as csv_file:
            csv_content = csv_file.read()
            print(csv_content)
