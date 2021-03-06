#place all the imports at the beginning of the code
from pathlib import Path

def seq_ping():
    print('OK')

def take_out_first_line(seq):
    return seq[seq.find('\n') + 1:].replace('\n', "")

def seq_read_fasta(filename):
    sequence = take_out_first_line(Path(filename).read_text())
    return sequence

def seq_len(seq):
    return len(seq) #bc every time we call seq_len we will have first called seq_read_fasta

def seq_count_base(seq, base):
    return seq.count(base)
def seq_count(seq):
    gene_dict = {'A': 0, 'C': 0, 'G': 0, 'T': 0}
    for d in seq:
        gene_dict[d] +=1
    return gene_dict
def seq_reverse(seq):
    first_20_bases = seq[0:20]
    return(first_20_bases[::-1])
def seq_complement(seq):
    comp_dict = {'A': 'T', 'G': 'C', 'C': 'G', 'T': 'A'}
    comp_seq = []
    for i in seq:
        comp_seq.append(comp_dict[i])
    comp_seq_str = "".join(comp_seq)
    return comp_seq_str
def most_freq(seq):
    gene_dict = {'A': 0, 'C': 0, 'G': 0, 'T': 0}
    for d in seq:
        gene_dict[d] += 1
    freq_base = max(gene_dict, key=gene_dict.get)
    return freq_base
#def is_valid_sequence(self):#if we need the class attributes to work with this function, we need to add 'self' as an argument of the function
        #for i in self.strbases:
            #if i != 'A' and i !='C' and i != 'G' and i != 'T':
                #return False
        #return True



