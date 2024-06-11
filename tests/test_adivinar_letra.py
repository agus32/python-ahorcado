import sys
import os


sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from main import verificar_letra
import pytest

def test_letra_vacia():
    assert verificar_letra("", "hola") == False

def test_letra_mas_de_una():
    assert verificar_letra("as", "hola") == False

def test_correcto():
    assert verificar_letra("a", "hola") == True

def test_letra_mayuscula():
    assert verificar_letra("A", "hola") == True

def test_letra_con_tilde():
    assert verificar_letra("á", "hola") == False

def test_letra_especial():
    assert verificar_letra("%", "hola") == False
