import React, { useState } from 'react';
import './styles/App.css';
import EventList from './components/EventList';
import EventForm from './components/EventForm';
import ProductCard from './components/ProductCard';

function App() {
  const [showEventForm, setShowEventForm] = useState(false);

  return (
    <div className="App">
      <header className="App-header">
        <h1>Event Planner</h1>
        <button className="toggle-form" onClick={() => setShowEventForm(!showEventForm)}>
          {showEventForm ? 'View Events' : 'Create Event'}
        </button>
      </header>

      {showEventForm ? <EventForm /> : <EventList />}
    </div>
  );
}

export default App;
