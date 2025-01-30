import React from 'react';
import { Card, Button } from 'react-bootstrap';
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome';
import { faCalendarPlus } from '@fortawesome/free-solid-svg-icons';

function EventCard({ event, addToSchedule }) {
  return (
    <Card className="shadow-sm">
      <Card.Img
        variant="top"
        src={event.image || 'https://i.pinimg.com/736x/83/a5/fc/83a5fc6d8364822d0bc44707db485126.jpg'}
        alt={event.name}
        className="card-img-top"
      />
      <Card.Body>
        <Card.Title>{event.name}</Card.Title>
        <Card.Text>Date: {event.date}</Card.Text>
        <Card.Text>Location: {event.location}</Card.Text>
        <Card.Text>Organizer: {event.organizer}</Card.Text>
        <Button variant="success" onClick={() => addToSchedule(event)}>
          <FontAwesomeIcon icon={faCalendarPlus} /> Add to Schedule
        </Button>
      </Card.Body>
    </Card>
  );
}

export default EventCard;