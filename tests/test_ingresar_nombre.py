from '../main' import verificar_nombre
import pytest

def test_nombre_vacio():
    assert verificar_nombre("") == False

def test_nombre_correcto():
    assert verificar_nombre("Juan") == True

def test_nombre_con_espacios():
    assert verificar_nombre("   Ana   ") == True

def test_nombre_con_caracteres_especiales():
    assert verificar_nombre("M@ría") == False

def test_nombre_con_numeros():
    assert verificar_nombre("Pedro123") == True

def test_nombre_con_simbolos():
    assert verificar_nombre("!@#$%") == True

def test_nombre_con_longitud_maxima():
    assert verificar_nombre("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ") == True

def test_nombre_con_longitud_excedida():
    assert verificar_nombre("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1") == False



