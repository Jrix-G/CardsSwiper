def dico_add(dico, key, value):
    if key in dico:
        dico[key].append(value)
    else:
        dico[key] = value
    return dico

def dico_search(dico, value):
    for key in dico:
        print(key)
        if dico[key] == value:
            return key, value
    return None

def calcul_marche(dico, marche="marche"):
    for key in dico:
        if key == marche:
            sume = 0
            for i in dico[key]:
                sume += dico[key][i]
    return sume
