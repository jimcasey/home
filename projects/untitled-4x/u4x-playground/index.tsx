import React, { useEffect } from 'react'
import ReactDOM from 'react-dom'

import { Tile } from './grid/tile'
import { useWindowSize } from './utils/hooks'

const App = () => {
  const size = useWindowSize()

  const x = size.height && size.height / 2
  const y = size.width && size.width / 2

  return (
    <div>
      <Tile x={x} y={y} />
    </div>
  )
}

document.title = 'Untitled 4x'
ReactDOM.render(<App />, document.getElementById('app'))
