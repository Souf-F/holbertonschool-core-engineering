#!/usr/bin/env python3
"""Module pour lire un fichier."""


def read_file(filename=""):
    """Lit un fichier UTF-8 et l'affiche sur stdout."""
    with open(filename, 'r', encoding='utf-8') as f:
        print(f.read(), end='')
