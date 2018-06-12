from Bio import Entrez
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

    return data

def getData (data):
    newdata = []
    for x in data:
        geneid = x[0]
        locus = x[1]
        handle = Entrez.efetch(db="gene", id=geneid, retmode="xml")
        records = Entrez.parse(handle)
        for record in records:
            description = record['Entrezgene_locus'][0]['Gene-commentary_products'][0]['Gene-commentary_label']
            pubmedIDs = record['Entrezgene_locus'][0]['Gene-commentary_products'][0]["Gene-commentary_refs"]
            pubHits = []
            for hit in pubmedIDs:
                hit = hit["Pub_pmid"]["PubMedId"]
                pubHits.append(hit)
        newdata.append([geneid, locus, description, pubHits])
    return newdata

# Wegschrijven van de data, tabs separated, in een text-bestand.
def writeOutput(data):
    output = open(snakemake.output[0], "w")
    for i in data:
        pubmedline = ""
        for id in i[3]:
            pubmedline += id
            if id != i[3][len(i[3])-1]:
                pubmedline += ","
        line = i[0] + "\t"+ i[1]+ "\t"+ i[2]+ "\t"+ pubmedline +"\n"
        output.write(line)


def main():
    data = openFile()
    data = getData(data)
    writeOutput(data)

main()
