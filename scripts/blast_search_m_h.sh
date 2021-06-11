#!/bin/bash
FILES="../DATA/mouse_seqs/*.fasta"
for f in $FILES
do
  echo "Processing $f"
  fn=${f##*/}
  fnn="${fn%.fasta}"
  blastn -query $f -db ../DATA/human_blast/all_human_seq.fasta | egrep ">" -A 7 -m 1 > "../DATA/mouse_human_results/${fnn}.summary"
done
