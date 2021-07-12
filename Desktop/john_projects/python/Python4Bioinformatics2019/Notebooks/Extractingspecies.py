{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 17,
   "metadata": {},
   "outputs": [],
   "source": [
    "#combined function\n",
    "# This first code extracts all the species from files that have the species at fields 0\n",
    "\n",
    "def gene_extra(filename):\n",
    "    species=[]\n",
    "    with open(filename,'r') as myfile:\n",
    "        lines = myfile.readlines()\n",
    "        for i,line in enumerate(lines):\n",
    "            if i>35:\n",
    "                line_split = line.split()\n",
    "                fields = (line_split[0])\n",
    "                if fields.startswith('-'):\n",
    "                    break\n",
    "                #print(fields)\n",
    "                joined=''.join(fields)\n",
    "                species.append(joined)\n",
    "\n",
    "        return(species)\n",
    "\n",
    "\n",
    "        "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "metadata": {},
   "outputs": [],
   "source": [
    "#this second code writes the species extracted from the first code to a file\n",
    "def gene_writer(specielist,outfile1):\n",
    "    with open(outfile1,'w')as outfile:\n",
    "        outfile.write('species names \\n')\n",
    "        for sp in species:\n",
    "            outfile.write(sp+'\\n')\n",
    "        \n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 19,
   "metadata": {},
   "outputs": [],
   "source": [
    "gene_writer(gene_extra('../Data/humstr1.txt'),'../Data/gene_nm.txt')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "##Extracts species from a file\n",
    "def gene_extra(inputfile,outfile):\n",
    "    with open(inputfile,'r') as myfile:\n",
    "        with open(outfile,'w') as outfile:\n",
    "            lines = myfile.readlines()\n",
    "            for i,line in enumerate(lines):\n",
    "                if i>35:\n",
    "                    line_split = line.split()\n",
    "                    fields = (line_split[0])\n",
    "                    if fields.startswith('-'):\n",
    "                        break\n",
    "                    #print(fields)\n",
    "                    joined=''.join(fields)\n",
    "                    \n",
    "                    outfile.write(joined +'\\n')\n",
    "   \n",
    "    #print(species)\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "gene_extra('../Data/humstr1.txt',\"../Data/genenames.txt\")"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.6.5"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
