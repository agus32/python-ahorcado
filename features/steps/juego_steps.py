from behave import given, when, then
from main import app, inicializar_juego, dibujar_palabra, adivinar_letra, adivinar_palabra
from flask.testing import FlaskClient

@given('I have a valid word "{word}"')
def step_impl(context, word):
    context.word = word
    context.juego = inicializar_juego(word)
    context.client = app.test_client()

@when('I start the game')
def step_impl(context):
    with context.client.session_transaction() as session:
        session['juego'] = context.juego

@then('I should see the masked word "{masked_word}"')
def step_impl(context, masked_word):
    response = context.client.get('/juego')
    assert dibujar_palabra(context.juego['letras_adivinadas'], context.word) == masked_word

@when('I guess the letter "{letter}"')
def step_impl(context, letter):
    adivinar_letra(context.juego, letter)

@then('I should see "{masked_word}"')
def step_impl(context, masked_word):
    assert dibujar_palabra(context.juego['letras_adivinadas'], context.word) == masked_word

@when('I guess the word "{guess}"')
def step_impl(context, guess):
    adivinar_palabra(context.juego, guess)

@then('the remaining attempts should be {attempts:d}')
def step_impl(context, attempts):
    assert context.juego['intentos_restantes'] == attempts
