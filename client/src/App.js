import React, { Component } from 'react';
import { Route, Switch } from 'react-router-dom';

import Auth from './containers/Auth/Auth';
import Layout from './hoc/Layout/Layout';
// import Profile from './containers/Profile/Profile';

class App extends Component {
  render() {
    return (
        <div >
          <Layout>
            <Switch>
              <Route exact path='/' Component={Auth} />
              {/* <Route path='/profile' Component={Profile} /> */}
            </Switch>
          </Layout>
        </div>
    );
  }
}

export default App;
