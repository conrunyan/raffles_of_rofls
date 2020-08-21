import React from "react";
import { Field, reduxForm } from "redux-form";
import { connect } from "react-redux";

class PageCreateSession extends React.Component {
  renderError({ error, touched }) {
    if (touched && error) {
      return (
        <div className="ui error message">
          <div className="header">{error}</div>
        </div>
      );
    }
  }
  renderInput = ({ input, label, meta }) => {
    console.log(meta);
    const className = meta.touched && meta.error ? "field error" : "field";
    return (
      <div className={className}>
        <label>{label}</label>
        <input {...input} autoComplete="off" />
        {this.renderError(meta)}
      </div>
    );
  };

  render() {
    return (
      <div className="ui container">
        <h1 className="ui header centered">Host a Session</h1>
        <form className="ui form error">
          <Field
            name="hostName"
            component={this.renderInput}
            label={"Host Name"}
          />
          <Field
            name="sessionName"
            component={this.renderInput}
            label={"Session Name"}
          />
          <div className="ui submit button">Create Session</div>
        </form>
      </div>
    );
  }
}

const validate = (formValues) => {
  const errors = {};
  if (!formValues.hostName) {
    errors.hostName = "Host Name cannot be blank.";
  }
  if (!formValues.sessionName) {
    errors.sessionName = "Session Name cannot be blank.";
  }

  return errors;
};

const formWrapped = reduxForm({
  form: "streamCreate",
  validate: validate,
})(PageCreateSession);

export default connect(null, {})(formWrapped);
