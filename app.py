from flask import Flask, render_template, request, redirect, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from dotenv import load_dotenv
import certifi
import os

load_dotenv()

app = Flask(__name__)

app.secret_key = os.getenv("SECRET_KEY", "hero-vired-secret")

mongo = None
mongo_uri = os.getenv("MONGO_URI")

if mongo_uri:
    app.config["MONGO_URI"] = mongo_uri

    if os.getenv("GITHUB_ACTIONS") == "true":
        mongo = PyMongo(app)
    else:
        mongo = PyMongo(app, tlsCAFile=certifi.where())


# ---------------------------------------------------
# Home Page
# ---------------------------------------------------
@app.route("/")
def index():

    if mongo:
        students = mongo.db.students.find()
    else:
        students = []

    return render_template("index.html", students=students)


# ---------------------------------------------------
# Add Student
# ---------------------------------------------------
@app.route("/add", methods=["GET", "POST"])
def add_student():

    if request.method == "POST":

        if mongo:
            mongo.db.students.insert_one(
                {
                    "name": request.form["name"],
                    "email": request.form["email"],
                    "course": request.form["course"],
                }
            )

        return redirect(url_for("index"))

    return render_template("add_student.html")


# ---------------------------------------------------
# Update Student
# ---------------------------------------------------
@app.route("/update/<student_id>", methods=["GET", "POST"])
def update_student(student_id):

    student = None

    if mongo:
        student = mongo.db.students.find_one(
            {"_id": ObjectId(student_id)}
        )

    if request.method == "POST":

        if mongo:
            mongo.db.students.update_one(
                {"_id": ObjectId(student_id)},
                {
                    "$set": {
                        "name": request.form["name"],
                        "email": request.form["email"],
                        "course": request.form["course"],
                    }
                },
            )

        return redirect(url_for("index"))

    return render_template("update_student.html", student=student)


# ---------------------------------------------------
# Delete Student
# ---------------------------------------------------
@app.route("/delete/<student_id>")
def delete_student(student_id):

    if mongo:
        mongo.db.students.delete_one(
            {"_id": ObjectId(student_id)}
        )

    return redirect(url_for("index"))


# ---------------------------------------------------
# Main
# ---------------------------------------------------
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)