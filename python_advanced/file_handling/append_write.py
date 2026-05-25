#!/usr/bin/env python3
"""Module pour ajouter du texte à un fichier."""


def append_write(filename="", text=""):
    """
    Ajoute une chaîne à la fin d'un fichier UTF-8.

    Args:
        filename: Nom du fichier
        text: Texte à ajouter

    Returns:
        Nombre de caractères ajoutés
    """
    with open(filename, 'a', encoding='utf-8') as f:
        return f.write(text)
