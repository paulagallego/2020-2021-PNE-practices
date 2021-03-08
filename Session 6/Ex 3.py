from Seq0 import Seq, generate_seqs #used function can be written this way too
#function found in module



seq_list1 = generate_seqs('A', 3)
seq_list2 = generate_seqs('AC', 5)

print('List 1:')
Seq.print_seqs(seq_list1)

print()
print('List 2:')
Seq.print_seqs(seq_list2)