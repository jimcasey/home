import React from 'react'
import ReactDOM from 'react-dom'

import { createGrid } from '~u4x-engine'

const grid = createGrid()
console.log('grid', grid)

document.title = 'Untitled 4x'
ReactDOM.render(
  <div>Untitled 4x Playground</div>,
  document.getElementById('app'),
)
