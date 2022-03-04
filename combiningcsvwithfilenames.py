import csv
from lib2to3.pgen2.token import NEWLINE
import os
import sys
import glob
from numpy import std
import pandas as pd


#number of command line arguments
n = len(sys.argv)

#Adding them in a list
arguments=[]
for i in range(1, n):
    arguments.append(sys.argv[i])

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

with open("temporary.csv", 'r') as csvfile:
    datareader = csv.reader(csvfile)
    for row in datareader:
        writer = csv.writer(sys.stdout)
        writer.writerow(row)
         





    
  



