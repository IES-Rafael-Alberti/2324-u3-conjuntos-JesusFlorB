from src.ejercicio5 import obtener_pares, obtener_multiplos_de_tres, obtener_interseccion

def test_obtener_pares():
    assert obtener_pares({1, 2, 3, 4, 5, 6, 7, 8, 9, 10}) == {2, 4, 6, 8, 10}

def test_obtener_multiplos_de_tres():
    assert obtener_multiplos_de_tres({1, 2, 3, 4, 5, 6, 7, 8, 9, 10}) == {3, 6, 9}

def test_obtener_interseccion():
    conjunto1 = {2, 4, 6, 8, 10}
    conjunto2 = {3, 6, 9}
    assert obtener_interseccion(conjunto1, conjunto2) == {6}