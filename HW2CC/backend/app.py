from flask import Flask

app = Flask("Football App")


@app.route('/')
def index():
    return 'Hello, World!'
