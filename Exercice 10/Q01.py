import os

def trouver_motif(chemin_fichier, motif):
    resultat = None

    if not os.path.exists(chemin_fichier):
        print("le fichier n'existe pas")
    
    elif not os.path.isfile(chemin_fichier):
        print("erreur fichier")
    
    else:
        with open(chemin_fichier, 'r') as fichier:
            for index_ligne, ligne in enumerate(fichier):

                #la méthode find() return 0 ou -1
                index_colonne = ligne.find(motif)

                if index_colonne != -1:
                    resultat = (index_ligne, index_colonne)
                    break

    return resultat

