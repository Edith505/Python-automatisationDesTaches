from Q01 import trouver_motif
from Q02 import suivre_fichier


chemin = "text.txt"
motif = "printer"

resultat = trouver_motif(chemin, motif)

if resultat is not None:
    print("Motif trouvé à :", resultat)
else:
    print("Motif non trouvé")

print("-------------------------------------")
cheminQ2 = "\\var\\log\\syslog"
suivre_fichier(cheminQ2)