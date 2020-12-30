import styled from '@emotion/styled'

import { Color, hexWidthToSide, Position } from './hexagonUtils'

const DEFAULT_SIZE = 100
const DEFAULT_COLOR = { r: 0, g: 0, b: 0 }
const DEFAULT_POSITION = { x: 0, y: 0 }

export const Hexagon = styled.div(
  ({
    width = DEFAULT_SIZE,
    fillColor = DEFAULT_COLOR,
    position = DEFAULT_POSITION,
  }: {
    width?: number
    fillColor?: Color
    position?: Position
  }) => {
    const hexWidth = width + 2
    const hexSide = hexWidthToSide(hexWidth)
    const offset = hexSide / 2
    const border = hexWidth / 2

    const { r, g, b } = fillColor
    const colorString = `rgb(${r}, ${g}, ${b})`

    const { x, y } = position
    const top = y - hexWidth / 2 + offset
    const left = x - hexWidth / 2

    return `
      width: ${hexWidth}px;
      height: ${hexSide}px;
      background: ${colorString};
      position: fixed;
      top: ${top};
      left: ${left};

      &::before,
      &::after {
        content: '';
        position: absolute;
        left: 0;
        width: 0;
        height: 0;
        border-left: ${border}px solid transparent;
        border-right: ${border}px solid transparent;
      }
      &::before {
        top: ${-offset}px;
        border-bottom: ${offset}px solid ${colorString};
      }
      &::after {
        bottom: ${-offset}px;
        border-top: ${offset}px solid ${colorString};
      }
    `
  },
)
