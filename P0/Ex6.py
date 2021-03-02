#Write a python program for creating a new fragment composed of the first 20 bases of the U5 gene. This fragment should be printed on the console. Then calculate the reverse of this fragment by calling the seq_reverse() function. Finally print it on the console
import Seq0
GENE_FOLDER = './sequences/'
ID = 'U5.txt'
U5_Seq = Seq0.seq_read_fasta(GENE_FOLDER + ID)
print('------| Exercise 6 |------')
print('The first 20 bases are: ', U5_Seq[0:20])
print('Reverse: ', Seq0.seq_reverse(U5_Seq))
