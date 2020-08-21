from flask import Flask, jsonify, request, render_template, redirect, url_for, abort, flash
from habit import Habit

app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

habits = [
    Habit("Clean").to_dict(),
    Habit("Work").to_dict(),
    Habit("Run").to_dict(),
    Habit("Sleep").to_dict()
]

@app.route("/habits")
def get_all():
    return render_template("habits.html", habits = habits)

@app.route("/habits/<int:habit_id>", methods = ["GET"])
def get_one(habit_id):
    habit = None

    for i in range(len(habits)):
        if habits[i]["id"] == habit_id:
            habit = habits[i]

    if habit is None:
        abort(404)
    
    return render_template("show_habit.html", habit=habit)

@app.route("/habits", methods = ["POST"])
def create_habit():
    if request.form["title"] == "":
        flash("Error: Title is required!")
        return redirect(url_for("get_all"))

    h = Habit(request.form["title"])

    habits.append(h.to_dict())
        
    return redirect(url_for("get_all"))

@app.route("/habits/edit/<int:habit_id>", methods = ["GET", "POST"])
def edit_habit(habit_id):
    habit = None

    for i in range(len(habits)):
        if habits[i]["id"] == habit_id:
            habit = habits[i]

    if habit is None:
        abort(404)
    
    if request.method == "GET":
        return render_template("edit_habit.html", habit=habit)


    habit["title"] = request.form["title"]

    return redirect(url_for("get_all"))

@app.route("/habits/delete/<int:habit_id>", methods = ["GET", "POST"])
def delete_habit(habit_id):
    for i in range(len(habits)):
        if habits[i]["id"] == habit_id:
            habits.pop(i)
            return redirect(url_for("get_all"))

    return "", 404