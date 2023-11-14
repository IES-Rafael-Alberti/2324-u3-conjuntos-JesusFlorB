"""Solicitar al usuario que introduzca los nombres de pila de los alumnos de primaria de una escuela, finalizando cuando se introduzca “x”. 
A continuación, solicitar que introduzca los nombres de los alumnos de secundaria, finalizando al introducir “x”.

Mostrar los nombres de todos los alumnos de primaria y los de secundaria, sin repeticiones.
Mostrar qué nombres se repiten entre los alumnos de primaria y secundaria.
Mostrar qué nombres de primaria no se repiten en los de nivel secundaria.
Mostrar si todos los nombres de primaria están incluidos en secundaria."""

def obtener_nombres_alumnos(nivel):
    """
    Solicita al usuario introducir nombres de alumnos hasta que se ingrese "x".

    Args:
        nivel (str): Nivel educativo, "primaria" o "secundaria".

    Returns:
        set: Un conjunto de nombres de alumnos para el nivel especificado.
    """
    nombres = set()
    nombre = input(f"Ingrese el nombre de un alumno de {nivel} (o 'x' para terminar): ").strip().lower()

    while nombre != 'x':
        nombres.add(nombre)
        nombre = input(f"Ingrese el nombre de un alumno de {nivel} (o 'x' para terminar): ").strip().lower()

    return nombres

def mostrar_nombres_alumnos(titulo, nombres):
    """
    Muestra los nombres de los alumnos.

    Args:
        titulo (str): Título para la seccion.
        nombres (set): Conjunto de nombres de alumnos.
    """
    print(f"\n{titulo}:")
    for nombre in nombres:
        print(nombre)

def main():
    #Obtener nombres de alumnos de primaria
    nombres_primaria = obtener_nombres_alumnos("primaria")

    #Obtener nombres de alumnos de secundaria
    nombres_secundaria = obtener_nombres_alumnos("secundaria")

    #Mostrar nombres de todos los alumnos de primaria y secundaria sin repeticiones
    todos_los_nombres = nombres_primaria.union(nombres_secundaria)
    mostrar_nombres_alumnos("Todos los nombres", todos_los_nombres)

    #Mostrar nombres que se repiten entre primaria y secundaria
    nombres_repetidos = nombres_primaria.intersection(nombres_secundaria)
    mostrar_nombres_alumnos("Nombres repetidos", nombres_repetidos)

    #Mostrar nombres de primaria que no se repiten en secundaria
    nombres_primaria_no_repetidos = nombres_primaria - nombres_secundaria
    mostrar_nombres_alumnos("Nombres de primaria no repetidos en secundaria", nombres_primaria_no_repetidos)

    #Mostrar si todos los nombres de primaria estan incluidos en secundaria
    todos_en_secundaria = nombres_primaria.issubset(nombres_secundaria)
    print("\n¿Todos los nombres de primaria estan incluidos en secundaria?:", "Si" if todos_en_secundaria else "No")

if __name__ == "__main__":

    main()