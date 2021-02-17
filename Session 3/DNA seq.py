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
print('Total length: ', len(dna))
#avoids running the loops so many times
a, c, g, t = dnacount(dna)
print(f"A: {a} \n"
      f"C: {c} \n"
      f"G: {g} \n"
      f"T: {t} \n")


