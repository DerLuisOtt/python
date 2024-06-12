def func1(tupel):
    hypotenuse = float(pow(pow(tupel[0], 2)+pow(tupel[1], 2), 0.5))
    flaecheninhalt = float((tupel[0]*tupel[1])/2)
    return (tupel[0], tupel[1], hypotenuse, flaecheninhalt)
tupel = (1.0, 2.0)
tupel = func1(tupel)
print(tupel)
input("Done")
def func2(liste):
    woerterbuch = {"vorname":"luis", "nachname":"Ott", "alter":21, "geschlecht":'m'}
    for i in liste:
        x = None
        if i in woerterbuch:
            x = woerterbuch.get(i)
        if x is None:
            x = "der Key Value ist nicht vorhanden"
        print(x)
liste = ["vorname", "rasse", "alter", 20, 'm']
func2(liste)
input("Done")