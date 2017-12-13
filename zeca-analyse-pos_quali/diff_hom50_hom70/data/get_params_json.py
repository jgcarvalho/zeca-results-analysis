import json
from pprint import pprint
from sys import argv
import os
from string import maketrans

with open(argv[1]) as data_file:    
    data = json.load(data_file)

base=os.path.basename(argv[1])
print base

intab = "_*|?"
outtab = "CHE?"
trantab = maketrans(intab, outtab)

fseq = open("./seq/"+base, "w")
fseq.write(">"+base+"\n")
fseq.write("".join(data["Seq"]))
fseq.close()

fseq = open("./all3/"+base, "w")
fseq.write(">"+base+"\n")
ss = "".join(data["All3"])
ss = ss.replace("*", "H").replace("|", "E").replace("_", "C")
fseq.write(ss)
fseq.close()

fseq = open("./dssp/"+base, "w")
fseq.write(">"+base+"\n")
ss = "".join(data["Dssp3"])
ss = ss.replace("*", "H").replace("|", "E").replace("_", "C")
fseq.write(ss)
fseq.close()

fseq = open("./stride/"+base, "w")
fseq.write(">"+base+"\n")
ss = "".join(data["Stride3"])
ss = ss.replace("*", "H").replace("|", "E").replace("_", "C")
fseq.write(ss)
fseq.close()

fseq = open("./kaksi/"+base, "w")
fseq.write(">"+base+"\n")
ss = "".join(data["Kaksi3"])
ss = ss.replace("*", "H").replace("|", "E").replace("_", "C")
fseq.write(ss)
fseq.close()

fseq = open("./pross/"+base, "w")
fseq.write(">"+base+"\n")
ss = "".join(data["Pross3"])
ss = ss.replace("*", "H").replace("|", "E").replace("_", "C")
fseq.write(ss)
fseq.close()
