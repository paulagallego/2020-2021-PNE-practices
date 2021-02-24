import Seq0

GENE_FOLDER = "./sequences/"
gene_list = ["U5", "ADA", "FRAT1", "FXN"]
base_list = ['A', 'C', 'T', 'G']
print("-----| Exercise 4 |------")

for gene in gene_list:
    sequence = Seq0.seq_read_fasta(GENE_FOLDER + gene + '.txt') #we need to use GENE_FOLDER in order to obtain the sequences (as ex1, ex2 are in directory P0 and sequences are in sequences directory)
    print('Gene', gene)
    for base in base_list:
        print(base + ":", Seq0.seq_count_base(sequence, base))


