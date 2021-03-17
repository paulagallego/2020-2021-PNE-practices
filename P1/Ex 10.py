#Write a python program that automatically calculate the answer to this question:

#Which is the most frequent base in each gene?

from Seq1 import Seq

def print_result(i, sequence): #i=number sequence are what changes along the def
    print('Sequence' + ': (Length: ' + str(sequence.len()) + ')' + str(sequence))
    print('Most common bases: ' + str(sequence.most_frequent_bases()))


PROJECT_PATH = "../P0/sequences/"
print('-----|Practice 1, Exercise 9|-----')
s1 = Seq()
s1.read_fasta(PROJECT_PATH + 'ADA.txt')
s1.most_frequent_bases()
print_result("", s1)
s2 = Seq()
s2.read_fasta(PROJECT_PATH + 'FRAT1.txt')
s2.most_frequent_bases()
print_result("", s2)
s3 = Seq()
s3.read_fasta(PROJECT_PATH + 'FXN.txt')
s3.most_frequent_bases()
print_result("", s3)
s4 = Seq()
s4.read_fasta(PROJECT_PATH + 'RNU6_269P.txt')
s4.most_frequent_bases()
print_result("", s4)
s5 = Seq()
s5.read_fasta(PROJECT_PATH + 'U5.txt')
s5.most_frequent_bases()
print_result("", s5)

