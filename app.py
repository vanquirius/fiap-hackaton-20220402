# coding=utf-8
# Hackaton FIAP
# Enilson dos Santos Jr., Klaus Araújo, Lilian Barbosa, Marcelo Góes,
# Müller Silva, Nicolas Osmundo, Roberto Ribeiro, Vinicius Montouro
# 2022-04-02

# teste teste

from flask import Flask
from flask_wtf.csrf import CSRFProtect
import os

app = Flask(__name__)
csrf = CSRFProtect(app)
csrf.init_app(app)

@app.route("/")
def pagina_inicial():
    return "Hello Hackaton!"

if __name__ == '__main__':
#    app.run()
    port = os.getenv('PORT')
    app.run('0.0.0.0', port=port)