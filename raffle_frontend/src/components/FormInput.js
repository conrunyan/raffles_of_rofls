import React from "react";

export default ({label, input, className, errComponent}) => {
  return (
    <div className={className}>
      <label>{label}</label>
      <input {...input} autoComplete="off" />
      {errComponent}
    </div>
  );
};
