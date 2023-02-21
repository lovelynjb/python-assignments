#2. load into a single csv file with same structure to a /tgt folder in your m/c

from pathlib import Path


def writeFile(csv_content):
    with open('src/dest.txt', 'a') as dest_file:
        dest_file.write(csv_content)


for name in Path('src').iterdir():
    if name.match('*.csv'):
        with open(name) as csv_file:
            csv_content = csv_file.read()

            writeFile(csv_content)
