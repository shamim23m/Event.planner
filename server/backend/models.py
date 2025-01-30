# models.py

from datetime import datetime
from config import db

# User model
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    events = db.relationship('Event', backref='organizer', lazy=True)
    reservations = db.relationship('Reservation', backref='user', lazy=True)

    def __repr__(self):
        return f"<User {self.username}>"

# Event model
class Event(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)
    description = db.Column(db.String(500))
    date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    reservations = db.relationship('Reservation', backref='event', lazy=True)

    def __repr__(self):
        return f"<Event {self.name}>"

# Reservation model (many-to-many relationship between User and Event)
class Reservation(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    event_id = db.Column(db.Integer, db.ForeignKey('event.id'), nullable=False)
    reserved_seats = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f"<Reservation {self.user_id} - {self.event_id}>"
