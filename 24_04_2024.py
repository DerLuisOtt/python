from random import *
eingabe = float(input("Geben Sie die Zahlen in Minuten an: "))
stunden = int(eingabe//60)
minuten = int(eingabe%60)
sekunden = int(eingabe%1)*60
print(stunden,"h", minuten,"m", sekunden,"s")
input("Done")
raten = 0
zahl = randint(1,99)
while raten != zahl :
    raten = int(input("Erraten Sie die Zahl zwichen 0 und 100: "))
    if raten < zahl :
        print("größer")
    if zahl < raten :
        print("kleiner")
print("richtig")
input("Done")
eingabe2 = input("Schreiben Sie was Sie wollen: ")
buchstaben = ""
zahl2 = 0
for i in eingabe2:
    
    if(i.isnumeric()):
        zahl2 += int(i)
    else:
        buchstaben += i
print(zahl2, buchstaben)
input("Done")