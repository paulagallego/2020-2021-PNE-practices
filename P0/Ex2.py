#Write a python program for opening the U5.txt file and writing into the console the first 20 bases of the sequence

import Seq0
FOLDER = "./sequences/" #referencing to another file, 1 point= same folder, 2 points = parent folder (root of repository, in this case 2020-2021 PNE PRACTICES)
ID = 'ADA.txt'

U5_Seq = Seq0.seq_read_fasta(FOLDER + ID)
print('The first 20 bases are: ', U5_Seq[0:20])
#print(len(U5_Seq[0:20])) #Use to count the number of bases in each interval (in case of doubt)
