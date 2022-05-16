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
        max_quantity={p.customer_stock}
      />
    );
  });

  useEffect(() => {
    getProducts();
  }, []);

  return (
    <Container className="h-100">
      <div className="text-center my-5">
        <h1>Produits</h1>
      </div>

      <ListGroup variant="flush" as="ul">
        {product}
      </ListGroup>
    </Container>
  );
};

export default Catalog;
