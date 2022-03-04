# csv-combiner
 
 **PMG challenge:** 
Write a command line program that takes several CSV files as arguments. Each CSV file (found in the fixtures directory of this repo) will have the same columns. Your script should output a new CSV file to stdout that contains the rows from each of the inputs along with an additional column that has the filename from which the row came (only the file's basename, not the entire path). Use filename as the header for the additional column.

**Language used:**
The code has been written entirely in Python.

**Features and proposed inputs:**
There are two python files in the repository. 
1. combiningcsvsinfolder.py allows users to specify the location of the folder containing the csv files and combine them in an outsput csv file mentioned by the user. Command line arguments to run the script would look like - **combiningcsvsinfolder.py fixtures > output.csv**
2. combiningcsvwithfilenames.py allows users to enter any number of file locations as inputs and combines them into a csv file with the filename mentioned by the user. Command line argument to run the script would look like - **combiningcsvswithfilenames.py ./fixtures/clothing.csv ./fixtures/accessories.csv > out.csv**
3. Both scripts generate a temporary file in case the output file name mentioned by the user is not inputted in the right format or if there are any other issues in execution of the script. The temporary combined files act as a way to restore the combined data file which can also be used by the user and are constantly updated in each run.

**Limitations:**
1. Given the requirement of the challenge, the scripts can only combine csv files which have the same headers. This code does not include the functionality of adding files in separate sheets in a workbook if different headers are present.
