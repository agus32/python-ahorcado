from '../main' import generar_palabra
import pytest

def test_palabra_vacio():
    assert generar_palabra("") == False

def test_palabra_con_mayuscula():
    assert generar_palabra("Juan") == False

def test_palabra_con_espacios():
    assert generar_palabra("   Ana   ") == False

def test_palabra_con_caracteres_especiales():
    assert generar_palabra("M@ría") == False

def test_palabra_con_numeros():
    assert generar_palabra("Pedro123") == False

def test_palabra_con_simbolos():
    assert generar_palabra("!@#$%") == False

def test_palabra_con_longitud_maxima():
    assert generar_palabra("abcdefghijklmnopqrstuvwxyz") == True

def test_palabra_con_longitud_excedida():
    assert generar_palabra("abcdefghijklmnopqrstuvwxyzA") == False

def test_palabra_con_longitud_minima():
    assert generar_palabra("pa") == False

def test_palabra_correcta():
    assert generar_palabra("palangana") == True

def test_nombre_con_tilde():
    assert generar_palabra("ramíro") == False

def test_palabra_mas_palabras():
    assert generar_palabra("martin genaro") == False