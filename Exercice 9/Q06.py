import argparse

parser = argparse.ArgumentParser()

parser.add_argument("nombre", type=int, help="Un nombre entier")
parser.add_argument("operation", choices=["double", "binaire"], help="Type d'opération")

args = parser.parse_args()

if args.operation == "double":
    resultat = args.nombre * 2
    print(f"Le double de {args.nombre} est {resultat}")

elif args.operation == "binaire":
    resultat = bin(args.nombre)
    print(f"La représentation binaire de {args.nombre} est {resultat}")

"""
python "Exercice 9\Q06.py" 5 double
"""