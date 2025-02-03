import React from 'react';


function ProductCard({ event }) {
  return (
    <div className="product-card">
      <h3>{event.name}</h3>
      <p>{event.description}</p>
      <p><strong>Organized by:</strong> {event.organizer}</p>
      <p><strong>Date:</strong> {new Date(event.date).toLocaleString()}</p>
    </div>
  );
}

export default ProductCard;
