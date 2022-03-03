import csv
import os
import sys
import glob
from numpy import std
import pandas as pd



#Mentioning the source directory as a command line argument
source_dir= str(input)
path = source_dir
files_collection = glob.glob(os.path.join(path, "*.csv"))
combined_dataframe = []
for file in files_collection:
    df = pd.read_csv(file, sep=',')
    df['filename'] = file.split('/')[-1]
    combined_dataframe.append(df)
master_df = pd.concat(combined_dataframe, ignore_index=True, sort=True)
files_collection = glob.glob(os.path.join(path, "*.csv"))
combined_dataframe = []
for file in files_collection:
    df = pd.read_csv(file, sep=',')
    df['filename'] = file.split('/')[-1]
    combined_dataframe.append(df)
master_df = pd.concat(combined_dataframe, ignore_index=True, sort=True)
master_df.to_csv("temporary.csv",index=False)


with open("temp.csv", 'r') as csvfile:
    datareader = csv.reader(csvfile)
    for row in datareader:
        print(row)


    
  



