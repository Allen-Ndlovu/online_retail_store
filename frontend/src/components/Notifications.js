import React, { useEffect, useState, useContext } from 'react';
import { AuthContext } from '../AuthContext';
import './Notifications.css';

export default function Notifications(){
  const { user } = useContext(AuthContext);
  const [notes, setNotes] = useState([]);

  useEffect(() => {
    if (!user) return;
    const ws = new WebSocket(`ws://localhost:8000/ws/notifications/${user.user_id}/`);
    ws.onmessage = e => setNotes(prev => [JSON.parse(e.data), ...prev]);
    return () => ws.close();
  }, [user]);

  return (
    <div className="notes">
      <h2>Notifications</h2>
      {notes.length === 0 && <p>No notifications</p>}
      {notes.map((n,i) => (
        <div className="note-item" key={i}>{n.text}</div>
      ))}
    </div>
  );
}
