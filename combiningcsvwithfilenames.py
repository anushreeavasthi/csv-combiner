import csv
from lib2to3.pgen2.token import NEWLINE
import os
import sys
import glob
from numpy import std
import pandas as pd


def combine_files(input,output):
    #number of command line arguments
    n = len(sys.argv)
    #Adding them in a list
    arguments=[]
    for i in range(1, n):
        arguments.append(sys.argv[i])
    #Parsing them as a list and combining in a dataframe
    combined_dataframe=[]
    for i in range(0,len(arguments)):
        source_dir= arguments[i]
        path = source_dir
        file = os.path.join(path)
        df = pd.read_csv(file, sep=',')
        df['filename'] = file.split('/')[-1]
        combined_dataframe.append(df)
        master_df = pd.concat(combined_dataframe, ignore_index=True, sort=True)
    #Converting the combined dataframe to a temporary csv file
    status=0
    if(master_df.empty):
         status=0
    else:
        master_df.to_csv(output,index=False)
        status=1
    return(status)




if __name__=="__main__":
    #Calling combine_files based on command line argument location of files and storing in a temporary safe file
    combine_files(sys.argv,"temporary.csv")
    #Writing output of temporary file to the output file mentioned by user.
    with open("temporary.csv", 'r', newline=None) as csvfile:
        datareader = csv.reader(csvfile)
        for row in datareader:
            tsv_writer = csv.writer(sys.stdout)
            tsv_writer.writerow(row)
