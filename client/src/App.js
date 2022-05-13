import React, { Fragment, useEffect, useState } from "react";
import { Routes, Route } from "react-router-dom";
import { useCookies } from "react-cookie";

import Catalog from "./components/catalog/catalog";
import Header from "./components/header/header";
import CartContext from "./contexts/CartContext";
import useFetch from "./hooks/useFetch";

import "./App.scss";

const App = () => {
  const { get, post, status } = useFetch();
  const [cart, setCart] = useState(null);
  const [cookies, setCookie] = useCookies();

  const createCart = async () => {
    const res = await post("http://127.0.0.1:8000/api/v1/cart/create/");
    if (status.current.ok) {
      setCart(res);
      setCookie("cart_id", res.id);
    }
  };

  const getCart = async () => {
    const res = await get(
      `http://127.0.0.1:8000/api/v1/cart/get/${cookies.cart_id}/`
    );
    if (!cookies.cart_id) {
      createCart();
    } else {
      setCart(res);
    }
  };

  useEffect(() => {
    getCart();
  }, []);

  return (
    <Fragment>
      <Header />
      <CartContext.Provider value={{ cart: cart, getCart: getCart }}>
        <Routes>
          <Route path="/" element={<Catalog />} />
        </Routes>
      </CartContext.Provider>
    </Fragment>
  );
};

export default App;
