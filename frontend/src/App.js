import React from 'react';
import { BrowserRouter, Routes, Route } from 'react-router-dom';
import { AuthProvider } from './AuthContext';
import Navbar from './components/Navbar';
import ProductList from './components/ProductList';
import LoginForm from './components/LoginForm';
import RegisterForm from './components/RegisterForm';
import Notifications from './components/Notifications';

export default function App(){
  return (
    <AuthProvider>
      <BrowserRouter>
        <Navbar/>
        <Routes>
          <Route path="/" element={<ProductList/>}/>
          <Route path="/login" element={<LoginForm/>}/>
          <Route path="/register" element={<RegisterForm/>}/>
          <Route path="/notifications" element={<Notifications/>}/>
        </Routes>
      </BrowserRouter>
    </AuthProvider>
  );
}

