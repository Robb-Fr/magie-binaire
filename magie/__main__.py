"""Displays the solution of the card computation"""
from sys import argv

from . import Card

for i in reversed(range(6)):
    print(f"\n\n==== Carte {5-i} ====")
    if len(argv) == 2 and argv[1] == "bin":
        print(Card(i).display(binary=True))
    else:
        print(Card(i).display(binary=False))
