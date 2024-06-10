def func1(tupel):
    hypotenuse = float(pow(pow(tupel[0], 2)+pow(tupel[1], 2), 0.5))
    flaecheninhalt = float((tupel[0]*tupel[1])/2)
    return (tupel[0], tupel[1], hypotenuse, flaecheninhalt)
tupel = (1.0, 2.0)
tupel = func1(tupel)
print(tupel)
input("Done")