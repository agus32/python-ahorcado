import re


def initializar_juego(palabra):
    return {
        "palabra": palabra,
        "intentos_restantes": 5,
        "letras_adivinadas": [],
        "letras_erroneas": []
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
    return palabra.lower() == adivinanza




def verificar_nombre(nombre):
    aux  = nombre.replace(" ", "")
    if aux != nombre:
        return False
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
    if len(letra) == 0:
        return False

    if letra.lower() in palabra:
        return True
    return False

def dibujar_palabra(lista, palabra):
    espacios = ["_"] * len(palabra)

    for l in lista:
        for i, p in enumerate(palabra):
            if l == p:
                espacios[i] = l 

    return "".join(espacios) 


def adivinar_letra(juego, letra):
    # La letra ya ha sido adivinada (correcta o incorrectamente)
    if letra in juego["letras_adivinadas"] or letra in juego["letras_erroneas"]:
        juego["intentos_restantes"] -= 1
        return

    # La letra es parte de la palabra a adivinar
    if letra in juego["palabra"]:
        juego["letras_adivinadas"].append(letra)
    else:
        juego["letras_erroneas"].append(letra)
        juego["intentos_restantes"] -= 1
