# 1. Read from multiple files with same structure /src folder in your m/c

import glob

for file_ext in ['src/*.txt', 'src/*.dat']:
    for filename in glob.glob(file_ext):
        print(filename)
