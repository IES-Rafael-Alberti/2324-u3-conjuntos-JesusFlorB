"""Dado el conjunto de letras:

vocales = {'a', 'e', 'i', 'o', 'u'}

Crea un conjunto consonantes que contenga las letras del alfabeto que no son vocales.
Crea un conjunto letras_comunes que contenga las letras que están tanto en el conjunto vocales como en el conjunto consonantes."""

def obtener_consonantes(alfabeto, vocales):
    """
    Retorna un conjunto con las letras del alfabeto que no son vocales.

    Args:
        alfabeto (set): Conjunto de letras del alfabeto.
        vocales (set): Conjunto de vocales.

    Returns:
        set: Conjunto de consonantes.
    """
    return alfabeto - vocales

def obtener_letras_comunes(vocales, consonantes):
    """
    Retorna un conjunto con las letras comunes entre vocales y consonantes.

    Args:
        vocales (set): Conjunto de vocales.
        consonantes (set): Conjunto de consonantes.

    Returns:
        set: Conjunto de letras comunes.
    """
    return vocales.intersection(consonantes)

def main():
    alfabeto = set('abcdefghijklmnñopqrstuvwxyz')
    vocales = {'a', 'e', 'i', 'o', 'u'}

    consonantes = obtener_consonantes(alfabeto, vocales)
    letras_comunes = obtener_letras_comunes(vocales, consonantes)

    print("Conjunto de consonantes:", consonantes)
    print("Conjunto de letras comunes:", letras_comunes)

if __name__ == "__main__":

    main()