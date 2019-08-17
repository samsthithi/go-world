import React from 'react';

import classes from './NavigationItems.css';
import NavigationItem from './NavigationItem/NavigationItem';

const navigationItems = () => (
    <ul className={classes.NavigationItems}>
        <NavigationItem link="/" exact>Authenticate</NavigationItem>
        <NavigationItem link="/profile">Profile</NavigationItem>
        <NavigationItem link="/home">Home</NavigationItem>
    </ul>
);

export default navigationItems;