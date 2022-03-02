import os
import sys
import glob
import pandas as pd

#Mentioning the source directory
source_dir= str(sys.argv[1])

print(source_dir)

#total number of arguments
n = len(sys.argv)
print("Total arguments passed:", n)

#Checking all arguments passed
print("\nArguments passed:", end = " ")
for i in range(1, n):
    print(sys.argv[i], end = " ")
