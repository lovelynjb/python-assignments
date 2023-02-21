# 1.Read a list of files stored in a manifest file in a src/ folder in your local m/c
# 2. load the files into a single file a target folder
# 3.Move the files available in source folder and missing in manifest file
# to a /reject folder in your m/c
from pathlib import Path


def writeFile(manifest_content):
    with open('src/dest_manifest.txt', 'a') as dest_manifest_file:
        dest_manifest_file.write(manifest_content)


for name in Path('src').iterdir():
    if name.match('*.manifest'):
        with open(name) as manifest_file:
            manifest_content = manifest_file.read()
            print(manifest_content)

            writeFile(manifest_content)
