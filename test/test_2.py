from src.ejercicio2 import obtener_nombres_alumnos, mostrar_nombres_alumnos, main
from unittest.mock import patch

def test_obtener_nombres_alumnos():
    with patch('builtins.input', side_effect=['Juan', 'Maria', 'x']):
        nombres = obtener_nombres_alumnos("primaria")
        assert nombres == {'juan', 'maria'}

def test_mostrar_nombres_alumnos(capfd):
    nombres = {'juan', 'maria'}
    mostrar_nombres_alumnos("Prueba", nombres)
    captured = capfd.readouterr()
    assert "Prueba:" in captured.out
    assert "juan" in captured.out
    assert "maria" in captured.out

def test_main(capfd):
    with patch('builtins.input', side_effect=['Juan', 'Maria', 'x', 'Pedro', 'Ana', 'x']):
        main()
        captured = capfd.readouterr()
        assert "Todos los nombres:" in captured.out
        assert "juan" in captured.out
        assert "maria" in captured.out
        assert "pedro" in captured.out
        assert "ana" in captured.out
        assert "Nombres repetidos:" in captured.out
        assert "Nombres de primaria no repetidos en secundaria:" in captured.out
        assert "¿Todos los nombres de primaria estan incluidos en secundaria?" in captured.out