def commence_par(lettre, mot):
    return mot[0] == lettre

def contient_voyelle(mot):
    voyelles = "aeiouy"
    for lettre in mot:
        if lettre in voyelles:
            return True
    return False

def derniere_consonne(mot):
    voyelles = "aeiouy"
    for i in range(len(mot) - 1, -1, -1):
        if mot[i] not in voyelles:
            return i, mot[i]
    return None, None

def double_consonne(mot):
    voyelles = "aeiouy"
    for i in range(len(mot) - 1):
        if mot[i] == mot[i + 1] and mot[i] not
    return mot not in mots_interdits