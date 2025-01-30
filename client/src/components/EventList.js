import React from 'react';

function EventList({ events, editEvent }) {
  const handleEdit = (event) => {
    editEvent(event.id, event); // You can also open the form to edit here
  };

  return (
    <ul>
      {events.map((event) => (
        <li key={event.id}>
          <div>
            <h3>{event.name}</h3>
            <p>{event.description}</p>
            <p>{event.date}</p>
          </div>
          <button onClick={() => handleEdit(event)}>Edit</button>
        </li>
      ))}
    </ul>
  );
}

export default EventList;
