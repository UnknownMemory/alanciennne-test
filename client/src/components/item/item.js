import React, { useEffect, useState, useContext } from "react";
import { Button, ListGroupItem, FormControl } from "react-bootstrap";

import CartContext from "../../contexts/CartContext";
import useFetch from "../../hooks/useFetch";

const Item = (props) => {
  const { get, patch, status } = useFetch();
  const [product, setProduct] = useState(null);

  const getProduct = async () => {
    const res = await get(
      `http://127.0.0.1:8000/api/v1/product/${props.product_id}/`
    );
    if (status.current.ok) {
      setProduct(res);
    }
  };

  const updateQuantity = async (quantity) => {
    const formdata = new FormData();
    formdata.append("quantity", quantity);
    await patch(
      `http://127.0.0.1:8000/api/v1/cart/${props.item_id}/update-item/`,
      formdata
    );
    if (status.current.ok) {
      props.getCartItems();
      props.getCart();
    }
  };

  useEffect(() => {
    getProduct();
  }, []);

  return (
    <ListGroupItem className="d-flex align-items-center justify-content-between">
      <span>{product?.product_name}</span>
      <span>{props.price}€</span>
      <div className="d-flex align-items-center">
        <FormControl
          type="number"
          defaultValue={props.quantity}
          min="1"
          max={product?.customer_stock}
          onChange={(e) => updateQuantity(e.target.value)}
        />
      </div>
    </ListGroupItem>
  );
};

export default Item;
