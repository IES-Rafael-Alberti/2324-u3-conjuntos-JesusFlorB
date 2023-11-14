"""El conjunto potencia de un conjunto S es el conjunto de todos los subconjuntos de S.

Por ejemplo, el conjunto potencia de {1,2,3} es:

{∅,{1},{2},{3},{1,2},{1,3},{2,3},{1,2,3}}

Escriba la función conjunto_potencia(s) que reciba como parámetro un conjunto cualquiera s y retorne su «lista potencia» 
(la lista de todos sus subconjuntos):

>>> conjunto_potencia({6, 1, 4})
[set(), set([6]), set([1]), set([4]), set([6, 1]), set([6, 4]), set([1, 4]), set([6, 1, 4])]"""

def conjunto_potencia(s):
    """
    Retorna la lista de todos los subconjuntos del conjunto.

    Args:
        s (set): Conjunto de entrada.

    Returns:
        list: Lista de todos los subconjuntos.
    """
    #Inicializamos la lista de subconjuntos con el conjunto vacio
    potencia = [set()]

    #Generar los subconjuntos para cada elemento en el conjunto original
    for elemento in s:
        nuevos_subconjuntos = [subconjunto | {elemento} for subconjunto in potencia]
        potencia.extend(nuevos_subconjuntos)

    return potencia

if __name__ == "__main__":

    conjunto_original = {6, 1, 4}
    resultado = conjunto_potencia(conjunto_original)
    print(resultado)