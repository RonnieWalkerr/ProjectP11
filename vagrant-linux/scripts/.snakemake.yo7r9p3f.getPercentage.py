
######## Snakemake header ########
import sys; sys.path.insert(0, "/home/vagrant/miniconda3/envs/snakemake/lib/python3.5/site-packages"); import pickle; snakemake = pickle.loads(b'\x80\x03csnakemake.script\nSnakemake\nq\x00)\x81q\x01}q\x02(X\x06\x00\x00\x00paramsq\x03csnakemake.io\nParams\nq\x04)\x81q\x05}q\x06X\x06\x00\x00\x00_namesq\x07}q\x08sbX\x07\x00\x00\x00threadsq\tK\x01X\x06\x00\x00\x00configq\n}q\x0bX\x06\x00\x00\x00outputq\x0ccsnakemake.io\nOutputFiles\nq\r)\x81q\x0eX\x16\x00\x00\x00./data/sorted_data.txtq\x0fa}q\x10h\x07}q\x11sbX\x03\x00\x00\x00logq\x12csnakemake.io\nLog\nq\x13)\x81q\x14}q\x15h\x07}q\x16sbX\t\x00\x00\x00resourcesq\x17csnakemake.io\nResources\nq\x18)\x81q\x19(K\x01K\x01e}q\x1a(X\x06\x00\x00\x00_nodesq\x1bK\x01X\x06\x00\x00\x00_coresq\x1cK\x01h\x07}q\x1d(h\x1cK\x00N\x86q\x1eh\x1bK\x01N\x86q\x1fuubX\x05\x00\x00\x00inputq csnakemake.io\nInputFiles\nq!)\x81q"}q#h\x07}q$sbX\t\x00\x00\x00wildcardsq%csnakemake.io\nWildcards\nq&)\x81q\'}q(h\x07}q)sbX\x04\x00\x00\x00ruleq*X\x05\x00\x00\x00getGCq+ub.')
######## Original script #########
from Bio.SeqUtils import GC
import matplotlib.pyplot as plt
import numpy as np


def gcPercentage():
    try:
        file = open(snakemake.input[0], "r")
    except IOError:
        print("File broken")

    percentages = []
    for line in file.readlines():
        line = line.split("\t")
        seq = line[5]
        gen = line[0]
        gcseq = GC(seq)
        percentages.append([gen, gcseq])

    return percentages


def plotPercentage(gc):
    plt.style.use('ggplot')
    i = 0


    for x in range(0,len(gc),25):
        end = x + 25
        gene = []
        gcList = []
        atList = []
        for x in gc[x:end]:
            gene.append(x[0])
            gcList.append(x[1])
            atList.append(100-x[1])


        gcPerc = np.array(gcList)
        atPerc = np.array(atList)

        ind = [x for x, _ in enumerate(gene)]

        plt.bar(ind, gcPerc, width=0.5, label='GC %', color='yellow', bottom=atPerc)
        plt.bar(ind, atPerc, width=0.5, label='AT %', color='black')

        plt.xticks(ind, gene)
        plt.ylabel("Percentage")
        plt.xlabel("GeneID")
        plt.legend(loc="upper right")
        plt.title("GC % per GeneID")
        plt.setp(plt.gca().get_xticklabels(), rotation=45, horizontalalignment='right')

        
        
        #plt.show()
        plt.savefig(snakemake.output[i])
		i += 1
        plt.close()

def main():
    gc = gcPercentage()
    plot = plotPercentage(gc)

main()
