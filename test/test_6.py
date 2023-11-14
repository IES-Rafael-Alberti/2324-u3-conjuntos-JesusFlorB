from src.ejercicio6 import obtener_consonantes, obtener_letras_comunes

def test_obtener_consonantes():
    alfabeto = set('abcdefghijklmnopqrstuvwxyz')
    vocales = {'a', 'e', 'i', 'o', 'u'}
    consonantes = obtener_consonantes(alfabeto, vocales)
    assert consonantes == {'b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z'}

def test_obtener_letras_comunes():
    vocales = {'a', 'e', 'i', 'o', 'u'}
    consonantes = {'b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z'}
    letras_comunes = obtener_letras_comunes(vocales, consonantes)
    assert letras_comunes == set()