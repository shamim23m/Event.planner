import React, { useState } from 'react';
import api from './axios';

const CreateUser = () => {
  const [username, setUsername] = useState('');

  const handleSubmit = (e) => {
    e.preventDefault();
    api.post('/users', { username })
      .then(response => alert('User created successfully'))
      .catch(error => console.error('Error creating user:', error));
  };

  return (
    <div>
      <h2>Create User</h2>
      <form onSubmit={handleSubmit}>
        <input
          type="text"
          value={username}
          onChange={(e) => setUsername(e.target.value)}
          placeholder="Enter username"
          required
        />
        <button type="submit">Create User</button>
      </form>
    </div>
  );
};

export default CreateUser;