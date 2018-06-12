from Bio import Entrez
from Bio import SeqIO
from Bio.Seq import Seq
from Bio.Alphabet import IUPAC

Entrez.email = "ronaldvandenhurk@hotmail.com"

def openFile():
    try:
        file = open(snakemake.input[0], "r")
    except IOError:
        print("problem with file.")

    lines = file.readlines()
    data = []
    for x in lines:
        split_line = x.strip().split("\t")
        geneID = split_line[0]
        keggID = split_line[1]
        data.append([geneID,keggID])
    file.close()
    return data, lines

def getAccession(data):
    x = data[0]
    geneid = x[0]
    handle = Entrez.efetch(db="gene", id=geneid, retmode="xml")
    records = Entrez.parse(handle)

    for record in records:
        accession = record['Entrezgene_locus'][0]['Gene-commentary_accession']
    return accession


def giveMeMyFuckingGenbankFile(NCaccess):
    handle = Entrez.efetch(db="nuccore",id=NCaccess,rettype="gbwithparts",retmode="text")
    text = handle.read()
    seqLocList = []
    with open("GenbankFullFile.gbk","w") as file:
        file.write(text)

    for record in SeqIO.parse("GenbankFullFile.gbk", "genbank"):
        for f in record.features:
            if f.type == "gene":
                locus = f.qualifiers["locus_tag"][0]
                seqLocList.append([locus,str(f.location)])
    return seqLocList




def getSeq(seqLocList, NC):
        seqDic = {}
        handle = Entrez.efetch(db="nuccore", id=NC, rettype="fasta", retmode="text")
        seq = handle.read()
        with open("seq.fna", "w") as file:
             file.write(seq)
        record = SeqIO.read("seq.fna", "fasta")
        seq = record.seq
        for loc in seqLocList:
            locus = loc[0]
            pos = loc[1]
            start = pos[1:].split(":")[0]
            stop = pos.split(":")[1].split("]")[0]
            strand = pos.split("(")[1][0]
            genSeq = str(seq[int(start):int(stop)])
            if strand == "-":

                my_seq = Seq(genSeq, IUPAC.unambiguous_dna)
                genSeq = my_seq.reverse_complement()

            seqDic[locus] = genSeq
        return seqDic

def writeResult(seqDic, file):
    with open(snakemake.output[0], "w") as outfile:
        for line in file:
            line = line.strip().split("\t")
            locus = line[1]
            seq = seqDic[locus]
            line.append(seq)
            for i in line:
                outfile.write(str(i) + "\t")
            outfile.write("\n")




def main():
    data, fileLines = openFile()
    NCaccess = getAccession(data)
    seqLocList = giveMeMyFuckingGenbankFile(NCaccess)
    seqdata = getSeq(seqLocList, NCaccess)
    writeResult(seqdata, fileLines)

main()
