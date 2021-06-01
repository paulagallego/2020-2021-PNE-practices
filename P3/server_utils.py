from Seq1 import Seq
def print_colored(message, color):
    import termcolor
    import colorama
    colorama.init(strip="False")  # for pycharm's console to return colors and not weird symbols
    print(termcolor.colored(message, color))
def format_command(command):
    return command.replace("\n", "").replace("\r","")
def ping(cs):
    print_colored("PING command!", "green")
    response = "OK!"
    cs.send(str(response).encode())

def get(cs, list_sequences, argument):
    print_colored("GET", "yellow")
    response = list_sequences[int(argument)]
    print(response)
    cs.send(response.encode())
def info(cs, sequence):
    print_colored('INFO', 'green')
    s = Seq(sequence)
    response = 'Total length: ' + str(Seq.len(s)) + '\n' + str(Seq.percentage(s)) +'\n'
    print(response)
    cs.send(response.encode())
def comp(cs, sequence):
    print_colored('COMP', 'green')
    s = Seq(sequence)
    response=Seq.complement(s) + '\n'
    print(response)
    cs.send(response.encode())

def rev(cs, sequence):
    print_colored('REV', 'green')
    s= Seq(sequence)
    rev = s.reverse()
    response = rev + '\n'
    print(response)
    cs.send(response.encode())

def gene(cs, name_gene):
    gene_loc = './sequences/'
    print_colored('GENE', 'green')
    s = Seq()
    s.read_fasta(gene_loc + name_gene + ".txt")
    response = str(s) + '\n'
    print(response)
    cs.send(response.encode())