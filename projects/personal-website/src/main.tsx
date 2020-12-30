import React from 'react'
import ReactDOM from 'react-dom'

import { HexagonGrid } from './hexagonGrid'

const App = () => (
  <div>
    <HexagonGrid />
  </div>
)

const Bio = () => (
  <div>
    <em>Jim Casey</em> is a human who helps make awesome software things for
    Workday in Colorado.
  </div>
)

document.title = 'Human'
ReactDOM.render(<App />, document.getElementById('app'))
