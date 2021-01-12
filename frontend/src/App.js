import React from "react";
import { Route, Switch } from "react-router";


const App = function() {
  return (
    <Switch>
      <Route
        path="*"
        component={() => (
          <h1>404</h1>
        )} />
    </Switch>
  );
}

export default App;
