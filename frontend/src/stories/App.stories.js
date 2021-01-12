/* eslint-disable import/no-anonymous-default-export */

import App from "../App";
// import axios from "axios";
import { MemoryRouter } from "react-router-dom";
// import MockAdapter from "axios-mock-adapter"
import React from "react";

export default {
  component: App,
  decorators: [],
  title: "App",
};

export const Example = () => {
  // const mock = new MockAdapter(axios);

  return (
    <MemoryRouter initialEntries={["/"]}>
      <App />
    </MemoryRouter>
  );
};
