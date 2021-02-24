#Write a python program for calculating the total length of the 5 Genes: U5, ADA, FRAT1, FXN and U5. The program should call the seq_len() function
import Seq0
GENE_FOLDER = "./sequence/"
gene_list = ["U5, ADA, FRAT1, FXN"]
print("-----| Exercise 3 |------")
for gene in gene_list:
    sequence = Seq0.seq_read_fasta(GENE_FOLDER + gene + '.txt') #we need to use GENE_FOLDER in order to obtain the sequences (as ex1, ex2 are in directory P0 and sequences are in sequences directory)
    print('Gene' + gene + '---> length: ' + Seq0.seq_len(sequence))

