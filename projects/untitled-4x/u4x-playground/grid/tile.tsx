import React from 'react'
import styled from '@emotion/styled'

const TILE_WIDTH = 100

const Hexagon = () => {
  return (
    <svg
      xmlns="http://www.w3.org/2000/svg"
      x="0"
      y="0"
      viewBox="0 0 1000 1000"
      width="100%"
    >
      <path d="M500 24.1l412.2 238V738L500 975.9 87.9 738V262L500 24.1m0-14.1L75.6 255v490L500 990l424.4-245V255L500 10z"></path>
    </svg>
  )
}

const TileContainer = styled.div(
  ({ width, x, y }: { width: number; x: number; y: number }) => `
    width: ${width}px;
    height: ${width}px;
    position: fixed;
    top: ${y - width / 2};
    left: ${x - width / 2};
  `,
)

export const Tile = ({ x, y }: { x?: number; y?: number }) => {
  if (x === undefined || y === undefined) return <></>

  return (
    <TileContainer x={x} y={y} width={TILE_WIDTH}>
      <Hexagon />
    </TileContainer>
  )
}
