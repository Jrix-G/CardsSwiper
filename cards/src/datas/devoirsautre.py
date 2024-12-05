def moyenne_etudiant(etudiant):
    moyenne = 0
    for i in etudiant["notes"]:
        moyenne += etudiant["notes"][i]
    return moyenne / len(etudiant["notes"])
