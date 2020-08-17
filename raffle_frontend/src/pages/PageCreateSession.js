import React from "react";

class PageCreateSession extends React.Component {
  state = {
    sessionName: null,
    hostName: null,
  };
  render() {
    return (
      <div className="ui container">
        <h1 className="ui header centered">Host a Session</h1>
        <div className="ui form">
          <div className="item">
            <label>Host Name</label>
            <input
              type="text"
              onChange={(event) =>
                this.setState({ hostName: event.target.value })
              }
            />
          </div>
          <div className="item">
            <label>Session Name</label>
            <input
              type="text"
              onChange={(event) =>
                this.setState({ sessionName: event.target.value })
              }
            />
          </div>
          <div className="ui submit button">Create Session</div>
        </div>
      </div>
    );
  }
}

export default PageCreateSession;
