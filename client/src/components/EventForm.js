import React, { useState } from 'react';
import axios from 'axios';


function EventForm() {
  const [eventDetails, setEventDetails] = useState({
    name: '',
    description: '',
    date: '',
    user_id: 1, // Assuming user_id is 1 for now
  });

  const handleChange = (e) => {
    setEventDetails({
      ...eventDetails,
      [e.target.name]: e.target.value,
    });
  };

  const handleSubmit = (e) => {
    e.preventDefault();

    axios.post('http://localhost:5000/api/events', eventDetails)
      .then(response => {
        console.log('Event created:', response.data);
      })
      .catch(error => {
        console.log('Error creating event:', error);
      });
  };

  return (
    <div className="event-form">
      <h2>Create Event</h2>
      <form onSubmit={handleSubmit}>
        <input
          type="text"
          name="name"
          value={eventDetails.name}
          onChange={handleChange}
          placeholder="Event Name"
          required
        />
        <textarea
          name="description"
          value={eventDetails.description}
          onChange={handleChange}
          placeholder="Event Description"
          required
        />
        <input
          type="datetime-local"
          name="date"
          value={eventDetails.date}
          onChange={handleChange}
          required
        />
        <button type="submit">Create Event</button>
      </form>
    </div>
  );
}

export default EventForm;
