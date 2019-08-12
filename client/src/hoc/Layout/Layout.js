import React, { Component } from 'react';
import { BrowserRouter as Router, Route } from 'react-router-dom'
import Aux from '../Aux/Aux'
import Auth from '../../containers/Auth/Auth';
import NavBar from '../../components/Navigation/Navigation';
class Layout extends Component {
    render () {

        return (
            <Aux>
                <Router>
                    <div>
                        <NavBar />
                        <Route exact path="/" component={Auth} />
                        {/* {check} */}
                    </div>
                </Router>
            </Aux>
        );
    }
};

export default Layout;