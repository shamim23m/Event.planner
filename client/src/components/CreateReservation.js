import React, { useState } from 'react';
import api from './axios';

const CreateReservation = () => {
  const [userId, setUserId] = useState('');
  const [eventId, setEventId] = useState('');
  const [reservedSeats, setReservedSeats] = useState('');

  const handleSubmit = (e) => {
    e.preventDefault();
    api.post('/reservations', { user_id: userId, event_id: eventId, reserved_seats: reservedSeats })
      .then(response => alert('Reservation created successfully'))
      .catch(error => console.error('Error creating reservation:', error));
  };

  return (
    <div>
      <h2>Create Reservation</h2>
      <form onSubmit={handleSubmit}>
        <input type="number" value={userId} onChange={(e) => setUserId(e.target.value)} placeholder="User ID" required />
        <input type="number" value={eventId} onChange={(e) => setEventId(e.target.value)} placeholder="Event ID" required />
        <input type="number" value={reservedSeats} onChange={(e) => setReservedSeats(e.target.value)} placeholder="Reserved Seats" required />
        <button type="submit">Create Reservation</button>
      </form>
    </div>
  );
};

export default CreateReservation;
