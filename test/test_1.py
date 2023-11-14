from src.ejercicio1 import obtener_domicilios

def test_obtener_domicilios():
    #Datos de compras
    compras = [
        ("Nuria Costa", 5, 12780.78, "Calle Las Flores 355"),
        ("Jorge Russo", 7, 699, "Mirasol 218"),
        ("Nuria Costa", 7, 532.90, "Calle Las Flores 355"),
        ("Julian Rodriguez", 12, 5715.99, "La Mancha 761"),
        ("Jorge Russo", 15, 958, "Mirasol 218")
    ]

    #Llamamos a la función a probar
    domicilios_facturacion = obtener_domicilios(compras)

    #Verificamos los resultados
    assert len(domicilios_facturacion) == 3
    assert "Calle Las Flores 355" in domicilios_facturacion
    assert "Mirasol 218" in domicilios_facturacion
    assert "La Mancha 761" in domicilios_facturacion