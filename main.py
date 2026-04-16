from pathlib import Path

def trouver_motif(chemin_fichier, motif):
    resultat = None
    chemin = Path(chemin_fichier)

    with chemin.open('r') as fichier:
        for index_ligne, ligne in enumerate(fichier):
            print(f"index : {index_ligne}, ligne : {ligne}")

    return resultat

trouver_motif('text.txt', 'text')