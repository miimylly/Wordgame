import sys
print(sys.path)
sys.path.append('C:\\Users\\miiam\\OneDrive\\Documents\\Academy\\Week 9\\Wordgame')



### Varsinainen sanapeli ###

print("Minkä sanan haluat etsiä")
sana = input()

index = 0
while index < len(sana):
    sana[index]
    index +=1

sanalista = open("words.txt", "r", encoding="utf-8")

while True:
    sanat = sanalista.readline() # Luetaan tiedostosta rivi
    if len(sanalista) == 0: # Jos rivin pituus on 0, ollaan lopussa
        break
    print(sanalista, end = "")
sanalista.close()