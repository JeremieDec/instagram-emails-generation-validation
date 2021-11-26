
# coding: utf-8

import pandas as pd
import subprocess
import argparse
import sys
from json.decoder import JSONDecodeError
import os 

# batch processing : cut in pieces; param

filenames_paths = []
current_cwd = os.getcwd()

def dividing():
    global data_c
    global filenames_paths
    v1 = current_cwd+'//'+'data'+'//'+'cleaned_data.csv'
    data_c = pd.read_csv(v1, error_bad_lines=False)
    filenames_paths = []

    # optimize memory for parallel processing (subprocess.popopen)
    domains = ['gmail.com', 'gmail.com_reversed','gmail.com_stickform', 'gmail.com_reversed_stickform', 'orange.fr', 'orange.fr_reversed', 'orange.fr_stickform', 'orange.fr_reversed_stickform', 'profileUrl','username', 'fullName']
    data_c = data_c[domains]

    #print('longeur df %d' %len(data_c))

    if isinstance(len(data_c)/2, float):
        taille_piece = int((len(data_c)+1)/args.n_pieces)
    else:
        taille_piece  = int(len(data_c)/args.n_pieces)
        #print(taille_piece)

    for position_start in range(0,len(data_c), taille_piece):
        #print('starting pos : %d, final pos : %d'  %(position_start, (position_start+taille_piece)))
        batch_number_ = data_c.iloc[position_start:(position_start+taille_piece)]
        filename_batch = current_cwd+'//'+'batch'+'\\'+'batch_number_'+str(position_start)+'.csv'
        batch_number_.to_csv(filename_batch, index=False)
        filenames_paths.append(filename_batch)
    filenames_paths = pd.Series(filenames_paths)
    filenames_paths.to_csv(current_cwd+'//'+'batch'+'\\'+'filenames_paths'+'.csv', index=False)
    print('finish processing !')

def cleaning_processed_df():
    filep =  current_cwd+'//'+'processed'+'//'+'processed_df.csv'
    newproc= pd.read_csv(filep, error_bad_lines=False)
    newproc.to_csv(filep, index=False)

def cleaning_processed_df():
    filep =  current_cwd+'//'+'processed'+'//'+'processed_df.csv'
    newproc= pd.read_csv(filep, error_bad_lines=False)
    newproc.to_csv(filep, index=False)

def batch_processing():
    global filenames_paths
    global commands
    global results
    filenames_paths = pd.read_csv(current_cwd+'//'+'batch'+'//'+'filenames_paths'+'.csv')
    filenames_paths = list(filenames_paths['0'])[args.lower_bound:args.lower_bound+args.n_pieces_to_run]
    commands = []
    results = []
    command = []
    print('le dernier filename %s' %(filenames_paths[-1]))

    for nom_fichier in filenames_paths:
        nom = nom_fichier # current_cwd+'//'+'batch'+'//'+
        print('nom du path %s' %nom)
        print(command)
        file_path_root = current_cwd
        cm = f"""cmd /c "conda activate && python database_requester.py -in {nom} """ # 
        commands.append(cm)

# command a && command b --argument && command c

    procs = [ subprocess.Popen(i,  cwd=current_cwd, shell=True, stdout=subprocess.PIPE) for i in commands ]  # creationflags=subprocess.CREATE_NEW_CONSOLE
    for i in range(0, len(procs)):
        print(procs[i].communicate())


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='A test program.')
    parser.add_argument("-n", "--n_pieces", help="Prints the supplied argument.", type=int)
    parser.add_argument("-lb", "--lower_bound", help="Prints the supplied argument.", type=int)   
    parser.add_argument("-nr", "--n_pieces_to_run", help="Prints the supplied argument.", type=int)
    args = parser.parse_args()
  #  dividing()
  # cleaning_processed_df()
    batch_processing()
