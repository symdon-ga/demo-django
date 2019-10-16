import React from 'react'
import ReactDOM from 'react-dom'

import { createStore, applyMiddleware } from 'redux'
import { Provider } from 'react-redux'

import createHistory from 'history/createBrowserHistory'
import { Route } from 'react-router'

import { ConnectedRouter } from 'react-router-redux'
import thunk from 'redux-thunk'

import Counter from './components/Counter'
import Testing from './components/Testing'
import Login from './components/Login'
import reducer from './reducers';

const history = createHistory()
const rootEl = document.getElementById('root')


const store = createStore(
    reducer, applyMiddleware(thunk))


ReactDOM.render(
    (
        <Provider store={store}>
            <ConnectedRouter history={history}>
                <div>
                    <Route exact path="/" component={Counter} />
                    <Route path="/testing" component={Testing} />
                    <Route path="/login" component={Login} />
                </div>
            </ConnectedRouter>
        </Provider>
    ),
    rootEl
)
