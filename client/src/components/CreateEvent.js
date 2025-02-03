import React, { useState } from 'react';
import api from './axios';

const CreateEvent = () => {
  const [name, setName] = useState('');
  const [description, setDescription] = useState('');
  const [date, setDate] = useState('');
  const [userId, setUserId] = useState('');

  const handleSubmit = (e) => {
    e.preventDefault();
    api.post('/events', { name, description, date, user_id: userId })
      .then(response => alert('Event created successfully'))
      .catch(error => console.error('Error creating event:', error));
  };

  return (
    <div>
      <h2>Create Event</h2>
      <form onSubmit={handleSubmit}>
        <input type="text" value={name} onChange={(e) => setName(e.target.value)} placeholder="Event Name" required />
        <textarea value={description} onChange={(e) => setDescription(e.target.value)} placeholder="Description" required />
        <input type="datetime-local" value={date} onChange={(e) => setDate(e.target.value)} required />
        <input type="number" value={userId} onChange={(e) => setUserId(e.target.value)} placeholder="Organizer (User ID)" required />
        <button type="submit">Create Event</button>
      </form>
    </div>
  );
};

export default CreateEvent;