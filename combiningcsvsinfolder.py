import os
import sys
import glob
import pandas as pd

#Mentioning the source directory as a command line argument
source_dir= str(sys.argv[1])

#Passing path to the source directory
path = source_dir

#Creating a parser for all files in the folder which end with .csv
files_collection = glob.glob(os.path.join(path, "*.csv"))

combined_dataframe = []
for file in files_collection:
    df = pd.read_csv(file, sep=',')
    df['filename'] = file.split('/')[-1]
    combined_dataframe.append(df)
  
master_df = pd.concat(combined_dataframe, ignore_index=True, sort=True)

#Saving df as csv
master_df.to_csv("temporary.csv", index=False)



