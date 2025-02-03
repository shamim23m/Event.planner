import React, { useEffect, useState } from 'react';
import api from './axios';

const ReservationList = () => {
  const [reservations, setReservations] = useState([]);

  useEffect(() => {
    api.get('/reservations')
      .then(response => setReservations(response.data))
      .catch(error => console.error('Error fetching reservations:', error));
  }, []);

  return (
    <div>
      <h2>Reservation List</h2>
      <ul>
        {reservations.map(reservation => (
          <li key={reservation.id}>
            User ID: {reservation.user_id} | Event ID: {reservation.event_id} | Reserved Seats: {reservation.reserved_seats}
          </li>
        ))}
      </ul>
    </div>
  );
};

export default ReservationList;