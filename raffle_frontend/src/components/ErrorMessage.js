import React from "react";

export default ({ errMsg, touched }) => {
  if (touched && errMsg) {
    return (
      <div className="ui error message">
        <div className="header">{errMsg}</div>
      </div>
    );
  }
  return null;
};
