
import os
import argparse
import subprocess
import pandas as pd

cols = ['profileUrl','free.fr','free.fr_reversed','free.fr_reversed_stickform','free.fr_stickform','fullName,fullname_with_points','fullname_with_points2','fullname_with_points3','fullname_with_points4','fullname_with_points4_stickform','fullnames_reversed','fullnames_reversed_stickform','gmail.com','gmail.com_reversed','gmail.com_reversed_stickform','gmail.com_stickform','hotmail.fr','hotmail.fr_reversed','hotmail.fr_reversed_stickform','hotmail.fr_stickform','icloud.com','icloud.com_reversed','icloud.com_reversed_stickform','icloud.com_stickform','icloud.fr','icloud.fr_reversed','icloud.fr_reversed_stickform','icloud.fr_stickform','id,imgUrl','isPrivate','isVerified','orange.fr','orange.fr_reversed','orange.fr_reversed_stickform','orange.fr_stickform','outlook.fr','outlook.fr_reversed','outlook.fr_reversed_stickform','outlook.fr_stickform','query','sfr.fr','sfr.fr_reversed','sfr.fr_reversed_stickform','sfr.fr_stickform','timestamp','username']
df = pd.DataFrame(data=None, index=cols).T

def create():
    global df
    current_cwd = args.current_cd
    command = f"cmd /c mkdir result, batch, process_speed, processed, data"
    proc = subprocess.Popen(command,  cwd=current_cwd, shell=True, stdout=subprocess.PIPE) # creationflags=subprocess.CREATE_NEW_CONSOLE
    print(os.listdir())
    lod = args.current_cd+'\\'+'processed'+'\\'+'processed_df'+'.csv'
    df.to_csv(lod, index=False)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='A test program.')
    parser.add_argument("-f", "--current_cd", help="working dir to start.")
    args = parser.parse_args()
    create()