import React from 'react'
import styled from '@emotion/styled'

import { Plot } from '~u4x-engine'

const Hexagon = () => {
  return (
    <svg xmlns="http://www.w3.org/2000/svg" x="0" y="0" viewBox="0 0 1000 1000">
      <path d="M500 24.1l412.2 238V738L500 975.9 87.9 738V262L500 24.1m0-14.1L75.6 255v490L500 990l424.4-245V255L500 10z"></path>
    </svg>
  )
}

const TileContainer = styled.div(
  ({ width: width, position: [x, y] }: Props) => `
    width: ${width}px;
    position: fixed;
    top: ${y - Plot.getSide(width)};
    left: ${x - width / 2};

    svg {
      width: ${width}px;
    }
  `,
)

export const Tile = (props: Props) => (
  <TileContainer {...props}>
    <Hexagon />
  </TileContainer>
)

interface Props {
  position: Plot.Position
  width: number
}
