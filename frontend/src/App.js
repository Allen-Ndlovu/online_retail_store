import React, { useEffect, useState } from 'react';
import axios from 'axios';
import Navbar from './components/Navbar';
import ProductList from './components/ProductList';
import LoginForm from './components/LoginForm';
import './App.css';

function App() {
  const [products, setProducts] = useState([]);

  useEffect(() => {
    // Fetch core from the backend API
    axios
      .get('http://localhost:8000/api/products/')
      .then((response) => setProducts(response.data))
      .catch((error) => console.error('Error fetching core:', error));
  }, []);

  return (
    <div className="App">
      <Navbar />
      <div className="container">
        <h1>Welcome to the Innovative Online Retail Store</h1>
        <ProductList products={products} />
        <LoginForm />
      </div>
    </div>
  );
}

export default App;
