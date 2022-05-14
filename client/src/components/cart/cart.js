import React, { useEffect, useContext } from "react";
import { Button, Container, ListGroup, ListGroupItem } from "react-bootstrap";
import { useCookies } from "react-cookie";
import { useNavigate } from "react-router-dom";

import Item from "../item/item";

import CartContext from "../../contexts/CartContext";
import useFetch from "../../hooks/useFetch";

const Cart = () => {
  let navigate = useNavigate();
  const [cookies, removeCookie] = useCookies();
  const cart = useContext(CartContext);

  const { patch, status } = useFetch();

  const items = cart.cartItems?.map((item) => {
    return (
      <Item
        key={item.id}
        item_id={item.id}
        product_id={item.product_id}
        quantity={item.quantity}
        price={item.total_price}
        getCartItems={cart.getCartItems}
        getCart={cart.getCart}
      ></Item>
    );
  });

  const updateStock = async (cart_item) => {
    const formdata = new FormData();
    formdata.append("stock_ordered", cart_item.quantity);
    patch(
      `http://127.0.0.1:8000/api/v1/product/${cart_item.product_id}/update/`,
      formdata
    );
  };

  const checkedOut = async () => {
    const formdata = new FormData();
    formdata.append("checked_out", true);

    for (const cart_item of cart.cartItems) {
      updateStock(cart_item);
    }

    patch(
      `http://127.0.0.1:8000/api/v1/cart/check-out/${cart.cart.id}/`,
      formdata
    );

    if (status.current?.ok) {
      removeCookie("cart_id");
      cart.createCart();
      navigate("/", { replace: true });
    }
  };

  useEffect(() => {
    cart.getCartItems();
    cart.getCart();
  }, []);
  return (
    <Container className="h-100">
      <h1>Panier</h1>
      <ListGroup variant="flush">
        <ListGroupItem className="d-flex align-items-center justify-content-between">
          <span>Produits</span>
          <span>Prix</span>
          <span>Quantité</span>
        </ListGroupItem>
        {items}
        <ListGroupItem className="d-flex align-items-center justify-content-between">
          <span>Total </span>
          <span>{cart.cart?.total_cart}€</span>
          <span>{cart.cart?.total_items}</span>
        </ListGroupItem>
      </ListGroup>

      <Button
        onClick={() => {
          cart.cart?.total_items > 0 && checkedOut();
        }}
        disabled={cart.cart?.total_items == 0}
      >
        Commander
      </Button>
    </Container>
  );
};

export default Cart;
