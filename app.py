from flask import Flask, jsonify, request, render_template, redirect, url_for, abort, flash
from habit import Habit
import mysql.connector
import models.habit

app = Flask(__name__)

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="justaskforpass706",
  database="mydatabase"
)

habits = [
    Habit("Clean").to_dict(),
    Habit("Work").to_dict(),
    Habit("Run").to_dict(),
    Habit("Sleep").to_dict()
]

@app.route("/habits")
def get_all():
    habits = models.habit.list_habits(mydb)
    
    return render_template("habits.html", habits = habits)

@app.route("/habits/<int:habit_id>", methods = ["GET"])
def get_one(habit_id):
    habit = models.habit.get_one_habit(mydb, habit_id)
    
    return render_template("show_habit.html", habit=habit)

@app.route("/habits", methods = ["POST"])
def create_habit():
    if request.form["title"] == "":
        flash("Error: Title is required!")
        return redirect(url_for("get_all"))

    models.habit.create_habit(mydb, request.form["title"])
        
    return redirect(url_for("get_all"))

@app.route("/habits/edit/<int:habit_id>", methods = ["GET", "POST"])
def edit_habit(habit_id):
    habit = models.habit.get_one_habit(mydb, habit_id)
    
    if request.method == "GET":
        return render_template("edit_habit.html", habit=habit)

    models.habit.edit_habit(mydb, habit_id, request.form["title"])

    return redirect(url_for("get_all"))

@app.route("/habits/delete/<int:habit_id>", methods = ["GET", "POST"])
def delete_habit(habit_id):
    models.habit.delete_habit(mydb, habit_id)

    return redirect(url_for("get_all"))