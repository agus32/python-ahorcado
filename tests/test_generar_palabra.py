from '../main' import generar_palabra
import pytest

def test_palabra_vacio():
    assert verificar_nombre("") == False

def test_palabra_con_mayuscula():
    assert verificar_nombre("Juan") == False

def test_palabra_con_espacios():
    assert verificar_nombre("   Ana   ") == False

def test_palabra_con_caracteres_especiales():
    assert verificar_nombre("M@ría") == False

def test_palabra_con_numeros():
    assert verificar_nombre("Pedro123") == False

def test_palabra_con_simbolos():
    assert verificar_nombre("!@#$%") == False

def test_palabra_con_longitud_maxima():
    assert verificar_nombre("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ") == False

def test_palabra_con_longitud_excedida():
    assert verificar_nombre("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1") == False

def test_palabra_con_longitud_minima():
    assert verificar_nombre("pa") == False

def test_palabra_correcta():
    assert verificar_nombre("palangana") == True

def test_nombre_con_tilde():
    assert verificar_nombre("ramíro") == false

def test_palabra_mas_palabras():
    assert verificar_nombre("martin genaro") == false