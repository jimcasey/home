import React from 'react'
import styled from '@emotion/styled'

import { Plot } from '~u4x-engine'

const Hexagon = () => {
  return (
    <svg
      xmlns="http://www.w3.org/2000/svg"
      width="174"
      height="200"
      viewBox="0 0 173.20508075688772 200"
    >
      <path
        fill="#fff"
        stroke="#000"
        d="M73.61215932167728 7.499999999999999Q86.60254037844386 0 99.59292143521044 7.499999999999999L160.21469970012114 42.5Q173.20508075688772 50 173.20508075688772 65L173.20508075688772 135Q173.20508075688772 150 160.21469970012114 157.5L99.59292143521044 192.5Q86.60254037844386 200 73.61215932167728 192.5L12.99038105676658 157.5Q0 150 0 135L0 65Q0 50 12.99038105676658 42.5Z"
      ></path>
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

export const Tile = (props: Props) => {
  const height = Plot.getSide(props.width) * 2
  console.log(props.width, height)
  return (
    <TileContainer {...props}>
      <Hexagon />
    </TileContainer>
  )
}

interface Props {
  position: Plot.Position
  width: number
}
