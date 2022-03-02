import os
import sys
import glob
import pandas as pd

#total number of arguments
n = len(sys.argv)
print("Total arguments passed:", n)

#Checking all arguments passed and storing in a list
print("\nArguments passed:", end = " ")
arguments=[]
files_collection=[]
combined_dataframe = []
for i in range(1, n):
    print(sys.argv[i], end = " ")
    arguments.append(sys.argv[i])


for i in arguments:
    path=arguments[i]
    print(path)

files_collection = glob.glob(os.path.join(path, "*.csv"))

for file in files_collection:
    df = pd.read_csv(file, sep=',')
    df['filename'] = file.split('/')[-1]
    combined_dataframe.append(df)



master_df = pd.concat(combined_dataframe, ignore_index=True, sort=True)

#Saving df as csv
master_df.to_csv('Master.csv', index=False)


