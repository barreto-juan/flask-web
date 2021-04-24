from flask import Flask, render_template, request
from random import randint

app = Flask(__name__)

@app.route('/', methods = ["GET", "POST"])
def index():
    variavel = 'Quiz Python'

    if request.method == "GET":
        return render_template("index.html", variavel=variavel)
    else:
        array = ['A', 'A', 'C']
        a = request.form.get("questao1")
        b = request.form.get("questao2")
        c = request.form.get("questao3")
        

        respostas = [a, b, c]
        cont = 0
        for i in range(3):
            if array[i] == respostas[i]:
                cont+=1

        return f'<h2>Você acertou {cont} respostas!</h2>'
        
@app.route('/<string:nome>')
def error(nome):
    variavel = f'Página "{nome}" não encontrada!'
    return render_template("error.html", variavel=variavel)