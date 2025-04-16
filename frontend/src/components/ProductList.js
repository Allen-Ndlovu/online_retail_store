import React, { useEffect, useState } from 'react';
import api from '../api';
import Recommendations from './Recommendations';
import './ProductList.css';

export default function ProductList(){
  const [products, setProducts] = useState([]);
  const [q, setQ] = useState('');

  const fetchProducts = () =>
    api.get('products/', { params: { search: q, ordering: '-rating' } })
       .then(res => setProducts(res.data))
       .catch(console.error);

  useEffect(fetchProducts, [q]);

  return (
    <div className="product-list__container">
      <div className="product-list__filters">
        <input
          className="product-list__search"
          placeholder="Search products…"
          value={q}
          onChange={e => setQ(e.target.value)}
        />
      </div>
      <div className="product-list__grid">
        {products.map(p => (
          <div className="product-list__card" key={p.id}>
            <h3 className="product-list__title">{p.name}</h3>
            <p className="product-list__desc">{p.description}</p>
            <small className="product-list__meta">
              ${p.price} • Stock: {p.stock} • ⭐ {p.rating}
            </small>
            <Recommendations productId={p.id} />
          </div>
        ))}
      </div>
    </div>
  );
}
