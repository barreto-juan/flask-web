from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return 'Bem-vindo à página principal'

@app.route('/sobre')
def sobre():
    return 'Bem-vindo à página sobre'

@app.route('/contato')
def contato():
    return 'Bem-vindo à página contato'