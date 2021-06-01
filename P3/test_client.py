import self as self
from Client0 import Client

import server_utils
PRACTICE = 3
EXERCISE = 7

print(f"-----| Practice {PRACTICE}, Exercise {EXERCISE} |------")
list_sequences = ["ACGTAAAAGTTTAAGCGCCAAT", "AGTCCCCCCAAAATTTTGGGGGAATAT", "AGAGAGAGGATTATTATATACTCTTC", "GGGGGGGGGGGTTTTTTTTTAAAAAACCCC", "AAAAAATTTTTCGAAAAAAA"]
list_genes = ["U5", "ADA", "FRAT1", "FXN", "RNU6_269P"]
IP = "127.0.0.1"
PORT = 8080


c = Client(IP, PORT)
print(c)


print("*Testing PING...")
print(c.talk("OK!"))


print("*Testing GET...")
for elem in range(0, len(list_sequences)):
    response=c.talk("GET "+str(elem))
    print(f"{response}")

print("*Testing INFO...")
for elem in range(0, len(list_sequences)):
    response=c.talk("INFO "+str(elem))
    print(f"{response}")

print('*Testing COMP...')
for elem in range(0, len(list_sequences)):
    response=c.talk("COMP "+str(elem))
    print(f"{response}")

print('*Testing REV...')
for elem in range(0, len(list_sequences)):
    response=c.talk("REV "+str(elem))
    print(f"{response}")


print('*Testing GENE...')
for elem in list_genes:
    response = c.talk("GENE " + str(elem))
    print(f"{response}")