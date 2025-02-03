import React, { useState, useEffect } from 'react';
import axios from 'axios';
import ProductCard from './ProductCard';
import './EventList.css';


function EventList() {
  const [events, setEvents] = useState([]);

  useEffect(() => {
    axios.get('http://localhost:5000/api/events')
      .then(response => setEvents(response.data))
      .catch(error => console.log('Error fetching events:', error));
  }, []);

  return (
    <div className="event-list">
      <h2>Upcoming Events</h2>
      <div className="event-cards">
        {events.map(event => (
          <ProductCard key={event.id} event={event} />
        ))}
      </div>
    </div>
  );
}

export default EventList;
