from Client0 import Client
import socket
import server_utils
PRACTICE = 3
EXERCISE = 7

print(f"-----| Practice {PRACTICE}, Exercise {EXERCISE} |------")

IP = "127.0.0.1"
PORT = 8080
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((IP, PORT))

c = Client(IP, PORT)
print(c)


print("*Testing PING...")
print(c.talk("OK!"))


print("*Testing GET...")
for argument in range(5):
    list_sequences[int(argument)] + '\n'

print("*Testing INFO...")

s = c.talk("INFO ACGTAAAAGTTTAAGCGCCAAT")
s.connect((self.ip, self.port))
print("To Server:", argument)
s.send(argument.encode())
response1 = s.recv(2048).decode("utf-8")
response2 = s.recv(2048).decode("uft-8")
response3 = s.recv(2048).decode("uft-8")
response4 = s.recv(2048).decode("uft-8")
response5 = s.recv(2048).decode("uft-8")
s.close()
print("From server: " + response1 + '\n' + response2 + '\n' + response3 + '\n'+ response4 + '\n' + response5 + '\n')

print('*Testing COMP...')
s = c.talk("COMP ACGTAAAAGTTTAAGCGCCAAT")
s.connect((self.ip, self.port))
print("To Server:", argument)
s.send(argument.encode())
response = s.recv(2048).decode("utf-8")
s.close()
print("From server: " + response)

print('*Testing REV...')
s = c.talk("REV ACGTAAAAGTTTAAGCGCCAAT")
s.connect((self.ip, self.port))
print("To Server:", argument)
s.send(argument.encode())
response = s.recv(2048).decode("utf-8")
s.close()
print("From server: " + response)

print('*Testing GENE...')
s = c.talk("GENE ACGTAAAAGTTTAAGCGCCAAT")
s.connect((self.ip, self.port))
print("To Server:", argument)
s.send(argument.encode())
response = s.recv(2048).decode("utf-8")
s.close()
print("From server: " + response)
