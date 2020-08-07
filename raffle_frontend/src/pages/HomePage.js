import "./HomePage.css";
import React from "react";

class HomePage extends React.Component {
  render() {
    return (
      <div className="ui container">
        <div className="title">
          <img
            className="ui small image"
            src="https://cdn.pixabay.com/photo/2014/04/03/00/39/ice-cream-308972_960_720.png"
          />
          <h1 className="centered">Home Page</h1>
          <div className="button-container">
            <button className="ui teal button">Host Raffle</button>
            <button className="ui blue button">Join Raffle</button>
          </div>
        </div>
      </div>
    );
  }
}

export default HomePage;
