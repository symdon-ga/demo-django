import * as types from '../constants/ActionTypes'
import axios from 'axios'

const startRequest = () => ({type: types.REQUEST_START})
const successRequest = () => ({type: types.REQUEST_SUCCESS})
const errorRequest = () => ({type: types.REQUEST_ERROR})

const instance = axios.create({
    headers: {
        'Authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoxLCJ1c2VybmFtZSI6InN4aW1hZGEiLCJleHAiOjE1MTE3NDEzNTQsImVtYWlsIjoic3hpbWFkYUBnbWFpbC5jb20ifQ.PRg92_CuU8RrGGO1ylvKI_EjvUmrzOT2oFVRsSJTCyM',
    },
})



export const incrementCounter = (count) => ({
    type: types.INCREMENT,
    count: count,
})

export const doIncrement = () => (dispatch) => {
    dispatch(startRequest())
    return instance.get('http://127.0.0.1:8000/api/counter/2/increment/').then(res => {
        dispatch(successRequest())
        dispatch(incrementCounter(res.data.count))
    })
}


export const decrementCounter = (count) => ({
    type: types.DECREMENT,
    count: count,
})

export const doDecrement = () => (dispatch) => {
    dispatch(startRequest())
    return instance.get('http://127.0.0.1:8000/api/counter/2/decrement/').then(res => {
        dispatch(successRequest())
        dispatch(incrementCounter(res.data.count))
    })
}


export const login = (username, password) => ({
    type: types.LOGIN,
    username: username,
    password: password,
})

export const doLogin = () => (dispatch) => {
    dispatch(startRequest())
    return instance.post('http://127.0.0.1:8000/auth/token/', {
        username: 'sximada',
        password: 'adminadmin',
    }).then(res => {
        console.log(res)
        dispatch(successRequest())
    })
}
