import React from 'react';
import './Navbar.css';

function Navbar() {
  return (
    <nav className="navbar">
      <div className="navbar__logo">RetailStore</div>
      <ul className="navbar__menu">
        <li>Home</li>
        <li>Products</li>
        <li>Orders</li>
        <li>Login</li>
      </ul>
    </nav>
  );
}

export default Navbar;
