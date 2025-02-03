from app import db  # Import db from app.py to use the initialized db object

# User model
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), nullable=False, unique=True)
    events = db.relationship('Event', backref='organizer', lazy=True)
    reservations = db.relationship('Reservation', backref='user', lazy=True)

    def __repr__(self):
        return f"<User {self.username}>"

# Event model
class Event(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(500), nullable=False)
    date = db.Column(db.DateTime, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    organizer = db.relationship('User', backref=db.backref('events', lazy=True))

    def __repr__(self):
        return f"<Event {self.name}>"

# Reservation model
class Reservation(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    event_id = db.Column(db.Integer, db.ForeignKey('event.id'), nullable=False)
    reserved_seats = db.Column(db.Integer, nullable=False)
    user = db.relationship('User', backref=db.backref('reservations', lazy=True))
    event = db.relationship('Event', backref=db.backref('reservations', lazy=True))

    def __repr__(self):
        return f"<Reservation {self.user_id} - {self.event_id}>"
