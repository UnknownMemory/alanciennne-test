import React, { useEffect, useState } from "react";
import { Container, ListGroup } from "react-bootstrap";
import useFetch from "../../hooks/useFetch";
import Product from "../product/product";

const Catalog = () => {
  const { get, status } = useFetch();
  const [products, setProducts] = useState([]);

  const getProducts = async () => {
    const res = await get("http://127.0.0.1:8000/api/v1/product/list/");
    if (status.current.ok) {
      setProducts(res);
    }
  };

  const product = products.map((p) => {
    return (
      <Product
        key={p.id}
        product_id={p.id}
        name={p.product_name}
        price={p.price_ttc}
        max_quantity={p.stock_available}
      />
    );
  });

  useEffect(() => {
    getProducts();
  }, []);

  return (
    <Container className="h-100">
      <div className="max-w-2xl mx-auto py-16 px-4 sm:py-24 sm:px-6 lg:max-w-7xl lg:px-8">
        <h4 className="text-2xl font-extrabold tracking-tight text-gray-900">
          Produits
        </h4>

        <ListGroup variant="flush">{product}</ListGroup>
      </div>
    </Container>
  );
};

export default Catalog;
