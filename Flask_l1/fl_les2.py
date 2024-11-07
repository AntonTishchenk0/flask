from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    return 'Привет, незнакомец!'


@app.route('/Антон/')
def anton():
    return 'Привет, Антон!'


@app.route('/Иван/')
def ivan():
    return 'Привет, Иван!'


if __name__ == '__main__':
    app.run(debug=True)
    