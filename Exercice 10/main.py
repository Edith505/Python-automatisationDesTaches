from Q01 import trouver_motif


chemin = "text.txt"

motif = "printer"

resultat = trouver_motif(chemin, motif)

if resultat is not None:
    print("Motif trouvé à :", resultat)
else:
    print("Motif non trouvé")