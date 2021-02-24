#Write a program that opens the U5.txt file and prints on the console all the lines except the first one
from pathlib import Path
FILENAME = "U5.txt"
file_contents = Path(FILENAME).read_text()
x = file_contents.split('\n')
print('Body of the U5.txt file: ')
for element in x[1:]:
    print (element)



