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

@app.route("/post_to/", methods=['GET', 'POST'])
def post():
    if request.method ==  "GET":
        return render_template('browser_send.html')
    
    if request.method == "POST":
        global num_users
        num_users += 1
        #user = User()
        #user.add(request.json["playerName"], request.json["enemyName"], num_users, request.remote_addr)
        #user.append(user)
        print(request.json)
        #name = request.form['name']
        return "Post"

@app.route("/check_enemy/", methods=['GET', 'POST'])
def check():
    for user in users:
        for enemy in users:
            if enemy.username == user.enemy:
                return "There is your enemy"
    return "There isn't your enemy!"

@app.route("/players/", methods=["GET", "POST"])
def players():
    if request.method == "GET":
        return render_template('user.html', users=users)

    if request.method == "POST":
        global num_users
        num_users += 1
        user = User()
        user.add(request.json["playerName"], request.json["enemyName"], num_users, request.remote_addr)
        users.append(user)
        return "Post request!"

@app.route("/", methods=["GET", "POST"])
def home():
    return "Server for chess game!"
