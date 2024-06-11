import re


def initialize_game(word):
    return {
        "word": word,
        "attempts_left": 6,
        "guessed_letters": [],
        "wrong_guesses": []
    }



def generar_palabra(palabra):
    # Verificar si la palabra está vacía
    if not palabra:
        return False

    # Eliminar espacios al principio y al final
    palabra = palabra.strip()

    # Verificar longitud mínima y máxima
    if len(palabra) < 3 or len(palabra) > 26:
        return False

    # Verificar si la palabra contiene solo letras minúsculas y no tiene espacios o caracteres especiales
    if not re.match("^[a-z]+$", palabra):
        return False

    return True


def cheequear_palabra(palabra, adivinanza):
    def normalizar(texto):
        return ''.join(filter(str.isalpha, texto.lower()))

    palabra_normalizada = normalizar(palabra)
    adivinanza_normalizada = normalizar(adivinanza)

    return palabra_normalizada == adivinanza_normalizada





def verificar_nombre(nombre):
    # Verificamos que el nombre no esté vacío.
    if not nombre:
        return False
    
    # Eliminamos espacios al inicio y al final.
    nombre = nombre.strip()
    
    # Verificamos que el nombre tenga la longitud adecuada.
    if len(nombre) < 3 or len(nombre) > 20:
        return False
    
    # Permitimos espacios entre letras y números.
    if not re.match(r'^[a-zA-ZáéíóúÁÉÍÓÚüÜñÑ0-9\s]+$', nombre):
        return False
    
    # Verificamos que no haya espacios al inicio ni al final.
    if nombre != nombre.strip():
        return False
    
    return True


def verificar_letra(letra, palabra):
    # Verificamos que la letra sea un solo caracter.
    if len(letra) != 1:
        return False
    
    # Verificamos que la letra sea alfabética.
    if not letra.isalpha():
        return False
    
    # Verificamos que la letra sea minúscula.
    if not letra.islower():
        return False
    
    # Verificamos que la letra no haya sido ingresada previamente.
    if letra in palabra:
        return False
    
    return True