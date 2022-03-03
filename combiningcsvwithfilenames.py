import csv
import os
import sys
import glob
from numpy import std
import pandas as pd


#number of command line arguments
n = len(sys.argv)
print("Total arguments passed:", n)

#Adding them in a list
arguments=[]
for i in range(1, n):
    arguments.append(sys.argv[i])

print(arguments)

#Parsing them as a list
combined_dataframe=[]
for i in range(0,len(arguments)):
    source_dir= arguments[i]
    path = source_dir
    file = os.path.join(path)
    df = pd.read_csv(file, sep=',')
    df['filename'] = file.split('/')[-1]
    combined_dataframe.append(df)
    master_df = pd.concat(combined_dataframe, ignore_index=True, sort=True)


master_df.to_csv("temporary.csv",index=False)





    
  



