# 1. Read from multiple files with same structure /src folder in your m/c
# 2. load into a single file with same structure /tgt folder in your m/c
# 3. Convert the single csv file to a parquet format in /tgt folder in your m/c
import glob

for file_ext in ['src/*.txt', 'src/*.dat']:
    for filename in glob.glob(file_ext):
        print(filename)
