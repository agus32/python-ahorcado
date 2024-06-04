from '../main' import adivinar_palabra
import pytest

def test_palabra_incorrecta():
    assert adivinar_palabra("hola","chau") == False

def test_palabra_correcta():
    assert adivinar_palabra("hola","hola") == True  

def test_palabra_correcta_case_sensitive():
    assert adivinar_palabra("hOlA","hola") == True

def test_palabra_correcta_case_sensitive_invertido():
    assert adivinar_palabra("hola","hOlA") == True

