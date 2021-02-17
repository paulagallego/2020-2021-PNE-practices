def correct_sequence(dna):
    for i in dna:
        if i != 'A' and i != 'C' and i != 'G' and i != 'T':
            return False
    return True
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

dna = input('Introduce a sequence: ')
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
