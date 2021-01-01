import React, { useEffect, useState } from 'react'
import ReactDOM from 'react-dom'

import { Tile } from './tile'
import { useWindowSize } from './hooks'
import { Grid, Plot } from '~u4x-engine'

const TILE_WIDTH = 100

const App = () => {
  const size = useWindowSize()
  const [grid, setGrid] = useState({} as Grid.GridMap<Plot.Position>)

  useEffect(() => {
    if (!size.height || !size.width) return

    const offset: Plot.Position = [
      size.width && size.width / 2,
      size.height && size.height / 2,
    ]

    const map = Grid.createMap<Plot.Position>(Grid.getArea([0, 0], 3))
    Object.keys(map).forEach(
      (id) =>
        (map[id].data = Plot.getPosition({
          axial: map[id].axial,
          width: TILE_WIDTH,
          offset,
        })),
    )
    setGrid(map)
  }, [size])

  return (
    <div>
      {Object.keys(grid).map((id) => {
        const { data: position } = grid[id]
        return <Tile key={id} position={position} width={TILE_WIDTH} />
      })}
    </div>
  )
}

document.title = 'Untitled 4x'
ReactDOM.render(<App />, document.getElementById('app'))
