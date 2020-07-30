from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello():
    return 'Hello, World! <a href="/contacts">Контакты</a>'


@app.route("/contacts")
def contacts():
    return 'email: 123@mail.ru <a href="/">Назад</a>'


app.run()
