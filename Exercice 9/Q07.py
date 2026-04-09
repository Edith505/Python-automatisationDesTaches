import argparse

parser = argparse.ArgumentParser()

parser.add_argument(
    "nombres",
    nargs='+',        
    type=int,
    help="Liste de nombres entiers séparés par des espaces"
)

args = parser.parse_args()

tab = args.nombres

somme = sum(tab)
moyenne = somme / len(tab)
maximum = max(tab)
minimum = min(tab)

print("Nombres saisis :", tab)
print("Somme :", somme)
print("Moyenne :", moyenne)
print("Maximum :", maximum)
print("Minimum :", minimum)