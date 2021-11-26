from datetime import datetime
import os
import pandas as pd
import argparse
import subprocess
import sys
from pandas.errors import EmptyDataError

dfs = []

def concat():
    global os 
    global dfs
    global current_cwd
    current_cwd = os.getcwd()+'//'+'result'
    os.chdir(current_cwd)
    print(os.listdir())

    for i in os.listdir():
        try:
            if i[-3:] in 'xls':
                dfs.append(pd.read_excel(i))
            elif i[-3:] in 'csv':
                dfs.append(pd.read_csv(i, error_bad_lines=False))
        except EmptyDataError:
            print('empty_dataframe')
            continue
    concats = pd.concat(dfs, axis=0)
    if int(args.duplicates) == 1:
        concats = concats.drop_duplicates(subset=[args.subset])
        concats.to_csv(current_cwd+'//'+'//'+'COMPACT_no_duplicates.csv', index=False, header=False)

    else:
        concats.to_csv(current_cwd+'//'+'//'+'COMPACT.csv', index=False, header=False)


#result = concats.drop_duplicates(subset=['email'])

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='A test program.')
 #  parser.add_argument("-f", "--current_cd", help="Prints the supplied argument.")
    parser.add_argument("-d", "--duplicates", help="Prints the supplied argument.")
    parser.add_argument("-s", "--subset", help="Prints the supplied argument.")
    args = parser.parse_args()
    concat()
