#!/usr/bin/env python3
"""Module pour écrire dans un fichier."""


def write_file(filename="", text=""):

    with open(filename, 'w', encoding='utf-8') as f:
        return f.write(text)
