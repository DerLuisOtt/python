liste = [1,4,5,9,6]
del liste[2]
a = len(liste)
def funktionsname(parameter):
    parameter.sort()
    parameter.reverse()
    print(parameter)
#b = liste[2]
#c = liste[-1]
print(a)
liste.append(3)
liste.insert(3, 8)
print(liste)
for i in liste:
    print(i)
mix = [12, 15.4, "Brot", False, print, [2, 3, 4]]
print(mix)
y = liste[1:4:2]
print(y)
#liste = kopieren[start:ende:schritte]
del liste[2:4:1]
print(liste)
#liste[:] wählt alles aus
print(5 in liste)
funktionsname(liste[:])
input("Done")
