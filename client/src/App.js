// import React, { useState } from 'react';
// import './styles/App.css';
// import EventList from './components/EventList';
// import EventForm from './components/EventForm';
// import ProductCard from './components/ProductCard';

// function App() {
//   const [showEventForm, setShowEventForm] = useState(false);

//   return (
//     <div className="App">
//       <header className="App-header">
//         <h1>Event Planner</h1>
//         <button className="toggle-form" onClick={() => setShowEventForm(!showEventForm)}>
//           {showEventForm ? 'View Events' : 'Create Event'}
//         </button>
//       </header>

//       {showEventForm ? <EventForm /> : <EventList />}
//     </div>
//   );
// }

// export default App;
import React from 'react';
import UserList from './components/UserList';
import EventList from './components/EventList';
import ReservationList from './components/ReservationList';
import CreateUser from './components/CreateUser';
import CreateEvent from './components/CreateEvent';
import CreateReservation from './components/CreateReservation';

function App() {
  return (
    <div className="App">
      <h1>Event Planner</h1>
      <CreateUser />
      <CreateEvent />
      <CreateReservation />
      <UserList />
      <EventList />
      <ReservationList />
    </div>
  );
}

export default App;
