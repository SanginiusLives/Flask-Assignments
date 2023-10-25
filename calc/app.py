# Put your app in here.

from flask import Flask, request
from operations import add, sub, mult, div

app = Flask(__name__)

@app.route('/add')
def do_add():
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    calc = add(a, b)

    return str(calc)

@app.route('/sub')
def do_sub():
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    calc = sub(a, b)

    return str(calc)

@app.route('/mult')
def do_mult():
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    calc = mult(a, b)

    return str(calc)


@app.route('/div')
def do_div():
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    calc = div(a, b)

    return str(calc)

operations = {
    "add": add,
    "sub": sub,
    "mult": mult,
    "div": div
}

@app.route('/math/<operation>')
def do_calc(operation):
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    calc = operations[operation](a, b)

    return str(calc)


