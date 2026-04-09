from pathlib import Path

"""
Question reformulée :

Écrire un script Python qui :

- Prend comme constante le chemin d’un dossier à analyser.
- Parcourt récursivement tous les fichiers et sous-dossiers de ce dossier.
- Calcule et affiche :
    le nombre total de fichiers
    la taille totale de tous les fichiers en kilo-octets (Ko)
    le plus gros fichier avec son nom et sa taille en Ko

"""

chemin = Path("C:/Users/2433177/Documents")

taille_totale = 0
nb_fichiers = 0
fichier_max = ""
taille_max = 0

for racine, dossiers, fichiers in chemin.walk():
    for nom in fichiers:
        fichier = racine / nom
        taille = fichier.stat().st_size / 1024
        
        taille_totale += taille
        nb_fichiers += 1

        if taille > taille_max:
            taille_max = taille
            fichier_max = fichier

print(f"Nombre total de fichiers : {nb_fichiers}")

print(f"Taille totale : {taille_totale:.2f} Ko")

print(f"Fichier le plus gros : {fichier_max} ({taille_max:.2f} Ko)")
