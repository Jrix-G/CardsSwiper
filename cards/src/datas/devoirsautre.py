def decomp(n):
    digit = []
    while n > 0:
        digit.append(n%10)
        n //= 10

    return digit

def estA(n):
    liste = decomp(n)
    nombre = 0
    for c in liste:
        nombre += c**len(liste)
    return nombre == n

def allbelo(nmax):
    liste = []
    for i in range(nmax):
        if estA(i):
            liste.append(i)

    return liste

faire exercice sur le triangle de pascal.