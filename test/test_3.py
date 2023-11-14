from src.ejercicio3 import conjunto_potencia

def test_conjunto_potencia():
    conjunto_original = {6, 1, 4}
    resultado = conjunto_potencia(conjunto_original)
    
    #Verificamos que el conjunto vacio esta en el resultado
    assert set() in resultado
    
    #Verificamos que todos los elementos del conjunto original estan en el resultado
    for elemento in conjunto_original:
        assert {elemento} in resultado
    
    #Verificamos que la longitud del resultado es 2^n (n es la longitud del conjunto original)
    assert len(resultado) == 2 ** len(conjunto_original)