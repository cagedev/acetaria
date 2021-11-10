from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/game/{game_id}")
def game(game_id):
    return f"<h1>Game {game_id}</h1>"