import React from 'react';
import './ProductCard.css';

function ProductCard({ product }) {
  return (
    <div className="product-card">
      <h3>{product.name}</h3>
      <p>{product.description}</p>
      <p>
        <strong>Price:</strong> ${product.price}
      </p>
      <p>
        <strong>Stock:</strong> {product.stock}
      </p>
      <button className="btn">Buy Now</button>
    </div>
  );
}

export default ProductCard;
