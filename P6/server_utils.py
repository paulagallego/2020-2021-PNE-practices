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
    response = "OK!"
    cs.send(str(response).encode())

def get(list_sequences, seq_number):
    context={
        "number": seq_number,
        "sequence": list_sequences[int(seq_number)]
    }
    contents = read_template_html_file("./html/get.html").render(context=context)
    return contents

def info(cs, argument):
    termcolor.cprint('INFO', 'green')
    s = Seq(argument)
    info_dict = s.info_seq()
    response1 = 'Total length: ' + str(len(argument)) + '\n'
    cs.send(response1.encode())
    response2 = 'A: ' + str(info_dict['A'][0]) + ' ' + str(info_dict['A'][1]) + '%' + '\n'
    cs.send(response2.encode())
    response3 = 'C: ' + str(info_dict['C'][0]) + ' ' + str(info_dict['C'][1]) + '%' + '\n'
    cs.send(response3.encode())
    response4 = 'G: ' + str(info_dict['G'][0]) + ' ' + str(info_dict['G'][1]) + '%' + '\n'
    cs.send(response4.encode())
    response5 = 'T: ' + str(info_dict['T'][0]) + ' ' + str(info_dict['T'][1]) + '%' + '\n'
    cs.send(response5.encode())
    print(response1, response2, response3, response4, response5)

def comp(cs, argument):
    termcolor.cprint('COMP', 'green')
    s = Seq(argument)
    complement = s.complement()
    response = complement + '\n'
    cs.send(response.encode())
    print(response)

def rev(cs, argument):
    termcolor.cprint('REV', 'green')
    s= Seq(argument)
    rev = s.reverse()
    response = rev + '\n'
    cs.send(response.encode())
    print(response)

def gene(seq_name):
    PATH ="./Sequences/" + seq_name + '.txt'
    s1 = Seq()
    s1.read_fasta(PATH)
    context= {
        "gene_name": seq_name,
        "gene_contents": s1.str_bases
    }
    contents = read_template_html_file("./html/gene.html").render(context=context)
    return contents