"""Dadas las siguientes listas:

frutas1 = ["manzana", "pera", "naranja", "plátano", "uva"]
frutas2 = ["manzana", "pera", "durazno", "sandía", "uva"]

Crea conjuntos a partir de estas listas y nómbralos set_frutas1 y set_frutas2.
Encuentra las frutas que están en ambas listas y guárdalas en un nuevo conjunto llamado frutas_comunes.
Encuentra las frutas que están en frutas1 pero no en frutas2 y guárdalas en un conjunto llamado frutas_solo_en_frutas1.
Encuentra las frutas que están en frutas2 pero no en frutas1 y guárdalas en un conjunto llamado frutas_solo_en_frutas2."""

def crear_conjuntos(lista1, lista2):
    """
    Crea conjuntos a partir de dos listas y los retorna.

    Args:
        lista1 (list): Primera lista de frutas.
        lista2 (list): Segunda lista de frutas.

    Returns:
        tuple: Tupla con dos conjuntos creados a partir de las listas.
    """
    set_frutas1 = set(lista1)
    set_frutas2 = set(lista2)
    return set_frutas1, set_frutas2

def encontrar_frutas_comunes(set1, set2):
    """
    Encuentra las frutas comunes entre dos conjuntos y las retorna.

    Args:
        set1 (set): Primer conjunto de frutas.
        set2 (set): Segundo conjunto de frutas.

    Returns:
        set: Conjunto con las frutas comunes.
    """
    return set1.intersection(set2)

def encontrar_frutas_solo_en(set1, set2):
    """
    Encuentra las frutas que estan en el primer conjunto pero no en el segundo y las retorna.

    Args:
        set1 (set): Primer conjunto de frutas.
        set2 (set): Segundo conjunto de frutas.

    Returns:
        set: Conjunto con las frutas solo en el primer conjunto.
    """
    return set1.difference(set2)

def mostrar_resultados(frutas_comunes, frutas_solo_en_1, frutas_solo_en_2):
    """
    Muestra los resultados de las operaciones.

    Args:
        frutas_comunes (set): Conjunto de frutas comunes.
        frutas_solo_en_1 (set): Conjunto de frutas solo en el primer conjunto.
        frutas_solo_en_2 (set): Conjunto de frutas solo en el segundo conjunto.
    """
    print("Frutas comunes:", frutas_comunes)
    print("Frutas solo en frutas1:", frutas_solo_en_1)
    print("Frutas solo en frutas2:", frutas_solo_en_2)

if __name__ == "__main__":

    #Listas originales
    frutas1 = ["manzana", "pera", "naranja", "platano", "uva"]
    frutas2 = ["manzana", "pera", "durazno", "sandía", "uva"]

    #Llamadas a funciones
    set_frutas1, set_frutas2 = crear_conjuntos(frutas1, frutas2)
    frutas_comunes = encontrar_frutas_comunes(set_frutas1, set_frutas2)
    frutas_solo_en_frutas1 = encontrar_frutas_solo_en(set_frutas1, set_frutas2)
    frutas_solo_en_frutas2 = encontrar_frutas_solo_en(set_frutas2, set_frutas1)

    #Mostrar resultados
    mostrar_resultados(frutas_comunes, frutas_solo_en_frutas1, frutas_solo_en_frutas2)