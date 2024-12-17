def compte(liste):
    dicoR = {}
    for c in liste:
        print("SAODAOSD", c)
        if c in dicoR:
            dicoR[c] += 1
        else:
            dicoR[c] = 1
    return dicoR

print(compte("Salut commment ca va moi ca va bien"))
 