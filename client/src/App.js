import React, { useState } from 'react';
import EventForm from './components/EventForm';
import EventList from './components/EventList';
import './App.css';

function App() {
  const [events, setEvents] = useState([]);

  const addEvent = (newEvent) => {
    setEvents([...events, newEvent]);
  };

  const editEvent = (id, updatedEvent) => {
    setEvents(events.map(event => event.id === id ? updatedEvent : event));
  };

  return (
    <div className="App">
      <header>
        <h1>Event Planner</h1>
      </header>

      <main>
        <section id="event-form-section">
          <EventForm addEvent={addEvent} editEvent={editEvent} />
        </section>

        <section id="event-list-section">
          <h2>Upcoming Events</h2>
          <EventList events={events} editEvent={editEvent} />
        </section>
      </main>
    </div>
  );
}

export default App;
