import ntpath
import os
import pandas as pd
from pathlib import Path
import csv

master_df = pd.DataFrame()

source_dir= 'fixtures'

filename_list =[]

csv_files = list(Path(source_dir).glob('*.csv'))

for file in csv_files:
        master_df= master_df.append(pd.read_csv(file))
        print(file)
        reader = csv.reader(file)
        lines= len(list(reader))
        print(lines)
        filename_list.append(file)

#master_df['Filename']= filename_list
print(filename_list)
master_df.to_csv('Master_CSV.csv', index=False)
