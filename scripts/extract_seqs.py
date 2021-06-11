# Extract human seqs from tsv file from HORDE

import pandas as pd

df = pd.read_csv('../DATA/human_seqs/genes.csv', sep = '\t')
all_human_seq = ''
all_headers = []
for i in range(len(df)):
    line = df.iloc[i,:]
    if line['Pseduo Gene'] == 0:
        header = '>seq' + str(i) + ' Sym: ' + str(line['Symbol']) + ' Family Id ' + str(line['Family Id']) + ' Sub-Family ' +\
            line['Sub Family'] + ' Chromosome ' + str(line['Chromosome']) + ' Start ' + str(line['Start']) + ' End ' + str(line['End']) + '\n'
        all_headers.append(header)
        file = header + line['Nucleotide Sequence']
        file_name = '../DATA/human_seqs/' + str(line['Symbol']) + '.fasta'
        all_human_seq += file + '\n'
        with open(file_name, 'w') as writer:
            writer.write(file)
all_fname = '../DATA/human_blast/all_human_seq.fasta'
with open(all_fname, 'w') as writer:
    writer.write(all_human_seq)