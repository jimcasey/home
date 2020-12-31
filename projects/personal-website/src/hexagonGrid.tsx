import React, { useEffect, useState } from 'react'

import { createGrid, getRipple } from './hexagonUtils'
import { Hexagon } from './hexagon'
import { random } from './utils'

// TODO: handle window resize
const { clientWidth, clientHeight } = document.documentElement
const { grid: startGrid, hexWidth } = createGrid(clientWidth, clientHeight, 12)

const RIPPLE_MS = 2500

export const HexagonGrid = () => {
  const [grid, setGrid] = useState(startGrid)
  const [ripple, setRipple] = useState<
    { id: string; radius: number } | undefined
  >(undefined)

  useEffect(() => {
    setInterval(() => {
      const ids = Object.keys(grid)
      setRipple({ id: ids[random(ids.length - 1)], radius: 0 })
    }, random(RIPPLE_MS, RIPPLE_MS * 2))
  }, [])

  useEffect(() => {
    if (!ripple) return

    const { id, radius } = ripple
    const items = getRipple(grid, id, radius)

    if (!items) return

    setGrid({
      ...grid,
      ...items,
    })

    setTimeout(
      () => setRipple({ id, radius: radius + 1 }),
      10 + Math.log(radius) * 75,
    )
  }, [ripple])

  return (
    <>
      {Object.keys(grid).map((id) => {
        const { position, color } = grid[id]

        const fillColor = color ? `rgba(${color.join(',')})` : undefined

        return (
          <Hexagon
            key={id}
            position={position}
            width={hexWidth}
            fillColor={fillColor}
          />
        )
      })}
    </>
  )
}
