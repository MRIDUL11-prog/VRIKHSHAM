
from flask import Blueprint, render_template

main = Blueprint("main", __name__)


@main.route("/")
def home():
    return render_template("index.html")


@main.route("/about")
def about():
    return render_template("about.html")


@main.route("/plant-doctor")
def plant_doctor():
    return render_template("plant_doctor.html")


@main.route("/plant-care")
def plant_care():
    return render_template("plant_care.html")


@main.route("/my-garden")
def my_garden():
    return render_template("my_garden.html")


@main.route("/reminders")
def reminders():
    return render_template("reminders.html")


@main.route("/health-history")
def health_history():
    return render_template("health_history.html")
