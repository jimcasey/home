import React from 'react'

import { createGrid, getGridItemColor, GridMap } from './hexagonUtils'
import { Hexagon } from './hexagon'

export const HexagonGrid = () => {
  const { clientWidth: width, clientHeight: height } = document.documentElement
  const { grid, hexWidth } = createGrid({ height, width, columns: 12 })

  const colorGrid = Object.keys(grid).reduce((obj: GridMap, id) => {
    obj[id] = { ...grid[id], color: getGridItemColor(grid, id) }
    return obj
  }, {})

  return (
    <>
      {Object.keys(colorGrid).map((id) => {
        const { position, color } = colorGrid[id]
        return (
          <Hexagon
            key={id}
            position={position}
            width={hexWidth}
            fillColor={color}
          />
        )
      })}
    </>
  )
}
