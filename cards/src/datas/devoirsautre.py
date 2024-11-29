def tarif_carte(nom_carte):
    if nom_carte == "Jeune":
        return 50
        if periode == "bleue":
            prix *= 0.5
        elif periode == "blanche":
            prix *= 0.75
    elif carte is None and not modifiable:
        prix *= 0.9

    return prix

def prix_client():
    total = 0

    carte_reduction = input("Voulez-vous acheter une carte de réduction ? (oui/non) ").strip().lower()
    if carte_reduction == "oui":
        carte = input("Choisissez votre carte : (Jeune/Senior) ").strip()
        prix_carte = tarif_carte(carte)
        if prix_carte is None:
            return
        total += prix_carte
    else:
        carte = None

    billet = input("Voulez-vous acheter un billet ? (oui/non) ").strip().lower()
    if billet == "oui":
        depart = input("Depart : ").strip()
        destination = input("Destination : ").strip()

        if carte:
            print("Vous avez une carte de réduction")
            periode = input("Precisez la periode (bleue/blanche) : ").strip()
            prix_billet = tarif_billet(depart, destination, carte=carte, periode=periode)
        else:
            autres_precisions = input("Autres precisions a fournir ? (oui/non) ").strip().lower()
            if autres_precisions == "oui":
                carte = input("Carte de reduction (Jeune, Senior, ou aucune)? ").strip()
                if carte in ["Jeune", "Senior"]:
                    periode = input("Precisez la periode (bleue/blanche): ").strip()
                    prix_billet = tarif_billet(depart, destination, carte=carte, periode=periode)
                else:
                    modifiable = input("Billet modifiable ? (oui/non) ").strip().lower() == "oui"
                    prix_billet = tarif_billet(depart, destination, modifiable=modifiable)
            else:
                prix_billet = tarif_billet(depart, destination)

        if prix_billet is None:
            return
        total += prix_billet

    print(f"Prix total : {total} euros")
    return total