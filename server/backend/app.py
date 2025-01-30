from flask import Flask, jsonify, request
from flask_restful import Api, Resource
from config import app, api, db
from models import User, Event, Reservation

@app.route('/')
def home():
    return jsonify(message="Event Planner API is running")

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

@app.route('/api/events', methods=['POST'])
def create_event():
    data = request.get_json()
    new_event = Event(
        name=data['name'],
        description=data['description'],
        date=datetime.strptime(data['date'], '%Y-%m-%dT%H:%M:%S'),
        user_id=data['user_id']
    )
    db.session.add(new_event)
    db.session.commit()
    return jsonify({
        'id': new_event.id,
        'name': new_event.name,
        'description': new_event.description,
        'date': new_event.date,
        'organizer': new_event.organizer.username
    }), 201

@app.route('/api/reservations', methods=['POST'])
def create_reservation():
    data = request.get_json()
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

@app.route('/api/events/<int:event_id>/reservations', methods=['GET'])
def get_reservations_for_event(event_id):
    event = Event.query.get_or_404(event_id)
    reservations = Reservation.query.filter_by(event_id=event.id).all()
    return jsonify([{
        'user_id': res.user_id,
        'reserved_seats': res.reserved_seats
    } for res in reservations])

if __name__ == '__main__':
    app.run(debug=True)
