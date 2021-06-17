from flask import Flask, request, jsonify, make_response, render_template
from time import sleep
import random, json

app = Flask(__name__)

from classes import User
users = []
num_users = 0

@app.route("/set_game/", methods=["GET", "POST"])
def set_game():
    if request.method == "GET":
        r = random.randint(1, 2)
        return str(r)
    else:
        pass

@app.route("/players/", methods=["GET", "POST"])
def players():
    if request.method == "GET":
        return render_template('user.html', users=users)

    if request.method == "POST":
        global num_users
        num_users += 1
        user = User()
        user.add(request.json["playerName"], request.json["enemyName"], num_users)
        users.append(user)
        return "Post request!"

@app.route("/", methods=["GET", "POST"])
def home():
    return "Server for chess game!"
