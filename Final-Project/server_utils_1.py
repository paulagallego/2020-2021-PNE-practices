import http.client
import json

import termcolor
from Seq1 import Seq
import pathlib
import jinja2
def read_html_file(filename):
    content = pathlib.Path(filename).read_text()
    return content

def read_template_html_file(filename):
    #create template object, can't be directly sent to the browser as it only reads plain text, files or html (template is none of them), we transform it by render function
    content = jinja2.Template(pathlib.Path(filename).read_text())
    return content

def print_colored(message, color):
    import termcolor
    import colorama
    colorama.init(strip="False")  # for pycharm's console to return colors and not weird symbols
    print(termcolor.colored("Message", "yellow"))
def format_command(command):
    return command.replace("\n", "").replace("\r","")
def ping():
    print_colored("PING command!", "green")
    print("OK!")


def get(list_sequences, seq_number):
    sequence = list_sequences[int(seq_number)] + '\n'
    context={
        "number": seq_number,
        "sequence": list_sequences[int(seq_number)]
    }
    contents = read_template_html_file("./html/get.html").render(context=context)
    return contents

def info(sequence):
    termcolor.cprint('INFO', 'green')
    s = Seq(sequence)
    info_dict = s.count()
    response =f"""Total length {len(sequence)}
A: {info_dict['A'][0]} ({info_dict['A'][1]})
C: {info_dict['C'][0]} ({info_dict['C'][1]})
G: {info_dict['A'][0]} ({info_dict['G'][1]})
T: {info_dict['T'][0]} ({info_dict['T'][1]})"""
    context = {
        'sequence': sequence,
        'information': response,
        'operation': 'info'
    }
    contents = read_template_html_file('./html/form-4.html').render(context=context)
    return contents

def comp(sequence):
    termcolor.cprint('COMP', 'green')
    s = Seq(sequence)
    complement = s.complement()
    response = complement + '\n'
    context = {
            'sequence': sequence,
            'information': response,
            'operation':'comp'
    }
    contents = read_template_html_file('./html/form-4.html').render(context=context)
    return contents
def rev(sequence):
    termcolor.cprint('REV', 'green')
    s= Seq(sequence)
    rev = s.reverse()
    response = rev + '\n'
    context = {
        'sequence': sequence,
        'information': response,
        'operation': 'Rev'
    }
    contents = read_template_html_file('./html/form-4.html').render(context=context)
    return contents

def gene(seq_name):
    PATH ="./Sequences/" + seq_name + '.txt'
    s = Seq()
    s.read_fasta(PATH)
    context= {
        "gene_name": seq_name,
        "gene_contents": s.strbases
    }
    contents = read_template_html_file("./html/gene.html").render(context=context)
    return contents
def obtain_dict(endpoint):
    server = "rest.ensembl.org"
    parameters = '?content-type=application/json'
    connection = http.client.HTTPConnection(server)
    connection.request('GET', endpoint+parameters)
    response=connection.getresponse()
    response_dict = json.loads(response.read().decode())
    return response_dict
def obtain_info_list(dict_info):
    input_seq=dict_info['seq']
    sequence_seq=Seq(input_seq)
    seq_length=[]
    length =sequence_seq.len()
    seq_length.append(length)
    info_dict=sequence_seq.info_seq()
    A_list = info_dict['A']
    C_list = info_dict['C']
    G_list = info_dict['G']
    T_list = info_dict['T']
    info_list=[]
    info_list.append(A_list)
    info_list.append(C_list)
    info_list.append(G_list)
    info_list.append(T_list)
    info_list.append(seq_length)
    return info_list



