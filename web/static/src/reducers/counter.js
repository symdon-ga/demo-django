import { INCREMENT, DECREMENT } from '../constants/ActionTypes'

// import axios from 'axios'


const initialState = {
    value: 0
}


export default (state = initialState, action) => {
    // axios.get('/api/counter/2/increment/').then((response) => {
    //     console.log(response)
    // })

    switch(action.type) {
    case INCREMENT:
        return {
            value: state.value + 1,
        }
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
