from src.ejercicio4 import crear_conjuntos, encontrar_frutas_comunes, encontrar_frutas_solo_en

def test_crear_conjuntos():
    lista1 = ["manzana", "pera", "naranja", "platano", "uva"]
    lista2 = ["manzana", "pera", "durazno", "sandia", "uva"]
    set_frutas1, set_frutas2 = crear_conjuntos(lista1, lista2)
    assert set_frutas1 == {"manzana", "pera", "naranja", "platano", "uva"}
    assert set_frutas2 == {"manzana", "pera", "durazno", "sandia", "uva"}

def test_encontrar_frutas_comunes():
    set_frutas1 = {"manzana", "pera", "naranja", "platano", "uva"}
    set_frutas2 = {"manzana", "pera", "durazno", "sandia", "uva"}
    frutas_comunes = encontrar_frutas_comunes(set_frutas1, set_frutas2)
    assert frutas_comunes == {"manzana", "pera", "uva"}

def test_encontrar_frutas_solo_en():
    set_frutas1 = {"manzana", "pera", "naranja", "platano", "uva"}
    set_frutas2 = {"manzana", "pera", "durazno", "sandia", "uva"}
    frutas_solo_en_frutas1 = encontrar_frutas_solo_en(set_frutas1, set_frutas2)
    frutas_solo_en_frutas2 = encontrar_frutas_solo_en(set_frutas2, set_frutas1)
    assert frutas_solo_en_frutas1 == {"naranja", "platano"}
    assert frutas_solo_en_frutas2 == {"durazno", "sandia"}