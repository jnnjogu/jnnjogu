#!/usr/bin/env python

import sys
filename = sys.argv[1]
outfile1 = sys.argv[2]


def gene_extra(filename):
    species=[]
    with open(filename,'r') as myfile:
        lines = myfile.readlines()
        for i,line in enumerate(lines):
            if i>35:
                line_split = line.split()
                fields = (line_split[0])
                if fields.startswith('-'):
                    break
                #print(fields)
                joined=''.join(fields)
                species.append(joined)

        return(species)

specieslist = gene_extra(filename)
def gene_writer(specieslist,outfile1):
    with open(outfile1,'w')as outfile:
        outfile.write('species names \n')
        for sp in specieslist:
            outfile.write(sp+'\n')
           
if __name__=='__main__':
  
    gene_writer(specieslist,outfile1)
    
    print('this is the name of the file to be extracted ', sys.argv[1])
    print('this is the name of the output file ', sys.argv[2])