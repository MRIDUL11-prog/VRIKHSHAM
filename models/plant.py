
from extensions import db
from datetime import datetime, timezone


class Plant(db.Model):

    __tablename__ = "plants"

    id = db.Column(
        db.Integer,
        primary_key=True
    )

    # Owner of this plant
    user_id = db.Column(
        db.Integer,
        db.ForeignKey("users.id"),
        nullable=False
    )

    name = db.Column(
        db.String(100),
        nullable=False
    )

    species = db.Column(
        db.String(150),
        nullable=True
    )

    planted_date = db.Column(
        db.Date,
        nullable=True
    )

    health_status = db.Column(
        db.String(50),
        default="Healthy"
    )

    notes = db.Column(
        db.Text,
        nullable=True
    )

    created_at = db.Column(
        db.DateTime(timezone=True),
        default=lambda: datetime.now(timezone.utc)
    )

    def __repr__(self):
        return f"<Plant {self.name}>"
