import React, { createContext, useState } from 'react';
import jwtDecode from 'jwt-decode';
import api from './api';

export const AuthContext = createContext();

export function AuthProvider({ children }) {
  const [user, setUser] = useState(() => {
    const t = localStorage.getItem('accessToken');
    return t ? jwtDecode(t) : null;
  });

  const login = async (u,p) => {
    const { data } = await api.post('auth/token/', { username:u, password:p });
    localStorage.setItem('accessToken', data.access);
    localStorage.setItem('refreshToken', data.refresh);
    setUser(jwtDecode(data.access));
  };
  const logout = () => {
    localStorage.clear();
    setUser(null);
  };

  return (
    <AuthContext.Provider value={{ user, login, logout }}>
      {children}
    </AuthContext.Provider>
  );
}
