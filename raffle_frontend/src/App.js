import React from "react";
import { HashRouter, Route } from "react-router-dom";

import PageHome from "./pages/PageHome";
import PageCreateSession from "./pages/PageCreateSession";

const App = () => {
  return (
    <div className="ui container">
      <HashRouter>
        <Route path="/" exact component={PageHome} />
        <Route path="/host/create" exact component={PageCreateSession} />
      </HashRouter>
    </div>
  );
};

export default App;
