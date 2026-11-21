
from flask import (
    Blueprint,
    render_template,
    request,
    redirect,
    url_for,
    session
)

from extensions import db
from models import User

from werkzeug.security import (
    generate_password_hash,
    check_password_hash
)

auth = Blueprint("auth", __name__)


# =====================================
# USER REGISTRATION
# =====================================

@auth.route("/register", methods=["GET", "POST"])
def register():

    if request.method == "POST":

        name = request.form.get("name", "").strip()
        email = request.form.get("email", "").strip().lower()
        password = request.form.get("password", "")
        confirm_password = request.form.get("confirm_password", "")

        # Check empty fields
        if not name or not email or not password or not confirm_password:
            return render_template(
                "register.html",
                error="Please fill in all fields."
            )

        # Check password length
        if len(password) < 8:
            return render_template(
                "register.html",
                error="Password must contain at least 8 characters."
            )

        # Check password confirmation
        if password != confirm_password:
            return render_template(
                "register.html",
                error="Passwords do not match."
            )

        # Check existing email
        existing_user = User.query.filter_by(email=email).first()

        if existing_user:
            return render_template(
                "register.html",
                error="This email is already registered."
            )

        # Hash password securely
        hashed_password = generate_password_hash(password)

        new_user = User(
            name=name,
            email=email,
            password=hashed_password
        )

        try:
            db.session.add(new_user)
            db.session.commit()

            return render_template(
                "register.html",
                success="Account created successfully! You can now log in."
            )

        except Exception:
            db.session.rollback()

            return render_template(
                "register.html",
                error="Something went wrong. Please try again."
            )

    return render_template("register.html")


# =====================================
# USER LOGIN
# =====================================

@auth.route("/login", methods=["GET", "POST"])
def login():

    if request.method == "POST":

        email = request.form.get("email", "").strip().lower()
        password = request.form.get("password", "")

        user = User.query.filter_by(email=email).first()

        if user and check_password_hash(user.password, password):

            # Get originally requested page
            next_page = request.form.get("next", "")

            # Clear previous session
            session.clear()

            # Store logged-in user information
            session["user_id"] = user.id
            session["user_name"] = user.name

            # Redirect to originally requested page
            if (
                next_page
                and next_page.startswith("/")
                and not next_page.startswith("//")
                and "\\" not in next_page
            ):
                return redirect(next_page)

            # Default redirect to Home Page
            return redirect(url_for("main.home"))

        return render_template(
            "login.html",
            error="Invalid email address or password."
        )

    return render_template("login.html")


# =====================================
# USER LOGOUT
# =====================================

@auth.route("/logout", methods=["POST"])
def logout():

    # Clear the user's session
    session.clear()

    # Redirect to Home Page
    return redirect(url_for("main.home"))
