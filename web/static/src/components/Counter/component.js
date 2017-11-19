import React from 'react'
import PropTypes from 'prop-types'

import template from './template.pug';


const Counter = ({value,  actions}) => template.call(this, {value,  actions})


Counter.propTypes = {
    value: PropTypes.number.isRequired,
    actions: PropTypes.object.isRequired,
}


export default Counter
