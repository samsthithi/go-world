import React from 'react';

import NavigationItem from './NavigationItem/NavigationItem';

const navigationItems = (props) => (
    <ul >
        <NavigationItem link="/" exact>Authntication</NavigationItem>
    </ul>
);

export default navigationItems;