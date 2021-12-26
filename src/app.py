from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return "Bye Jkod!"

@app.route('/hello')
def greeting():
    return "Hello World"

@app.route('/sum/<int:a>/<int:b>')
def sum(a: int, b: int):
    nums_sum = a + b
    return f"La suma es: {str(nums_sum)}"

@app.route('/multiply/<int:a>/<int:b>')
def multiply(a: int, b: int):
    result = float(a * b)
    return f"Resultado de la multiplicación: {str(result)}"
