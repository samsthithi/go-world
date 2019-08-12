import React, { Component } from 'react'
import Profile from '../Profile/Profile';
import { BrowserRouter as Router, Route } from 'react-router-dom';

import NavBar from '../../components/Navigation/Navigation';
import Layout from '../../hoc/Layout/Layout';

class Auth extends Component {
    render () {
        let check = null;
        if (check!==null) {
            check = <Route exact path="/profile" component={Profile} />
        }
        return (
            <div>
                <Layout>
                    <NavBar />
                    {check}
                </Layout>
            </div>
        );
    }
}

export default Auth;
