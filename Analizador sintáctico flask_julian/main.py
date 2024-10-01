from flask import Flask, request, render_template
from lexer import analizar_codigo
from parser import analizar_sintaxis

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    resultado_lexico = []
    resultado_sintactico = []

    if request.method == 'POST':
        codigo = request.form['codigo']
        resultado_lexico = analizar_codigo(codigo)
        resultado_sintactico = analizar_sintaxis(codigo)

    return render_template('index.html', resultado_lexico=resultado_lexico, resultado_sintactico=resultado_sintactico)

if __name__ == '__main__':
    app.run(debug=True)