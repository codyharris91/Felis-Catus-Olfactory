#!/bin/bash
FILES="../DATA/human_seqs/*.fasta"
for f in $FILES
do
  echo "Processing $f"
  fn=${f##*/}
  fnn="${fn%.fasta}"
  blastn -query $f -db ../DATA/cat_blast/all_seq.fasta | egrep ">" -A 7 -m 1 > "../DATA/cat_blast_results/${fnn}.summary"
done
