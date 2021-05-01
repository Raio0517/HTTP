from flask import Flask, render_template, request
from random import choice

app = Flask(__name__)

@app.route("/")
def index():
  return render_template("index.html")

@app.route("/factorial/<number>")
def factorial(number):
  fact = 1
  for i in range(1, int(number)+1):
    fact = fact * i 
  return str(fact)

app.run(host='0.0.0.0', port=8080)