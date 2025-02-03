# seed.py
from config import db
from models import User, Event, Reservation
from datetime import datetime

# Create sample user
user = User(username="john_doe")
db.session.add(user)

# Create a sample event
event = Event(name="Coding Bootcamp", description="Learn Flask and React", date=datetime(2025, 6, 1), user_id=1)
db.session.add(event)

# Commit to database
db.session.commit()

print("Database seeded!")
