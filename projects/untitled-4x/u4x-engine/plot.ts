import { Axial } from './grid'

export const getSide = (width) => width * (1 / Math.sqrt(3))
export const getRowHeight = (width) => getSide(width) * 1.5

type Offset = [number, number] // col, row
const getOffset = ([q, r]: Axial): Offset => [q + (r - (r & 1)) / 2, r]

export type Position = [number, number] // x, y
export const getPosition = ({
  axial,
  width,
  round = true,
  offset = [0, 0],
}: {
  axial: Axial
  width: number
  round?: boolean
  offset?: Position
}) => {
  const [col, row] = getOffset(axial)
  let position = [
    col * width + (row & 1) * (width / 2),
    row * getRowHeight(width),
  ]
  if (round) position = position.map(Math.round)
  return position.map((value, index) => value + offset[index]) as Position
}
