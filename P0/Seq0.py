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