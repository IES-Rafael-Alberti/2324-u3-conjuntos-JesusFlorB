"""Dado el conjunto de números enteros:

numeros = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}

Crea un conjunto pares que contenga los números pares del conjunto numeros.
Crea un conjunto multiplos_de_tres que contenga los números que son múltiplos de tres del conjunto numeros.
Encuentra la intersección entre los conjuntos pares y multiplos_de_tres y guárdala en un conjunto llamado pares_y_multiplos_de_tres."""

def obtener_pares(numeros):
    """
    Retorna un conjunto con los numeros pares del conjunto dado.

    Args:
        numeros (set): Conjunto de numeros enteros.

    Returns:
        set: Conjunto de numeros pares.
    """
    return {num for num in numeros if num % 2 == 0}

def obtener_multiplos_de_tres(numeros):
    """
    Retorna un conjunto con los numeros multiplos de tres del conjunto dado.

    Args:
        numeros (set): Conjunto de numeros enteros.

    Returns:
        set: Conjunto de numeros multiplos de tres.
    """
    return {num for num in numeros if num % 3 == 0}

def obtener_interseccion(conjunto1, conjunto2):
    """
    Retorna la interseccion entre dos conjuntos.

    Args:
        conjunto1 (set): Primer conjunto.
        conjunto2 (set): Segundo conjunto.

    Returns:
        set: Interseccion entre los conjuntos.
    """
    return conjunto1.intersection(conjunto2)

def main():

    numeros = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
    
    pares = obtener_pares(numeros)
    multiplos_de_tres = obtener_multiplos_de_tres(numeros)
    interseccion = obtener_interseccion(pares, multiplos_de_tres)

    print("Conjunto de numeros pares:", pares)
    print("Conjunto de multiplos de tres:", multiplos_de_tres)
    print("Interseccion entre pares y multiplos de tres:", interseccion)

if __name__ == "__main__":
    
    main()