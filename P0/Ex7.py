#Write a python program for creating a new fragment composed of the first 20 bases of the U5 gene. This fragment should be printed on the console. Then calculate the complement of this fragment by calling the seq_complement() function. Finally print it on the console
import Seq0
GENE_FOLDER = './sequences/'
ID = 'U5.txt'
U5_Seq = Seq0.seq_read_fasta(GENE_FOLDER + ID)
print('------| Exercise 7 |------')
print('The first 20 bases are: ', U5_Seq[0:20])
print('The complementary sequence is: ', Seq0.seq_complement(U5_Seq[0:20]))