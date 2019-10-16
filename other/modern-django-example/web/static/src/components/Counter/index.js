import { bindActionCreators } from 'redux'
import { connect } from 'react-redux'

import * as actions from '../../actions'

import Counter from './component.js'

const mapStateToProps = state => ({ value: state.counter.value })

const mapDispatchToProps = dispatch => {
    return {
        actions: bindActionCreators(actions, dispatch),
    }
}


export default connect(
    mapStateToProps,
    mapDispatchToProps
)(Counter)
