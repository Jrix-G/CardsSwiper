def moyenne_etudiant(etudiant):
    moyenne = 0
    for i in etudiant["notes"]:
        moyenne += etudiant["notes"][i]
    return moyenne / len(etudiant["notes"])

def meilleur(notes_groupe):
    print(notes_groupe[0]["notes"])
    meilleure_note = moyenne_etudiant(notes_groupe[0])
    for i in range(1, len(notes_groupe)):
        if moyenne_etudiant(notes_groupe[i]) > meilleure_note:
            meilleure_note = moyenne_etudiant(notes_groupe[i])
            name = notes_groupe[i]["nom"]
    return meilleure_note, name

print("JKASDK", meilleur([{"classe": 2, "nom": "Patrick", "notes": {"math": 12, "fr": 14, "hist": 10}},{"classe": 2, "nom": "Jason", "notes": {"math": 15, "fr": 20, "hist": 10}}])) 