def LireListeEntiers():
    liste = []
    while True:
        try:
            nombre = input("Element?")
            if '.' in nombre:
                print("Veuillez entrer un entier valide.")
                continue
            nombre = int(nombre)
            if nombre < 0:
                break
            liste.append(nombre)
        except ValueError:
            print("Veuillez entrer un entier valide.")
    return liste

def LireListeReelsBornes(bmin=0, bmax=100):
    liste = []
    while True:
        try:
            nombre = float(input("Element?"))
            if nombre < bmin or nombre > bmax:
                break
            liste.append(nombre)
        except ValueError:
            print("Veuillez entrer un réel valide.")
    if not liste:
        return None, None, 0
    min_val = min(liste)
    max_val = max(liste)
    somme = sum(liste)
    return min_val, max_val, somme

def MMSListe(liste):
    if not liste:
        return None, None, 0
    min_val = liste[0]
    max_val = liste[0]
    somme = 0
    for nombre in liste:
        if nombre < min_val:
            min_val = nombre
        if nombre > max_val:
            max_val = nombre
        somme += nombre
    return min_val, max_val, somme

# Programme principal
if __name__ == "__main__":
    # Appel de la fonction LireListeEntiers
    liste_entiers = LireListeEntiers()
    print(liste_entiers)

    # Appel de la fonction LireListeReelsBornes
    min_val, max_val, somme = LireListeReelsBornes()
    if min_val is not None:
        print((min_val, max_val, somme))