import React from 'react';
import ProductCard from './ProductCard';
import './ProductList.css';

function ProductList({ products }) {
  if (!products || products.length === 0) {
    return <p>No products available.</p>;
  }
  return (
    <div className="product-list">
      {products.map((product) => (
        <ProductCard key={product.id || product._id} product={product} />
      ))}
    </div>
  );
}

export default ProductList;
