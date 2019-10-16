import { INCREMENT, DECREMENT } from '../constants/ActionTypes'


const initialState = {
    value: 0
}



export default (state = initialState, action) => {
    switch(action.type) {
    case INCREMENT:
        return {
            value: action.count,
        }
    case DECREMENT:
        return {
            value: action.count,
        }
    default:
        return {
            value: state.value,
        }
    }
}
