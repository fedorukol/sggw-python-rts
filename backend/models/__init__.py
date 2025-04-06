

from backend.core.database import db
from backend.core.database import TimestampModel


class Player(TimestampModel):
    __tablename__ = "players"

    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)

    towns = db.relationship("Town", backref="player", lazy=True)

    def __repr__(self):
        return f"<Player {self.username}>"


class Town(TimestampModel):
    __tablename__ = "towns"

    name = db.Column(db.String(80), unique=False, nullable=False)
    player_id = db.Column(db.Integer, db.ForeignKey("players.id"), nullable=False)
    population = db.Column(db.Integer, nullable=False, default=0)

    def __repr__(self):
        return f"<Town {self.name}, player {self.player.username}>"