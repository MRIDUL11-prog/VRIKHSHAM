
import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    SECRET_KEY = os.getenv("SECRET_KEY", "dev-secret-key")

    SQLALCHEMY_DATABASE_URI = os.getenv(
        "DATABASE_URL",
        "postgresql://postgres:YOUR_PASSWORD@localhost:5432/vriksham_db"
    )

    SQLALCHEMY_TRACK_MODIFICATIONS = False
