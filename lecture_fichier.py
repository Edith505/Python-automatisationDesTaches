import argparse
import pathlib as path
"""

parser = argparse.ArgumentParser()

parser.add_argument("fichier", type=str)

args = parser.parse_args()

with open(args.fichier, "r") as f:
    for line in f:
        print(line.rstrip("\n"))
"""
chemin = path.Path("text.txt")

print(f"chemin absolut : {chemin.absolute()}\n")
with open(chemin, "r") as f:
    print(f.read())

print(list(path.Path("Exercice 9").walk()))