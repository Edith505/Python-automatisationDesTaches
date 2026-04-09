import argparse

parser = argparse.ArgumentParser(description="un exemple de argparse")

parser.add_argument("nom",type=str, help="votre nom")
parser.add_argument("--age", default=0, type=int, help="votre age (optionnel)")

args = parser.parse_args()

print(args)

print(f"Bonjour {args.nom} !")
if args.age > 0:
    print(f"Vous avez {args.age} ans.")

