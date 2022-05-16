import React, { useState, useContext } from "react";
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
    cart.getCartItems();
  };

  return (
    <ListGroupItem
      className="d-flex align-items-center justify-content-between"
      as="li"
    >
      <span className="w-100">{props.name}</span>

      <span>{props.price}€</span>
      <FormControl
        className="catalog-product mx-4"
        type="number"
        defaultValue={props.max_quantity === 0 ? 0 : 1}
        min={props.max_quantity === 0 ? 0 : 1}
        max={props.max_quantity}
        onChange={(e) => setQuantity(e.target.value)}
      />
      <Button
        className="w-25"
        onClick={props.max_quantity === 0 ? null : addToCart}
        variant="outline-dark"
        disabled={props.max_quantity === 0}
      >
        Ajouter au panier
      </Button>
    </ListGroupItem>
  );
};

export default Product;
