#tässä sotkua että voidaan lukea samasta working directorysta kuin missä ollaan AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
#import sys
#import os
#print(sys.path)
#sys.path.append('C:\\Users\\miiam\\OneDrive\\Documents\\Academy\\Week 9\\Wordgame')
#os.getcwd()
#os.chdir('C:\\Users\\miiam\\OneDrive\\Documents\\Academy\\Week 9\\Wordgame')

#importataan sanalista

from itertools import combinations
from itertools import permutations

def aloita():
    sanalista = open("wordlist.txt", "r")
    sanalista = list(sanalista)

    uusilista = []
    for sana in sanalista:
        uusilista.append(sana.replace("\n", ""))

    return uusilista

# Get all combinations
def kombinaatiot(sana):
    for i in range(len(sana)):
        comb = combinations(list(sana), i+1)
        # Get all permutations
        print(list(comb))
        #EI TOIMI
        #perm = permutations(list(comb))
        # Print the obtained permutations
        #for j in list(perm):
            #print(j)

def etsi_sanat(merkkijono, lista):
    return [sana for sana in lista if merkkijono in sana]

#print(etsi_sanat("moi", aloita()))
print(kombinaatiot("moi"))