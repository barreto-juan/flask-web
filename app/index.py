from flask import Flask, render_template, request
from random import randint

app = Flask(__name__)

@app.route('/', methods = ["GET", "POST"])
def index():
    variavel = 'Acerte o número'

    if request.method == "GET":
        return render_template("index.html", variavel=variavel)
    else:
        numero = randint(1, 9)
        palpite = int(request.form.get("name"))

        if numero == palpite:
            return f'N: {numero} <h2>Você acertou</h2>'
        else:
            return f'N: {numero} <h2>Você errou</h2>'

@app.route('/<string:nome>')
def error(nome):
    variavel = f'Página "{nome}" não encontrada!'
    return render_template("error.html", variavel=variavel)