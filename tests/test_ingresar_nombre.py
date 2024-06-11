import sys
import os


sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from main import verificar_nombre
import pytest

def test_nombre_vacio():
    assert verificar_nombre("") == False

def test_nombre_correcto():
    assert verificar_nombre("Juan") == True

def test_nombre_con_espacios_a_los_costados():
    assert verificar_nombre("   Ana   ") == False

def test_nombre_con_espacios_entre_letras():
    assert verificar_nombre("J u a n") == True

def test_nombre_con_caracteres_especiales():
    assert verificar_nombre("M@r.a") == False

def test_nombre_con_tilde():
    assert verificar_nombre("María") == True

def test_nombre_con_numeros():
    assert verificar_nombre("Pedro123") == True

def test_nombre_con_simbolos():
    assert verificar_nombre("!@#$%") == False

def test_nombre_con_longitud_maxima(): #20 caracteres
    assert verificar_nombre("abcdefghijklmnopqrst") == True

def test_nombre_con_longitud_minima():
    assert verificar_nombre("ab") == False

def test_nombre_con_longitud_excedida():
    assert verificar_nombre("abcdefghijklmnopqrstu") == False



