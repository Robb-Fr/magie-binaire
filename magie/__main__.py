"""Displays the solution of the card computation"""
import argparse
from . import all_cards

parser = argparse.ArgumentParser(
                    prog='Magie Binaire',
                    description="Ce programme permet d'afficher les cartes dont il est question dans l'activité magie-binaire de modulo",
                    epilog='https://enseigner.modulo-info.ch/rep-info/activ/magie_binaire.html')

parser.add_argument("-b", "--bin", action="store_true", help="Si cette option est activée, les nombres seront affichés en format binaire. Sinon ils le seront en format décimal")
args = parser.parse_args()

for i in reversed(range(6)):
    print(f"\n\n==== Carte {5-i} ====")
    if args.bin:
        print(all_cards[i].display(binary=True))
    else:
        print(all_cards[i].display(binary=False))
