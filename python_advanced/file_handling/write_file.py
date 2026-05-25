#!/usr/bin/env python3
"""Module pour écrire dans un fichier."""


def write_file(filename="", text=""):
    """
    Écrit une chaîne dans un fichier UTF-8.

    Args:
        filename: Nom du fichier
        text: Texte à écrire

    Returns:
        Nombre de caractères écrits
    """
    with open(filename, 'w', encoding='utf-8') as f:
        return f.write(text)
