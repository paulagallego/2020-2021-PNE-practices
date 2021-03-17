#Write a python program that automatically calculate the answer to this question:

#Which is the most frequent base in each gene?

from Seq1 import Seq

def print_result(i, sequence): #i=number sequence are what changes along the def
    print('Sequence' + ': (Length: ' + str(sequence.len()) + ')' + str(sequence))
    print('Most common bases: ' + str(sequence.most_frequent_bases()))


PROJECT_PATH = "../P0/sequences/"
file_list =['ADA.txt', 'FRAT1.txt', 'FXN.txt', 'RNU6_269P.txt', 'U5.txt']
print('-----|Practice 1, Exercise 9|-----')
for file in file_list:
    s1 = Seq()
    s1.read_fasta(PROJECT_PATH + file)
    s1.most_frequent_bases()
    print_result("", s1)


