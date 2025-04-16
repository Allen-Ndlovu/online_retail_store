import React, { useState, useContext } from 'react';
import { useNavigate } from 'react-router-dom';
import { AuthContext } from '../AuthContext';
import './LoginForm.css';

export default function LoginForm(){
  const [creds, setCreds] = useState({ username: '', password: '' });
  const { login } = useContext(AuthContext);
  const navigate = useNavigate();

  const handleSubmit = async e => {
    e.preventDefault();
    try {
      await login(creds.username, creds.password);
      navigate('/');
    } catch {
      alert('Login failed');
    }
  };

  return (
    <form className="form-card" onSubmit={handleSubmit}>
      <h2>Login</h2>
      <input
        className="form-card__input"
        placeholder="Username"
        onChange={e => setCreds({...creds, username: e.target.value})}
      />
      <input
        className="form-card__input"
        type="password"
        placeholder="Password"
        onChange={e => setCreds({...creds, password: e.target.value})}
      />
      <button className="form-card__btn" type="submit">Sign In</button>
    </form>
  );
}
