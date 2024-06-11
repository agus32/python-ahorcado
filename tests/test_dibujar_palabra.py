import sys
import os


sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from main import dibujar_palabra
import pytest

def test_dibujar_palabra_falta_ultima():
    assert dibujar_palabra("cha","chau") == "cha_"

def test_dibujar_palabra_falta_primera():
    assert dibujar_palabra("hau","chau") == "_hau"

def test_dibujar_palabra_faltan_dos():
    assert dibujar_palabra("cu","chau") == "c__u"

def test_dibujar_palabra_dos_iguales():
    assert dibujar_palabra("o","oso") == "o_o"

def test_dibujar_palabra_todas_iguales():
    assert dibujar_palabra("nazreo","nazareno") == "nazareno"

def test_dibujar_palabra_distinto_orden():
    assert dibujar_palabra("oerzan","nazareno") == "nazareno"

def test_dibujar_palabra_distinto_orden_errado():
    assert dibujar_palabra("al","palo") == "_al_"