import sys
import os


sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from main import cheequear_palabra, adivinar_palabra
import pytest

def test_adivinar_palabra_erronea():
    juego = {
        "palabra": "hola",
        "intentos_restantes": 5,
        "letras_adivinadas": [],
        "letras_erroneas": []
    }
    adivinar_palabra(juego,"chau")
    assert juego == {
        "palabra": "hola",
        "intentos_restantes": 4,
        "letras_adivinadas": [],
        "letras_erroneas": []
    }

def test_adivinar_palabra_correcta():
    juego = {
        "palabra": "hola",
        "intentos_restantes": 4,
        "letras_adivinadas": [],
        "letras_erroneas": []
    }
    adivinar_palabra(juego,"hola")
    assert juego == {
        "palabra": "hola",
        "intentos_restantes": 4,
        "letras_adivinadas": [],
        "letras_erroneas": []
    }


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