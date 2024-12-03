def tarif_carte(nom_carte):
    if nom_carte == "Jeune":
        return 50
        if periode == "bleue":
            prix *= 0.5
        elif periode == "blanche":
            prix *= 0.75
    elif carte is None and not modifiable:
        prix *=ction = input("Voulez-vous acheter une carte de réduction ? (oui/non) ").strip().lower()
    if carte_reduction == "oui":n billet ? (oui/non) ").strip().lower()
    if billet =et = tarif_billet(depart, destination, modifiable=modifiable)
            else:
                prix_billet = tarif_billet(depart, destination)

        if prix_billet is None:
            return
        total += prix_billet

    print(f"Prix total : {total} euros")
    return total