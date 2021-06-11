# Extract Data from Blast Searches

import os
import re
import pandas as pd
import numpy as np

def main():
    results_path = '../DATA/cat_blast_results/'
    found = pd.DataFrame()
    not_found = []
    num_files = len(os.listdir(results_path))
    for file in os.listdir(results_path):
        with open(results_path + file, 'r') as curr_file:
            data = curr_file.read().replace('\n', '')
            if data == '':
                not_found.append(file[:-8])
            else:
                dict_file = {}
                dict_file['Sequence'] = file[:-8]
                dict_file['Score']  = re.findall(r'Score = (.*?) bits', data)[0]
                dict_file['Identitiy_frac']  = re.findall(r'Identities = (.*?),', data)[0].split()[0]
                dict_file['Identitiy_pct']  = int(re.findall(r'Identities = (.*?),', data)[0].split()[1].replace(')', '').replace('%', '').replace('(', '')) / 100
                dict_file['Gaps_frac']  = re.findall(r', Gaps = (.*?) ', data)[0].split()[0]
                dict_file['Gaps_pct']  = np.round(eval(dict_file['Gaps_frac']), 4)
                has_chromo = re.findall(r' chromosome (.*?),', data)
                if len(has_chromo) == 0:
                    dict_file['Cat_chromo'] = ''
                else:
                    dict_file['Cat_chromo'] = re.findall(r' chromosome (.*?),', data)[0]
                found = found.append(dict_file, ignore_index = True)
        
    print(found)
    print(not_found)
    print(num_files)
    print("Pct missing", len(not_found)/num_files)
    found.to_csv('../DATA/summary_data/cat_human.csv')

if __name__ == '__main__':
    main()