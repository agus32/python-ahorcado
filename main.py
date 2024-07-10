from flask import Flask, render_template, request, redirect, url_for, session
import re
import os

app = Flask(__name__)
app.secret_key = os.urandom(24)


def inicializar_juego(palabra):
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

def adivinar_palabra(juego, adivinanza):
    if not cheequear_palabra(juego["palabra"], adivinanza):
        juego["intentos_restantes"] -= 1


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
    if letra.lower() in palabra and len(letra) == 1:
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
    if letra in juego["letras_erroneas"] or letra in juego["letras_adivinadas"]:
        juego["intentos_restantes"] -= 1
        return

    # La letra es parte de la palabra a adivinar
    if verificar_letra(letra, juego["palabra"]):
        juego["letras_adivinadas"].append(letra)
    else:
        juego["letras_erroneas"].append(letra)
        juego["intentos_restantes"] -= 1


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        palabra = request.form['palabra']
        if generar_palabra(palabra):
            session['juego'] = inicializar_juego(palabra)
            return redirect(url_for('juego'))
        else:
            error = "Palabra no válida. Debe tener entre 3 y 26 letras y no contener caracteres especiales."
            return render_template('index.html', error=error)
    return render_template('index.html')

@app.route('/juego', methods=['GET', 'POST'])
def juego():
    juego = session.get('juego', None)
    if not juego:
        return redirect(url_for('index'))

    mensaje = None
    if request.method == 'POST':
        opcion = request.form['opcion']
        if opcion == 'letra':
            letra = request.form['letra'].strip().lower()
            if len(letra) != 1 or not letra.isalpha():
                mensaje = "Entrada no válida. Ingresa una sola letra."
            else:
                adivinar_letra(juego, letra)
        elif opcion == 'palabra':
            adivinanza = request.form['adivinanza'].strip().lower()
            adivinar_palabra(juego, adivinanza)
            if cheequear_palabra(juego["palabra"], adivinanza):
                mensaje = "¡Has adivinado la palabra!"
                session['juego'] = juego
                return render_template('juego.html', juego=juego, palabra_completa=True, mensaje=mensaje, dibujar_palabra=dibujar_palabra)
        else:
            mensaje = "Opción no válida. Elige 'letra' o 'palabra'."

    if "_" not in dibujar_palabra(juego["letras_adivinadas"], juego["palabra"]):
        mensaje = f"¡Felicidades! Has adivinado la palabra: {juego['palabra']}"
        return render_template('juego.html', juego=juego, palabra_completa=True, mensaje=mensaje, dibujar_palabra=dibujar_palabra)
    elif juego["intentos_restantes"] <= 0:
        mensaje = f"Se han acabado los intentos. La palabra era: {juego['palabra']}"
        return render_template('juego.html', juego=juego, palabra_completa=True, mensaje=mensaje, dibujar_palabra=dibujar_palabra)

    session['juego'] = juego
    return render_template('juego.html', juego=juego, mensaje=mensaje, dibujar_palabra=dibujar_palabra)

if __name__ == '__main__':
    app.run(debug=True)