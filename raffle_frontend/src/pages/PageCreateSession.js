import React from "react";
import { Field, reduxForm } from "redux-form";
import { connect } from "react-redux";

import FormInput from "../components/FormInput";
import ErrorMessage from "../components/ErrorMessage";
import { createSession } from "../redux/actions";

class PageCreateSession extends React.Component {
  renderInput = ({ input, label, meta }) => {
    const className = meta.touched && meta.error ? "field error" : "field";
    return (
      <FormInput
        className={className}
        label={label}
        input={{ ...input }}
        errComponent={
          <ErrorMessage errMsg={meta.error} touched={meta.touched} />
        }
      />
    );
  };

  onSubmit = (formData) => {
    this.props.createSession(formData);
  };

  render() {
    return (
      <div className="ui container">
        <h1 className="ui header centered">Host a Session</h1>
        <form className="ui form error" onSubmit={this.props.handleSubmit(this.onSubmit)}>
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
          <button className="ui button primary">Create Session</button>
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
  form: "pageCreateSession",
  validate: validate,
})(PageCreateSession);

export default connect(null, {
  createSession,
})(formWrapped);
