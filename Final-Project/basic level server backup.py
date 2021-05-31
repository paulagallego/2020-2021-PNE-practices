import http.server
import pathlib
import socketserver
import termcolor
from urllib.parse import urlparse, parse_qs
import server_utils_1 as su
from Seq1 import Seq

PORT = 8080

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
        termcolor.cprint(self.requestline, 'green')
        termcolor.cprint(self.path, 'blue')

        o = urlparse(self.path)
        path_name = o.path
        arguments = parse_qs(o.query)
        print("Resource requested: ", path_name)
        print("Parameters: ", arguments)
        # IN this simple server version:
        # We are NOT processing the client's request
        # It is a happy server: It always returns a message saying
        # that everything is ok
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
                        if elem['name']== input_chromo and elem['coord_system'] == 'chromosome':
                            chromo_length = elem['length']

                        else:
                            contents = su.read_template_html_file('./html basic/ERROR.html').render()
                    context = {
                        'chromo_length': chromo_length
                    }
                    contents = su.read_template_html_file('./html basic/chromosomeLength.html').render(context=context)
            except KeyError:
                contents = su.read_template_html_file('./html basic/ERROR.html').render()
        else:
            contents = su.read_template_html_file('./html basic/ERROR.html').render()

        print(contents)
        # Generating the response message
        self.send_response(200)  # -- Status line: OK!

        # Define the content-type header:
        self.send_header('Content-Type', 'text/html')
        self.send_header('Content-Length', len(contents.encode()))

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