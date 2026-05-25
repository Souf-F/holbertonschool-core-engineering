#!/usr/bin/python3
"""Module de validation UTF-8."""


def validUTF8(data):
    """Valide si data représente un encodage UTF-8 valide."""

    n_bytes = 0

    for num in data:
        byte = num & 0xFF

        if n_bytes == 0:
            if byte >> 7 == 0:
                n_bytes = 0
            elif byte >> 5 == 0b110:
                n_bytes = 1
            elif byte >> 4 == 0b1110:
                n_bytes = 2
            elif byte >> 3 == 0b11110:
                n_bytes = 3
            else:
                return False
        else:
            if byte >> 6 != 0b10:
                return False
            n_bytes -= 1

    return n_bytes == 0
