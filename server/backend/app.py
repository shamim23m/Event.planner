# from flask import Flask, jsonify, request
# from flask_sqlalchemy import SQLAlchemy
# from flask_restful import Api, Resource, reqparse
# from flask_migrate import Migrate
# from flask_cors import CORS
# from models import User, Event, Reservation

# # Initialize app, database, and CORS
# app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'

# #app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///instance/app.db'  # Use SQLite for simplicity
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# db = SQLAlchemy(app)

# # Initialize db, CORS, and Migrate
# CORS(app)
# migrate = Migrate(app, db)
# api = Api(app)

# # --- Resource for Events ---
# class EventListResource(Resource):
#     def get(self):
#         events = Event.query.all()
#         return [{
#             'id': event.id,
#             'name': event.name,
#             'description': event.description,
#             'date': event.date,
#             'organizer': event.organizer.username
#         } for event in events], 200


# class EventResource(Resource):
#     def get(self, event_id):
#         event = Event.query.get_or_404(event_id)
#         return {
#             'id': event.id,
#             'name': event.name,
#             'description': event.description,
#             'date': event.date,
#             'organizer': event.organizer.username
#         }, 200

# # --- Resource for Reservations ---
# class ReservationResource(Resource):
#     def post(self):
#         data = request.get_json()

#         if not data.get('user_id') or not data.get('event_id') or not data.get('reserved_seats'):
#             return {'message': 'Missing required fields'}, 400

#         new_reservation = Reservation(
#             user_id=data['user_id'],
#             event_id=data['event_id'],
#             reserved_seats=data['reserved_seats']
#         )
#         db.session.add(new_reservation)
#         db.session.commit()

#         return {
#             'id': new_reservation.id,
#             'user_id': new_reservation.user_id,
#             'event_id': new_reservation.event_id,
#             'reserved_seats': new_reservation.reserved_seats
#         }, 201


# # Routes
# @app.route('/')
# def home():
#     return jsonify(message="Event Planner API is running")

# # Register Resources
# api.add_resource(EventListResource, '/api/events')
# api.add_resource(EventResource, '/api/events/<int:event_id>')
# api.add_resource(ReservationResource, '/api/reservations')

# if __name__ == '__main__':
#     app.run(debug=True)
from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Api, Resource
from flask_migrate import Migrate
from flask_cors import CORS
from models import db, User, Event, Reservation

# Initialize app, database, and CORS
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

# Initialize CORS, Migrate, and Flask-Restful API
CORS(app)
migrate = Migrate(app, db)
api = Api(app)

# Base API Route
@app.route('/')
def home():
    return jsonify(message="Event Planner API is running")

# --- API Resource for Users ---
class UserListResource(Resource):
    def get(self):
        users = User.query.all()
        return jsonify([user.to_dict() for user in users])

    def post(self):
        data = request.get_json()
        new_user = User(username=data['username'])
        db.session.add(new_user)
        db.session.commit()
        return jsonify(new_user.to_dict()), 201

class UserResource(Resource):
    def get(self, user_id):
        user = User.query.get_or_404(user_id)
        return jsonify(user.to_dict())

# --- API Resource for Events ---
class EventListResource(Resource):
    def get(self):
        events = Event.query.all()
        return jsonify([event.to_dict() for event in events])

    def post(self):
        data = request.get_json()
        new_event = Event(
            name=data['name'],
            description=data['description'],
            date=data['date'],
            user_id=data['user_id']
        )
        db.session.add(new_event)
        db.session.commit()
        return jsonify(new_event.to_dict()), 201

class EventResource(Resource):
    def get(self, event_id):
        event = Event.query.get_or_404(event_id)
        return jsonify(event.to_dict())

# --- API Resource for Reservations ---
class ReservationListResource(Resource):
    def get(self):
        reservations = Reservation.query.all()
        return jsonify([reservation.to_dict() for reservation in reservations])

    def post(self):
        data = request.get_json()
        new_reservation = Reservation(
            user_id=data['user_id'],
            event_id=data['event_id'],
            reserved_seats=data['reserved_seats']
        )
        db.session.add(new_reservation)
        db.session.commit()
        return jsonify(new_reservation.to_dict()), 201

class ReservationResource(Resource):
    def get(self, reservation_id):
        reservation = Reservation.query.get_or_404(reservation_id)
        return jsonify(reservation.to_dict())

# Add resources to the API
api.add_resource(UserListResource, '/api/users')
api.add_resource(UserResource, '/api/users/<int:user_id>')
api.add_resource(EventListResource, '/api/events')
api.add_resource(EventResource, '/api/events/<int:event_id>')
api.add_resource(ReservationListResource, '/api/reservations')
api.add_resource(ReservationResource, '/api/reservations/<int:reservation_id>')

if __name__ == '__main__':
    app.run(debug=True)
