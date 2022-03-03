# CRdist
Python script to calculate distance between amino acids C-alpha atoms using PDB file. Works with AlphaFold models.
Takes "csv file" as input and outputs a "tsv file" containing distance information

## Usage

    python CAdist_AF.py  -i "input filename" -o "output filename" -p1 "residue1" -p2 "residue 2" -a "protein ID"
    
#### Description 

    -i,--ifile         infile name with extension
  
    -o,--ofile         outfile name with extension
  
    -a,--acc           column index of protein accession in infile
    
    -p1, --pos1         column index for first residue in infile
    
    -p2,--pos2          column index for the second residue in infile

    -h, --help         show this help message and exit

#### example

    python CAdist_AF.py  -i example.txt -o exampleout.txt -a 0 -p1 1 -p2 2 
    

## Information written to outfile

Results will be wirtten as tab delimited to the specified outfile name. 
     ----------------------------------------------
     | ACC_ID  | residue1   | residue2 | CAdist   |
     | --------|------------|----------|--------- |
     | O00571  |     46     |    320   |  47.2576 |
     | O00571  |    100     |    125   |  52.6169 | 
     | P02545  |    235     |    240   |  8.4829  |
     | P02545  |    116     |    200   |  123.6562|
     ----------------------------------------------
   
   
 
