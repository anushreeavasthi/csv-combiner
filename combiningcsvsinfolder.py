from asyncio.windows_events import NULL
import csv
import os
import sys
import glob
from numpy import std
import pandas as pd


def combine_pdf (input,output):
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
    status=0
    if(master_df.empty):
         status=0
    else:
        master_df.to_csv(output,index=False)
        status=1
    return(status)


combine_pdf(sys.argv[1],"temp.csv")


with open("temp.csv", 'r', newline=None) as csvfile:
    datareader = csv.reader(csvfile)
    for row in datareader:
         tsv_writer = csv.writer(sys.stdout)
         tsv_writer.writerow(row)


    
  



