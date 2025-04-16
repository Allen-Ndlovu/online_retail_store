import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import api from '../api';
import './RegisterForm.css';

export default function RegisterForm(){
  const [form, setForm] = useState({ username:'', email:'', password:'' });
  const navigate = useNavigate();

  const handleSubmit = async e => {
    e.preventDefault();
    try {
      await api.post('auth/register/', form);
      alert('Registered successfully!');
      navigate('/login');
    } catch {
      alert('Registration error');
    }
  };

  return (
    <form className="form-card" onSubmit={handleSubmit}>
      <h2>Register</h2>
      <input
        className="form-card__input"
        placeholder="Username"
        onChange={e => setForm({...form, username: e.target.value})}
      />
      <input
        className="form-card__input"
        placeholder="Email"
        onChange={e => setForm({...form, email: e.target.value})}
      />
      <input
        className="form-card__input"
        type="password"
        placeholder="Password"
        onChange={e => setForm({...form, password: e.target.value})}
      />
      <button className="form-card__btn" type="submit">Sign Up</button>
    </form>
  );
}
