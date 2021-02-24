#Write a python program that opens the file RNU6_269P.txt and prints only its head

from pathlib import Path
FILENAME = "RNU6_269P.txt"
file_contents = Path(FILENAME).read_text()

x = file_contents.split('\n', 1)

print('First line of the RNU6_269P.txt file: ', '\n', x[0])
