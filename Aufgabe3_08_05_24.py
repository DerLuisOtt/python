def func1(zahl, liste):
    liste = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18]
    for i in liste:
        if(zahl == liste[i])
            del liste[i]
    print(liste)
liste = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,18,17,16,15,14,13]
eingabe = input("Geben Sie die zu entferndende Zahl ein: ")
func1(eingabe)
def func2(liste):
    liste1 = []
    for i in liste:
        zahl = liste[i]
        for f in liste:
            if(zahl == liste[f] and f != i):
                liste1.append(liste[i])
    for k in liste1:
        func1(liste1[k])
    liste.append(liste1)
    if(liste1):
        func2(liste)
func2(liste)
print(liste)
input("Done")