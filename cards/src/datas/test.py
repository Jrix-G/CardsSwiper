def gestion_comptes():
    lancement = input("Lancement de la gestion des comptes? ")
    if lancement.lower() != 'oui':
        print("OK. A bientot.")
        return

    solde_guillaume = float(input("Solde du compte de Guillaume? "))
    solde_marion = float(input("Solde du compte de Marion? "))

    if solde_guillaume > 0 and solde_marion > 0:
        print("Tous les deux en positif!")
    elif solde_guillaume < 0 and solde_marion < 0:
        print("Tous les deux en négatif!")
        print("Impossible de rétablir la situation.")
    elif solde_guillaume > 0 and solde_marion < 0:
        print("Marion est en négatif.")
        if solde_guillaume >= abs(solde_marion):
            print(f"Guillaume peut lui transférer {abs(solde_marion)} euros (il lui restera {solde_guillaume + solde_marion} euros).")
        else:
            print("Impossible de rétablir la situation.")
    elif solde_guillaume < 0 and solde_marion > 0:
        print("Guillaume est en négatif.")
        if solde_marion >= abs(solde_guillaume):
            print(f"Marion peut lui transférer {abs(solde_guillaume)} euros (il lui restera {solde_marion + solde_guillaume} euros).")
        else:
            print("Impossible de rétablir la situation.")

if __name__ == "__main__":
    gestion_comptes()