import { INCREMENT, DECREMENT } from '../constants/ActionTypes'

import axios from 'axios'


const initialState = {
    value: 0
}


export default (state = initialState, action) => {

    switch(action.type) {
    case INCREMENT:
        return axios.get('/api/counter/2/increment/').then((response) => {
            return {
                value: response.data.value + 1,
            }
        })
    case DECREMENT:
        return {
            value: state.value - 1,
        }
    default:
        return {
            value: state.value,
        }
    }
}
