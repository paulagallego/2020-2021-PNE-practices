#Write a program that opens the ADA.txt file and writes the total number of bases (Have in mind that you should remove the new line ('\n') characters
from pathlib import Path
FILENAME = "ADA.txt"
file_contents = Path(FILENAME).read_text()
x = file_contents.split('\n', 1)
del x[0]
x.
z = int(len(x))



print('The correct result is: ', z)
