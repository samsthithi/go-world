import React, { Component } from 'react'
// import { register } from './UserFunctions'
import axios from 'axios'


class Register extends Component {
    constructor() {
        super()
        this.state = {
            // first_name: '',
            // last_name: '',
            username: '',
            password: ''
        }

        this.onChange = this.onChange.bind(this)
        this.onSubmit = this.onSubmit.bind(this)
    }

    onChange (e) {
        this.setState({ [e.target.name]: e.target.value })
    }

    onSubmit (e) {
        e.preventDefault()

        const newUser = {
            // first_name: this.state.first_name,
            // last_name: this.state.last_name,
            username: this.state.username,
            password: this.state.password
        };

        axios.post('/register', newUser)
            .then(response => {this.props.history.push(`/login`)})
            .catch(error => console.log(error));

        console.log("Registerd!");
    }

    render () {
        return (
            <div className="container">
                <div className="row">
                    <div className="col-md-6 mt-5 mx-auto">
                        <form noValidate onSubmit={this.onSubmit}>
                            <h1 className="h3 mb-3 font-weight-normal">Register</h1>
                            <div className="form-group">
                                <label htmlFor="username">username</label>
                                <input type="username"
                                    className="form-control"
                                    name="username"
                                    placeholder="Enter username"
                                    value={this.state.username}
                                    onChange={this.onChange} />
                            </div>
                            <div className="form-group">
                                <label htmlFor="password">Password </label>
                                <input type="password"
                                    className="form-control"
                                    name="password"
                                    placeholder="Enter Password"
                                    value={this.state.password}
                                    onChange={this.onChange} />
                            </div>
                            <button type="submit" className="btn btn-lg btn-primary btn-block" onSubmit={this.onSubmit}>
                                Register
                            </button>
                        </form>
                    </div>
                </div>
            </div>
        )
    }
}

export default Register;