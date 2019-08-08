#tässä sotkua että voidaan lukea samasta working directorysta kuin missä ollaan AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
#import sys
#import os
#print(sys.path)
#sys.path.append('C:\\Users\\miiam\\OneDrive\\Documents\\Academy\\Week 9\\Wordgame')
#os.getcwd()
#os.chdir('C:\\Users\\miiam\\OneDrive\\Documents\\Academy\\Week 9\\Wordgame')

### Varsinainen sanapeli ###

#importataan sanalista
sanalista = open("wordlist.txt", "r")


# Kysytään sana mitä halutaan etsiä
print("Minkä sanan haluat etsiä")
sana = input()

index = 0
while index < len(sana):
    sana[index]
    index +=1



while True:
    sanat = sanalista.readline() # Luetaan tiedostosta rivi
    if len(sanalista) == 0: # Jos rivin pituus on 0, ollaan lopussa
        break
    print(sanalista, end = "")
sanalista.close()