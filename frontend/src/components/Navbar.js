import React, { useContext } from 'react';
import { Link } from 'react-router-dom';
import { AuthContext } from '../AuthContext';
import './Navbar.css';

export default function Navbar(){
  const { user, logout } = useContext(AuthContext);
  return (
    <nav className="navbar">
      <div className="navbar__logo">🏬 RetailStore</div>
      <div className="navbar__links">
        <Link to="/">Products</Link>
        {user ? (
          <>
            <Link to="/notifications">Notifications</Link>
            <button className="navbar__btn" onClick={logout}>Logout</button>
          </>
        ) : (
          <>
            <Link to="/login">Login</Link>
            <Link to="/register">Register</Link>
          </>
        )}
      </div>
    </nav>
  );
}
