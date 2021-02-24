#Write a python program that opens the file RNU6_269P.txt and prints only its head

from pathlib import Path
FILENAME = input('Introduce a valid filename')
file_contents = Path(FILENAME).readline()
head = 0
for line in file_contents:
    if head == 0:
        x = file_contents.split('\n')
        head +=1
        print('first line of the', FILENAME, 'file:', '\n', x )
    else:
        break
