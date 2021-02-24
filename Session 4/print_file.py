#This program just opens a text file (for example a dna file) and prints the contents on the console. The goal is to get familiar with the Path module. No error control is implemented yet
from pathlib import Path

# -- Constant with the new of the file to open
FILENAME = "RNU6_269P.txt"

# -- Open and read the file
file_contents = Path(FILENAME).read_text()

# -- Print the contents on the console
print(file_contents)