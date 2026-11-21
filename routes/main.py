
from flask import (
    Blueprint,
    render_template,
    session,
    redirect,
    url_for,
    request
)

from models import Garden, Plant, Reminder


main = Blueprint("main", __name__)


# =====================================
# HOME PAGE
# =====================================

@main.route("/")
def home():
    return render_template("index.html")


# =====================================
# ABOUT PAGE
# =====================================

@main.route("/about")
def about():
    return render_template("about.html")


# =====================================
# PLANT DOCTOR PAGE
# =====================================

@main.route("/plant-doctor")
def plant_doctor():
    return render_template("plant_doctor.html")


# =====================================
# PLANT CARE PAGE
# =====================================

@main.route("/plant-care")
def plant_care():
    return render_template("plant_care.html")


# =====================================
# MY GARDEN PAGE
# =====================================

@main.route("/my-garden")
def my_garden():

    if not session.get("user_id"):
        return redirect(
            url_for("auth.login", next=request.path)
        )

    user_id = session["user_id"]

    gardens = Garden.query.filter_by(
        user_id=user_id
    ).all()

    plants = Plant.query.filter_by(
        user_id=user_id
    ).all()

    return render_template(
        "my_garden.html",
        gardens=gardens,
        plants=plants
    )


# =====================================
# REMINDERS PAGE
# =====================================

@main.route("/reminders")
def reminders():

    if not session.get("user_id"):
        return redirect(
            url_for("auth.login", next=request.path)
        )

    user_id = session["user_id"]

    user_reminders = Reminder.query.filter_by(
        user_id=user_id
    ).all()

    return render_template(
        "reminders.html",
        reminders=user_reminders
    )


# =====================================
# HEALTH HISTORY PAGE
# =====================================

@main.route("/health-history")
def health_history():

    if not session.get("user_id"):
        return redirect(
            url_for("auth.login", next=request.path)
        )

    user_id = session["user_id"]

    user_plants = Plant.query.filter_by(
        user_id=user_id
    ).all()

    return render_template(
        "health_history.html",
        plants=user_plants
    )
