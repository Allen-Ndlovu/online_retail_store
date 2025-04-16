import React, { useEffect, useState } from 'react';
import api from '../api';
import './Recommendations.css';

export default function Recommendations({ productId }){
  const [recs, setRecs] = useState([]);

  useEffect(() => {
    api.get(`products/${productId}/recommend/`)
       .then(res => setRecs(res.data))
       .catch(console.error);
  }, [productId]);

  if (!recs.length) return null;

  return (
    <div className="recs">
      🔄 {recs.slice(0,3).map(r => r.name).join(', ')}
    </div>
  );
}
