import sys
import os


sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from main import verificar_letra,adivinar_letra
import pytest


def test_adivinar_letra_erronea():
    juego = {
        "palabra": "hola",
        "intentos_restantes": 5,
        "letras_adivinadas": ["h"],
        "letras_erroneas": ["p"]
    }
    adivinar_letra(juego,"c")
    assert juego == {
        "palabra": "hola",
        "intentos_restantes": 4,
        "letras_adivinadas": ["h"],
        "letras_erroneas": ["p","c"]
    }

def test_adivinar_letraa_correcta():
    juego = {
        "palabra": "hola",
        "intentos_restantes": 4,
        "letras_adivinadas": ["h"],
        "letras_erroneas": []
    }
    adivinar_letra(juego,"l")
    assert juego == {
        "palabra": "hola",
        "intentos_restantes": 4,
        "letras_adivinadas": ["h","l"],
        "letras_erroneas": []
    }

def test_adivinar_letra_repetida_correcta():
    juego = {
        "palabra": "hola",
        "intentos_restantes": 5,
        "letras_adivinadas": ["h"],
        "letras_erroneas": ["p"]
    }
    adivinar_letra(juego,"h")
    assert juego == {
        "palabra": "hola",
        "intentos_restantes": 4,
        "letras_adivinadas": ["h"],
        "letras_erroneas": ["p"]
    }


def test_adivinar_letra_repetida_erronea():
    juego = {
        "palabra": "hola",
        "intentos_restantes": 5,
        "letras_adivinadas": ["h"],
        "letras_erroneas": ["p"]
    }
    adivinar_letra(juego,"p")
    assert juego == {
        "palabra": "hola",
        "intentos_restantes": 4,
        "letras_adivinadas": ["h"],
        "letras_erroneas": ["p"]
    }

def test_adivinar_letra_doble():
    juego = {
        "palabra": "oso",
        "intentos_restantes": 4,
        "letras_adivinadas": [],
        "letras_erroneas": ["p"]
    }
    adivinar_letra(juego,"o")
    assert juego == {
        "palabra": "oso",
        "intentos_restantes": 4,
        "letras_adivinadas": ["o"],
        "letras_erroneas": ["p"]
    }

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
