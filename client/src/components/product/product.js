import React, { useEffect, useState, useContext } from "react";
import { Button, ListGroupItem, FormControl } from "react-bootstrap";

import CartContext from "../../contexts/CartContext";
import useFetch from "../../hooks/useFetch";

const Product = (props) => {
  const cart = useContext(CartContext);
  const { post } = useFetch();
  const [quantity, setQuantity] = useState(1);

  const addToCart = async () => {
    const formdata = new FormData();
    formdata.append("cart_id", cart.cart.id);
    formdata.append("product_id", props.product_id);
    formdata.append("quantity", quantity);

    await post("http://127.0.0.1:8000/api/v1/cart/add-item/", formdata);
  };

  return (
    <ListGroupItem className="d-flex align-items-center justify-content-between">
      <span>{props.name}</span>
      <div className="d-flex align-items-center">
        <span>{props.price}€</span>
        <FormControl
          type="number"
          defaultValue="1"
          min="1"
          max={props.max_quantity}
          onChange={(e) => setQuantity(e.target.value)}
        />
        <Button onClick={addToCart} variant="outline-dark">
          Ajouter au panier
        </Button>
      </div>
    </ListGroupItem>
  );
};

export default Product;
