import React, { useEffect, useState } from 'react';
import api from './axios';

const EventList = () => {
  const [events, setEvents] = useState([]);

  useEffect(() => {
    api.get('/events')
      .then(response => setEvents(response.data))
      .catch(error => console.error('Error fetching events:', error));
  }, []);

  return (
    <div>
      <h2>Event List</h2>
      <ul>
        {events.map(event => (
          <li key={event.id}>
            {event.name} - {event.date}
            <p>{event.description}</p>
            <p>Organizer: {event.organizer}</p>
          </li>
        ))}
      </ul>
    </div>
  );
};

export default EventList;
