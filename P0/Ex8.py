#Write a python program that automatically calculate the answer to this question: Which is the most frequent base in each gene?
import Seq0
GENE_FOLDER = "./sequences/"
gene_list = ["U5", "ADA", "FRAT1", "FXN"]
print("-----| Exercise 8 |------")
for gene in gene_list:
    sequence = Seq0.seq_read_fasta(GENE_FOLDER + gene + '.txt') #we need to use GENE_FOLDER in order to obtain the sequences (as ex1, ex2 are in directory P0 and sequences are in sequences directory)
    print('Gene ', gene, 'Most frequent base: ', Seq0.most_freq(sequence))
