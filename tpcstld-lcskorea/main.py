from flask import Flask
app = Flask(__name__)
app.debug = True

@app.route('/')
def show_chart():
    return "Hello, World"
