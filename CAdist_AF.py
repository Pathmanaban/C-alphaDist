"""
ProtMapPep.py

Created by Pathmanaban Ramasamy on 18th Sep 2018
Copyright (c) 2018 Pathmanaban Ramasamy. All rights reserved.

"""

from Bio.PDB import *
import numpy
import sys, getopt
import csv,os,argparse
from collections import defaultdict
import itertools

	    
def ca_dist(res1,res2):
	ca1 = res1['CA']
	ca2 = res2['CA']
	# Simply subtract the CA atoms to get their distance
	distance = ca1 - ca2
	return distance
# ~ x=0
# ~ keyerr=[]

def pdbparse(protid,pos1,pos2):
	
	# ~ global x
	# ~ global keyerr
	parser = PDBParser()
	curwd=os.getcwd()
	pdbid1="AF-"+protid+"-F1-model_v2.pdb"
	filepath=curwd+"/PDB/"+pdbid1
	if os.path.isfile(filepath): 
		structure = parser.get_structure(protid, filepath)

		model=structure[0]
		chain = model['A']
		pos1,pos2=int(pos1),int(pos2)
		#print chain[238]
		try:
			residue1 = chain[pos1]
			residue2 = chain[pos2]
			aadist=ca_dist(residue1,residue2)
		
			return aadist
		except KeyError as e:
			# ~ x+=1
			print (e.args[0])
			# ~ keyer.append([protid,pos1,pos2])
			
def CAdist():			
	parser = argparse.ArgumentParser(description='CA distance ')

	parser.add_argument('-i','--ifile', help='Specify the infile name with extension', required=True)
	parser.add_argument('-o','--ofile', help='Specify the outfile name with extension', required=True)
	parser.add_argument('-p1','--mutpos',help='Column index of mutation location in infile',required=True)
	parser.add_argument('-p2','--ptmpos',help='column index of modification in infile',required=True)
	parser.add_argument('-a','--acc',help='column index of protein accession in infile',required=True)
	args = vars(parser.parse_args())
	
	if len(args)==5:
		infile=args['ifile']
		outfile=args['ofile']
		mut_pos=int(args['mutpos'])
		ptm_pos=int(args['ptmpos'])
		accession=int(args['acc'])
		
		
		with open(infile,'r') as infile,open(outfile,'w') as outfile1:
			writer = csv.writer(outfile1,delimiter='\t')
			writer.writerow(['ACC_ID','Mut_pos','PTM_pos','CAdist(A)'])
			next(infile,None)
	
	
			datalis=defaultdict(list)
			for line in infile:
				line=line.split(',')
				protid=line[accession]
				ptmpos=line[ptm_pos]
				mutpos=line[mut_pos]
				if protid not in datalis:
					datalis[protid]=[(mutpos,ptmpos)]
					
					
				elif protid in datalis:
					#print datalis[pdbid][0],chain
					datalis[protid].append((mutpos,ptmpos))
		
	


			for acc,poslist in datalis.items():
				pdbid=acc
				poslist=list(set(poslist))
				print ("Calculating for Protein: ", pdbid)
				if  poslist:
			
					for elem in poslist:
					#print elem
						ca_dist=pdbparse(pdbid,elem[0],elem[1])
						writer.writerow([pdbid,int(elem[0]),int(elem[1]),float(ca_dist)])

		# ~ print ("total keyerrors",x)
		# ~ print (keyerr)
		
		print ("\n")
		print ("#################### Program finished ##############\n")									
		print ("Your results are available in the file: ", outfile)					

		print ("\n")
		print ("*****************************************************")
		print ("              Thanks for using CAdist                ")
		print ("*****************************************************")
	else:
		print ("Some argument missing")
		sys.exit() 
		

if __name__ == "__main__":
	print ("\n")
	print ("**************************************************")
	print ("               CAdist version 1.0                 ")
	print ("**************************************************")
	print ("\n")
	print ("Measuring CA distance.....please wait..............")
	CAdist()

