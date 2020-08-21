from flask import Flask, jsonify, request
from habit import Habit
import json

app = Flask(__name__)

habits = [
    Habit("Clean").to_dict(),
    Habit("Work").to_dict(),
    Habit("Run").to_dict(),
    Habit("Sleep").to_dict()
]

@app.route("/habits")
def get_all():
    return jsonify(habits), 200

@app.route("/habits/<int:habit_id>", methods = ["GET"])
def get_one(habitID):
    for i in range(len(habits)):
        if habits[i]["id"] == habitID:
            return habits[i], 200
        
    return "", 404

@app.route("/habits", methods = ["POST"])
def create_habit():

    req = request.get_json()
    h = Habit(req["title"])

    habits.append(h.to_dict())
        
    return h.to_dict(), 201

@app.route("/habits/<int:habit_id>", methods = ["PATCH"])
def update_habit(habit_id):

    req = request.get_json()

    for i in range(len(habits)):
        if habits[i]["id"] == habit_id:
            habits[i]["title"] = req["title"]
            return habits[i], 200
        
    return "", 404

@app.route("/habits/<int:habit_id>", methods = ["DELETE"])
def delete_habit(habit_id):
    for i in range(len(habits)):
        if habits[i]["id"] == habit_id:
            habits.pop(i)
            return jsonify(habits), 200

    return "", 404