import { random } from './utils'

enum Direction {
  E = 0,
  SE = 1,
  SW = 2,
  W = 3,
  NW = 4,
  NE = 5,
}

const DIRECTIONS = [
  [1, 0], //  E
  [0, 1], // SE
  [-1, 1], // SW
  [-1, 0], //  W
  [0, -1], // NW
  [1, -1], // NE
]

export const createGrid = (gridWidth: number, gridHeight: number, columns) => {
  const hexWidth = gridWidth / (columns - 0.5)
  const rowHeight = hexWidthToRowHeight(hexWidth)
  const rows = Math.ceil(gridHeight / rowHeight) + 1

  const grid: GridMap = {}
  for (let row = 0; row < rows; row++) {
    for (let col = 0; col < columns; col++) {
      const offset: Offset = [col, row]
      const axial = offsetToAxial(offset)
      grid[axialToID(axial)] = {
        position: offsetToPosition(offset, hexWidth),
        axial,
        width: hexWidth,
      }
    }
  }
  return {
    hexWidth,
    grid,
  }
}

export const getRipple = (grid: GridMap, centerID: string, radius: number) => {
  if (radius === 0) {
    return {
      [centerID]: {
        ...grid[centerID],
        color: getRandomColor(),
      },
    }
  }

  const center = idToAxial(centerID)
  const { color } = grid[centerID]

  const ring = getRing(center, radius)
  const items = ring.reduce((obj, axial) => {
    const id = axialToID(axial)
    const item = grid[id]
    if (item) {
      obj[id] = {
        ...item,
        color: getNextColor(color, 1 - (radius - 1) / 10),
      }
    }
    return obj
  }, {})

  return Object.keys(items).length ? items : undefined
}

const getRandomColor = (): Color => [
  random(160, 210),
  random(160, 210),
  random(160, 210),
  1,
]

const getNextColor = (colorA: Color, opacity, colorB?: Color) => [
  ...colorA.slice(0, 3),
  opacity,
]

const getRing = (center: Axial, radius: number) => {
  if (radius === 0) return [center]

  let axial = getNeighbor(center, Direction.NW, radius)
  return DIRECTIONS.reduce((ring: Axial[], _, index) => {
    for (let r = 0; r < radius; r++) {
      ring.push(axial)
      axial = getNeighbor(axial, index)
    }
    return ring
  }, [])
}

const getNeighbor = (
  [q, r]: Axial,
  direction: Direction,
  distance = 1,
): Axial => {
  const [q1, r1] = DIRECTIONS[direction]
  return [q + q1 * distance, r + r1 * distance]
}

const axialToID = (axial: Axial) => axial.join(',')

const idToAxial = (id: string) => id.split(',').map(Number) as Axial

const axialToOffset = ([q, r]: Axial): Offset => [q + (r - (r & 1)) / 2, r]

const offsetToAxial = ([col, row]: Offset): Axial => [
  col - (row - (row & 1)) / 2,
  row,
]

const offsetToPosition = ([col, row]: Offset, hexWidth: number): Position => [
  col * hexWidth + (row & 1) * (hexWidth / 2),
  row * hexWidthToRowHeight(hexWidth),
]

export const hexWidthToSide = (hexWidth) => hexWidth * (1 / Math.sqrt(3))
const hexWidthToRowHeight = (hexWidth) => hexWidthToSide(hexWidth) * 1.5

interface GridItem {
  axial: Axial
  position: Position
  width: number
  color?: Color
}

export interface GridMap {
  [id: string]: GridItem
}

type Axial = [number, number] // q, r
type Offset = [number, number] // col, row
export type Position = [number, number] // x, y
type Color = [number, number, number, number] // r, g, b, a
