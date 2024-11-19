def prix_menu(nom_menu, avecBoisson=False, nb_supplement=0):
    prix = 0
    if nom_menu == "Basique":
        prix = 9
    elif nom_menu == "Gourmand":
        prix = 15
    elif nom_menu == "Complet":
        prix = 19
    else:
        raise ValueError("Nom de menu invalide")

    if avecBoisson:
        prix += 4

    prix += nb_supplement * 1.5

    return prix

def table_Dupont():
    prix_jacqueline = prix_menu("Basique")
    prix_michel = prix_menu("Gourmand", avecBoisson=True)
    prix_johanna = prix_menu("Basique", nb_supplement=2)
    prix_antoine = prix_menu("Basique", avecBoisson=True, nb_supplement=1)

    total = prix_jacqueline + prix_michel + prix_johanna + prix_antoine
    return total

# Exemple d'utilisation
if __name__ == "__main__":
    print(f"Le prix total pour la table des Dupont est de {table_Dupont()} euros.")