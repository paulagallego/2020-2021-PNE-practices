def correct_sequence(dna):
    for i in dna:
        if i != 'A' and i != 'C' and i != 'G' and i != 'T':
            return False
    return True #must be outside the if loop or it wont work as desired
def dnacount(dna):
    a, c, g, t = 0,0,0,0

    for i in dna:
            if i == 'A':
                a += 1
            elif i == 'C':
                c += 1
            elif i == 'G':
                g += 1
            else:
                t += 1
    return a,c,g,t
def read_from_file(filename):
    with open(filename, 'r') as f:
        dna = f.read()
        dna = dna.replace('\n', '')
        f.close() #not necesary as we are just running the code once, if more than once it is needed
        return dna

dna = read_from_file('dna.txt')

correct_dna = correct_sequence(dna)
if correct_sequence(dna):
    print('Total length: ', len(dna))
#avoids running the loops so many times
    a, c, g, t = dnacount(dna)
    print(f"A: {a} \n"
      f"C: {c} \n"
      f"G: {g} \n"
      f"T: {t} \n")
else:
    print('Not a valid dna sequence')


