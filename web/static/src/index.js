import React from 'react'
import ReactDOM from 'react-dom'

import { createStore, combineReducers, applyMiddleware } from 'redux'
import { Provider } from 'react-redux'

import createHistory from 'history/createBrowserHistory'
import { Route } from 'react-router'

import { ConnectedRouter, routerReducer, routerMiddleware } from 'react-router-redux'

import Counter from './components/Counter'
import reducer from './reducers';

const history = createHistory()
const middleware = routerMiddleware(history)
const rootEl = document.getElementById('root')

const store = createStore(reducer)

ReactDOM.render(
    (
        <Provider store={store}>
            <ConnectedRouter history={history}>
                <Route exact path="/" component={Counter} />
            </ConnectedRouter>
        </Provider>
    ),
    rootEl
)
