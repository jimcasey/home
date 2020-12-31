import styled from '@emotion/styled'

import { hexWidthToSide, Position } from './hexagonUtils'

const BORDER_WIDTH = 2
const DEFAULT_COLOR = 'rgb(255, 255, 255)' // white

export const Hexagon = styled.div(
  ({
    fillColor = DEFAULT_COLOR,
    width,
    position: [x, y],
  }: {
    fillColor?: string
    width: number
    position: Position
  }) => {
    const hexWidth = width - BORDER_WIDTH
    const hexSide = hexWidthToSide(hexWidth)
    const offset = hexSide / 2
    const border = hexWidth / 2
    const top = y - hexWidth / 2 + offset
    const left = x - hexWidth / 2

    return `
      width: ${hexWidth}px;
      height: ${hexSide}px;
      background: ${fillColor};
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
        border-bottom: ${offset}px solid ${fillColor};
      }
      &::after {
        bottom: ${-offset}px;
        border-top: ${offset}px solid ${fillColor};
      }
    `
  },
)
