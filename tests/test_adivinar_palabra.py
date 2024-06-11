import sys
import os


sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from main import cheequear_palabra
import pytest

def test_palabra_incorrecta():
    assert cheequear_palabra("hola","chau") == False

def test_palabra_correcta():
    assert cheequear_palabra("hola","hola") == True  

def test_palabra_correcta_case_sensitive():
    assert cheequear_palabra("hOlA","hola") == True

def test_palabra_correcta_case_sensitive_invertido():
    assert cheequear_palabra("hola","hOlA") == False

def test_palabra_correcta_con_espacios():
    assert cheequear_palabra("    h ol  a   ","hola") == False