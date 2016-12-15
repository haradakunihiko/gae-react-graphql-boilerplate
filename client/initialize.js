import './styles/application.css';
import './styles/graphiql.css'

import React from 'react';
import ReactDOM from 'react-dom';
import Root from './app/root';

document.addEventListener('DOMContentLoaded', () => {
	ReactDOM.render(<Root />, document.getElementById('app'));
});
