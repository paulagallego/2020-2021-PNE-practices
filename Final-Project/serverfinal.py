import http.server
import pathlib
import socketserver
import termcolor
from urllib.parse import urlparse, parse_qs
import server_utils_1 as su
from Seq1 import Seq

PORT = 8080
DICT_GENES = {
    'FRAT1': 'ENSG00000165879',
    'ADA': 'ENSG00000196839',
    'FXN': 'ENSG00000165060',
    'RNU6_269P': 'ENSG00000212379',
    'KDR': 'ENSG00000128052',
    'ANK2': 'ENSG00000145362',
    'TTTY4C': 'ENSG00000228296',
    'RBMY2YP': 'ENSG00000227633',
    'FGFR3': 'ENSG00000068078',
    'MIR633': 'ENSG00000207552',
}

endpointA = '/info/species'
endpointB = '/info/assembly/'
endpointC = '/sequence/id/'

# -- This is for preventing the error: "Port already in use"
socketserver.TCPServer.allow_reuse_address = True


# Class with our Handler. It is a called derived from BaseHTTPRequestHandler
# It means that our class inheritates all his methods and properties
class TestHandler(http.server.BaseHTTPRequestHandler):

    def do_GET(self):
        """This method is called whenever the client invokes the GET method
        in the HTTP protocol request"""

        # Print the request line
        global contents
        termcolor.cprint(self.requestline, 'green')
        termcolor.cprint(self.path, 'blue')

        o = urlparse(self.path)
        path_name = o.path
        arguments = parse_qs(o.query)
        print("Resource requested: ", path_name)
        print("Parameters: ", arguments)

        context = {}
        response_dict = su.obtain_dict(endpointA)
        complete_list_species = response_dict['species']
        name_species = []
        # Message to send back to the client
        if path_name == '/':
            contents = su.read_template_html_file('./html basic/menu.html').render()
        elif path_name == "/listSpecies":
            try:
                for elem in complete_list_species:
                    name_species.append(elem['display_name'])
                if 'limit' not in arguments:
                    context['length']=len(name_species)
                    context['species_list'] = name_species
                    contents=su.read_template_html_file('./html basic/noLimitSpeciesList.html').render(context=context)
                else:
                    if int(arguments['limit'][0]) <= len(name_species):
                        context['length'] = len(name_species)
                        context['species_list']=name_species
                        context['limit']=int(arguments['limit'][0])
                        contents=su.read_template_html_file('./html basic/listSpecies.html').render(context=context)
                    else:
                        contents=su.read_template_html_file('./html basic/ERROR.html').render()
            except KeyError:
                contents=su.read_template_html_file('./html basic/ERROR.html').render()
        elif path_name == '/karyotype':
            try:
                input_species = arguments['specie'][0]
                response_dict = su.obtain_dict(endpointB + input_species)
                list_karyotypes = response_dict['karyotype']
                context = {
                    'list_karyotype': list_karyotypes
                }
                contents=su.read_template_html_file('./html basic/karyotype.html').render(context=context)
            except KeyError:
                contents = su.read_template_html_file('./html basic/ERROR.html').render()
        elif path_name == '/chromosomeLength':
            try:
                if 'specie' not in arguments:
                    contents = su.read_template_html_file('./html basic/ERROR.html').render()
                elif 'chromo' not in arguments:
                    contents = su.read_template_html_file('./html basic/ERROR.html').render()
                else:
                    input_species = arguments['specie'][0]
                    input_chromo = arguments['chromo'][0]
                    response_dict=su.obtain_dict(endpointB+input_species)
                    for elem in response_dict['top_level_region']:
                        if elem['name'] == input_chromo and elem['coord_system'] == 'chromosome':
                            chromo_length = elem['length']

                        else:
                            contents = su.read_template_html_file('./html basic/ERROR.html').render()
                    context = {
                        'chromo_length': chromo_length
                    }
                    contents = su.read_template_html_file('./html basic/chromosomeLength.html').render(context=context)
            except KeyError:
                contents = su.read_template_html_file('./html basic/ERROR.html').render()

        elif path_name == '/geneSeq':
            try:
                input_gene = arguments['gene'][0]
                gene_id = DICT_GENES[input_gene]
                response_dict = su.obtain_dict(endpointC+gene_id)
                input_sequence = response_dict['seq']
                context = {
                    'sequence': input_sequence,
                    'gene': input_gene
                }
                contents = su.read_template_html_file('./html medium/geneSeq.html').render(context=context)
            except KeyError:
                contents=su.read_template_html_file('./html basic/ERROR.html').render()
        elif path_name == '/geneInfo':
            try:
                input_gene = arguments['gene'][0]
                gene_id = DICT_GENES[input_gene]
                response_dict = su.obtain_dict(endpointC+gene_id)
                info_chrom_list = response_dict['desc'].split(':')
                chrom_name = info_chrom_list[1]
                chrom_number = info_chrom_list[2]
                start_coord = info_chrom_list[3]
                end_coord = info_chrom_list[4]
                info_list = su.obtain_info_list(response_dict)
                context = {
                    'name_chromosome': chrom_name,
                    'number_chromosome': chrom_number,
                    'start_coordinates': start_coord,
                    'end_coordinates': end_coord,
                    'id': gene_id,
                    'gene_length': info_list[4],
                    'gene': input_gene
                }
                contents = su.read_template_html_file('./html medium/geneInfo.html').render(context=context)
                print(start_coord, end_coord)
            except KeyError:
                contents =su.read_template_html_file('./html basic/ERROR.html').render()
        elif path_name == '/geneCalc':
            try:
                input_gene = arguments['gene'][0]
                gene_id = DICT_GENES[input_gene]
                response_dict = su.obtain_dict(endpointC+gene_id)
                info_list=su.obtain_info_list(response_dict)
                context={
                    'gene':input_gene,
                    'length':info_list[4],
                    'A':info_list[0],
                    'C':info_list[1],
                    'G':info_list[2],
                    'T':info_list[3]
                }
                contents=su.read_template_html_file('./html medium/geneCalc.html').render(context=context)
            except KeyError:
                contents=su.read_template_html_file('./html basic/ERROR.html').render()
        else:
            pass

        print(contents)
        # Generating the response message
        self.send_response(200)  # -- Status line: OK!

        # Define the content-type header:
        self.send_header('Content-Type', 'text/html')
        self.send_header('Content-Length', str(len(contents.encode())))
        # The header is finished
        self.end_headers()

        # Send the response message
        self.wfile.write(contents.encode())

        return
# ------------------------
# - Server MAIN program
# ------------------------
# -- Set the new handler
Handler = TestHandler

# -- Open the socket server
with socketserver.TCPServer(("", PORT), Handler) as httpd:

    print("Serving at PORT", PORT)

    # -- Main loop: Attend the client. Whenever there is a new
    # -- clint, the handler is called
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("")
        print("Stopped by the user")
        httpd.server_close()