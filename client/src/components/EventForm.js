import React, { useState, useEffect } from 'react';

function EventForm({ addEvent, editEvent }) {
  const [eventName, setEventName] = useState('');
  const [eventDescription, setEventDescription] = useState('');
  const [eventDate, setEventDate] = useState('');
  const [eventId, setEventId] = useState(null);

  useEffect(() => {
    if (eventId) {
      // If editing, fill in existing event details
      const event = JSON.parse(localStorage.getItem(eventId));
      setEventName(event.name);
      setEventDescription(event.description);
      setEventDate(event.date);
    }
  }, [eventId]);

  const handleSubmit = (e) => {
    e.preventDefault();

    if (!eventName || !eventDescription || !eventDate) {
      alert('Please fill out all fields.');
      return;
    }

    const newEvent = {
      id: eventId || Date.now().toString(),
      name: eventName,
      description: eventDescription,
      date: eventDate,
    };

    if (eventId) {
      editEvent(eventId, newEvent);
    } else {
      addEvent(newEvent);
    }

    clearForm();
  };

  const clearForm = () => {
    setEventName('');
    setEventDescription('');
    setEventDate('');
    setEventId(null);
  };

  return (
    <form onSubmit={handleSubmit}>
      <input type="hidden" id="event-id" value={eventId || ''} />
      <label htmlFor="event-name">Event Name:</label>
      <input
        type="text"
        id="event-name"
        value={eventName}
        onChange={(e) => setEventName(e.target.value)}
        required
      />

      <label htmlFor="event-description">Description:</label>
      <textarea
        id="event-description"
        value={eventDescription}
        onChange={(e) => setEventDescription(e.target.value)}
        required
      ></textarea>

      <label htmlFor="event-date">Event Date:</label>
      <input
        type="text"
        id="event-date"
        value={eventDate}
        onChange={(e) => setEventDate(e.target.value)}
        required
        placeholder="YYYY-MM-DD"
      />

      <button type="submit">Save Event</button>
    </form>
  );
}

export default EventForm;
