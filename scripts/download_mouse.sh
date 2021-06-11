#!/bin/bash
#Source: https://stackoverflow.com/questions/19058404/reading-files-line-by-line-in-by-using-for-loop-bash-script
#while IFS= read -r line <&3; do
#  echo "$line"
#  fname="${line}.fasta"
#  esearch -db nucleotide -query "$line" | efetch -format fasta > "${line}.fasta"
#done 3 < "$1"
while read line <&3; do
  echo $line
  esearch -db nucleotide -query "$line" | efetch -db nucleotide -format fasta > "../DATA/mouse_seqs/$line.fasta"
done 3<mouse_ids.txt
