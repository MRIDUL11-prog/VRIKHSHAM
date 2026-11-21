
from flask import Flask
from config import Config
from extensions import db

from routes.main import main
from routes.auth import auth

from models import User, Plant, Garden, Reminder


# Create Flask application
app = Flask(__name__)


# Load configuration
app.config.from_object(Config)


# Initialize database
db.init_app(app)


# Register blueprints
app.register_blueprint(main)
app.register_blueprint(auth)


# Database connection test
@app.route("/db-test")
def db_test():

    try:
        with db.engine.connect() as connection:
            return "PostgreSQL connected successfully!"

    except Exception as e:
        return f"Database connection failed: {e}", 500


# Temporary table creation route
@app.route("/create-tables")
def create_tables():

    try:
        with app.app_context():
            db.create_all()

        return "VRIKHSHAM tables created successfully!"

    except Exception as e:
        return f"Error: {e}", 500


# Run application
if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=5000,
        debug=True
    )