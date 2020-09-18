import React from "react";
import { HashRouter, Route } from "react-router-dom";
import { createStore, applyMiddleware, compose } from "redux";
import { Provider } from "react-redux";
import reduxThunk from "redux-thunk";

import PageHome from "./pages/PageHome";
import PageCreateSession from "./pages/PageCreateSession";

import reducers from "./redux/reducers";

const composeEnhancers = window.__REDUX_DEVTOOLS_EXTENSION_COMPOSE__ || compose;
const store = createStore(
  reducers,
  composeEnhancers(applyMiddleware(reduxThunk))
);

const App = () => {
  return (
    <Provider store={store}>
      <div className="ui container">
        <HashRouter>
          <Route path="/" exact component={PageHome} />
          <Route path="/host/create" exact component={PageCreateSession} />
        </HashRouter>
      </div>
    </Provider>
  );
};

export default App;
