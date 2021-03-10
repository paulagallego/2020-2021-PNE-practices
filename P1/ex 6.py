from Seq1 import Seq, test_sequences
#we create test_sequences to avoid writing the same seq all the time, cleaner code as the seq arent relevant for the program
#if we write import seq1, we'd need to add list(seq1.test_sequences().
def print_result(i, sequence): #i=number sequence are what changes along the def
    print('Sequence' + str(i) + ': (Length: ' + str(sequence.len()) + ')' + str(sequence))
    print('Bases: ', sequence.count())
print('-----|Practice 1, Exercise 6|-----')
list_sequences = list(test_sequences())
for i in range(0, len(list_sequences)):
    print_result(i, list_sequences[i])