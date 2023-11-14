"""Suponer una lista con datos de las compras hechas por clientes de una empresa a lo largo de un mes, la cual contiene tuplas con información de cada venta: (cliente, día del mes, monto, domicilio del cliente). Ejemplo:

[("Nuria Costa", 5, 12780.78, "Calle Las Flores 355"), ("Jorge Russo", 7, 699, "Mirasol 218"), ("Nuria Costa", 7, 532.90, "Calle Las Flores 355"), ("Julián Rodriguez", 12, 5715.99, "La Mancha 761"), ("Jorge Russo", 15, 958, "Mirasol 218")]

Escribir una función que reciba como parámetro una lista con el formato mencionado anteriormente 
y retorne los domicilios de cada cliente al cual se le debe enviar una factura de compra. 
Notar que cada cliente puede haber hecho más de una compra en el mes, por lo que la función debe retornar una estructura 
que contenga cada domicilio una sola vez."""


def obtener_domicilios(compras):
    """
    Obtiene una lista unica de domicilios de clientes a los cuales se les debe enviar una factura.

    Args:
        compras (list): Lista de tuplas con informacion de compras (cliente, día del mes, monto, domicilio).

    Returns:
        list: Lista unica de domicilios de clientes para enviar facturas.
    """
    
    domicilios = set()  #Utilizamos un conjunto para evitar duplicados

    for compra in compras:
        cliente, _, _, domicilio = compra
        domicilios.add(domicilio)

    return list(domicilios)  #Convertimos el conjunto a lista

if __name__ == '__main__':

    lista_compras = [
        ("Nuria Costa", 5, 12780.78, "Calle Las Flores 355"),
        ("Jorge Russo", 7, 699, "Mirasol 218"),
        ("Nuria Costa", 7, 532.90, "Calle Las Flores 355"),
        ("Julian Rodriguez", 12, 5715.99, "La Mancha 761"),
        ("Jorge Russo", 15, 958, "Mirasol 218")
    ]

    domicilios_facturacion = obtener_domicilios(lista_compras)

    print("Domicilios:")
    for domicilio in domicilios_facturacion:
        print(domicilio)