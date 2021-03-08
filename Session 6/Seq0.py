#place all the imports at the beginning of the code
from pathlib import Path
import termcolor

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
class Seq:
    """A class for representing sequences"""
    def __init__(self, strbases = 'NULL'):
        #Initialize the sequence with the value passed as argument when creating the object
        if strbases == 'NULL':
            print('Null seq created')
            self.strbases = strbases
        else:
            if self.is_valid_sequence():
                self.strbases = strbases
                print('New sequence created!')

            else:
                self.strbases = 'Error'
                print('INCORRECT sequence detected')

    def is_valid_sequence(self):
        for i in self.strbases:
            if i != 'A' and i != 'C' and i != 'G' and i != 'T':
                return False
        return True

    @staticmethod
    def is_valid_sequence_2(bases):
        for i in strbases:
            if i != 'A' and i != 'C' and i != 'G' and i != 'T':
                return False
        return True
    @staticmethod
    def print_seqs(list_sequences):
        for i in range(0, len(list_sequences)):
            #in order to use termcolor, we need to pass the first argument(text) as a whole string, the second argument would be the color we want to use
            text = 'Sequence' + str(i) + ': (Length:' + str(list_sequences[i].len()) + ')'+ str(list_sequences[i])
            termcolor.cprint(text, 'yellow')
    def __str__(self):
        """Method called when the object is being printed"""
        # -- We just return the string with the sequence
        return self.strbases

    def len(self):
        """Calculate the length of the sequence"""
        return len(self.strbases)


def generate_seqs(pattern, number):
    #A, 3
    list_seq = []
    for i in range(0, number):
        list_seq.append(Seq(pattern * (i + 1)))
    return list_seq
