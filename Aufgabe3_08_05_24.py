def func1(liste):
    eingabe = int(input("Geben Sie die zu entferndende Zahl ein: "))
    while eingabe in liste:
        liste.remove(eingabe)
    print(liste)
liste = [0,122,2,3,4,29,6,7,18,9,10,11,12,13,14,15,16,17,18,18,17,16,15,14,13]
func1(liste)
input("Done")
def func2(liste):
    i = 0
    while i < len(liste):
        j = i + 1
        while j < len(liste):
            if liste[j] == liste[i]:
                del liste[j]
            else:
                j += 1
        i += 1
    print(liste)
func2(liste)
input("Done")
def func3(liste):
    i = 0
    while i < len(liste):
        j = 0
        while j < len(liste)-i-1:
            k = j + 1
            if liste[k] < liste[j]:
                zwischen = liste[j]
                liste[j] = liste[k]
                liste[k] = zwischen
            j += 1
        i += 1
    print(liste)
func3(liste)
input("Done")