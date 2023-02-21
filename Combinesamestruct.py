# 4.1. Read from multiple files with same structure /src folder in your m/c
# 4.2. load into a single file with same structure /tgt folder in your m/c

import glob
def readcontent(file_name):
    with open(file_name) as file:
        return file.read()
def writeMyFile(x, file_ext):
    with open('dest' + file_ext, 'x') as dest_file:
        dest_file.write(x)

for file_ext in ['.txt', '.dat']:
    x = ''
    for filename in glob.glob('src/*' + file_ext):
        x = x + readcontent(filename)
    writeMyFile(x, file_ext)
