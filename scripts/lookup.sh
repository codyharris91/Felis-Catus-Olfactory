
#!/bin/bash

#NCBI "Welcome to E-utilities for PubMed" Sample Code for Class
#      Exercises; source:
#  https://dataguide.nlm.nih.gov/classes/intro/samplecode.html
echo "(vestigial AND vomeronasal)" > searchstring.txt

#5.1: Store query to be used in part 5.2                                                                                                                                                                                                     #
esearch -db pubmed -query "$(cat searchstring.txt)"   > esearch.out

#5.2: Let's retrieve the abstracts of the papers:
#
cat esearch.out | efetch -format abstract > searchresults.abstracts
echo "The abstracts of the papers have been written to file"
echo "  searchresults.abstracts"
echo "Appended first 20 lines of output to codyharris_module1.txt"
echo "with the most recent publications on top. Displaying the first"
echo "few lines of the file shows us the most recent publication:"
echo ""
head searchresults.abstracts
echo ""
head searchresults.abstracts >> ../LITERATURE/vestigial_vomeronasal.txt
echo ""
