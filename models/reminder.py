
from extensions import db
from datetime import datetime, timezone


class Reminder(db.Model):

    __tablename__ = "reminders"

    id = db.Column(
        db.Integer,
        primary_key=True
    )

    user_id = db.Column(
        db.Integer,
        db.ForeignKey("users.id"),
        nullable=False
    )

    plant_id = db.Column(
        db.Integer,
        db.ForeignKey("plants.id"),
        nullable=True
    )

    title = db.Column(
        db.String(150),
        nullable=False
    )

    reminder_type = db.Column(
        db.String(50),
        nullable=False
    )

    reminder_date = db.Column(
        db.DateTime(timezone=True),
        nullable=False
    )

    notes = db.Column(
        db.Text,
        nullable=True
    )

    is_completed = db.Column(
        db.Boolean,
        default=False
    )

    created_at = db.Column(
        db.DateTime(timezone=True),
        default=lambda: datetime.now(timezone.utc)
    )

    def __repr__(self):
        return f"<Reminder {self.title}>"
