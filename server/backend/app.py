from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Api
from flask_migrate import Migrate
from flask_cors import CORS

# Initialize app, database, and CORS
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///instance/app.db'  # Use SQLite for simplicity
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize db, CORS, and Migrate
db = SQLAlchemy(app)
CORS(app)
migrate = Migrate(app, db)
api = Api(app)

# Import models after db is initialized to avoid circular import
from models import User, Event, Reservation

# Routes
@app.route('/')
def home():
    return jsonify(message="Event Planner API is running")

# --- CRUD for Events ---
@app.route('/api/events', methods=['GET'])
def get_events():
    events = Event.query.all()
    return jsonify([{
        'id': event.id,
        'name': event.name,
        'description': event.description,
        'date': event.date,
        'organizer': event.organizer.username
    } for event in events])

# Get a specific event by id
@app.route('/api/events/<int:event_id>', methods=['GET'])
def get_event(event_id):
    event = Event.query.get_or_404(event_id)
    return jsonify({
        'id': event.id,
        'name': event.name,
        'description': event.description,
        'date': event.date,
        'organizer': event.organizer.username
    })

# --- CRUD for Reservations ---
@app.route('/api/reservations', methods=['POST'])
def create_reservation():
    data = request.get_json()

    if not data.get('user_id') or not data.get('event_id') or not data.get('reserved_seats'):
        return jsonify({'message': 'Missing required fields'}), 400

    new_reservation = Reservation(
        user_id=data['user_id'],
        event_id=data['event_id'],
        reserved_seats=data['reserved_seats']
    )
    db.session.add(new_reservation)
    db.session.commit()

    return jsonify({
        'id': new_reservation.id,
        'user_id': new_reservation.user_id,
        'event_id': new_reservation.event_id,
        'reserved_seats': new_reservation.reserved_seats
    }), 201

if __name__ == '__main__':
    app.run(debug=True)
