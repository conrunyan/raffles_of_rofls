import "./PageHome.css";
import React from "react";
import { Link } from "react-router-dom";

class PageHome extends React.Component {
  render() {
    return (
      <div className="ui container">
        <div className="title">
          <img
            className="ui small image"
            src="https://cdn.pixabay.com/photo/2014/04/03/00/39/ice-cream-308972_960_720.png"
            alt="icecream"
          />
          <h1 className="centered">Home Page</h1>
          <div className="ui borderless menu">
            <div className="horizontally fitted item">
              <Link to="/host/create">
                <button className="ui teal button">Host Raffle</button>
              </Link>
            </div>
            <div className="horizontally fitted item">
              <Link to="/participant/join">
                <button className="ui blue button">Join Raffle</button>
              </Link>
            </div>
          </div>
        </div>
      </div>
    );
  }
}

export default PageHome;
