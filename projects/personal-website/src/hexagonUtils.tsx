const SIDE_CONST = 1 / Math.sqrt(3)

export const createGrid = ({
  width: gridWidth = 600,
  height: gridHeight = 400,
  columns = 6,
} = {}) => {
  const hexWidth = gridWidth / (columns - 0.5)
  const rowHeight = hexWidthToRowHeight(hexWidth)
  const rows = Math.ceil(gridHeight / rowHeight) + 1

  const grid: GridMap = {}
  for (let row = 0; row < rows; row++) {
    for (let col = 0; col < columns; col++) {
      const offset = { row, col }
      const axial = offsetToAxial(offset)
      grid[axialToID(axial)] = {
        position: offsetToPosition(offset, hexWidth),
        axial,
        width: hexWidth,,
      }
    }
  }
  return {
    hexWidth,
    grid,
  }
}

const getRandomValue = () => Math.floor(Math.random() * Math.floor(255))

export const getGridItemColor = (grid: GridMap, id: string) => ({
  r: getRandomValue(),
  g: getRandomValue(),
  b: getRandomValue(),
})

const axialToID = ({ q, r }: Axial) => `${q},${r}`

const axialToOffset = ({ q, r }: Axial): Offset => ({
  col: q + (r - (r & 1)) / 2,
  row: r,
})

const offsetToAxial = ({ col, row }: Offset): Axial => ({
  q: col - (row - (row & 1)) / 2,
  r: row,
})

const offsetToPosition = (
  { col, row }: Offset,
  hexWidth: number,
): Position => ({
  x: col * hexWidth + (row & 1) * (hexWidth / 2),
  y: row * hexWidthToRowHeight(hexWidth),
})

export const hexWidthToSide = (hexWidth) => hexWidth * SIDE_CONST
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

export interface Axial {
  q: number
  r: number
}

export interface Offset {
  col: number
  row: number
}

export interface Position {
  x: number
  y: number
}

export interface Color {
  r: number
  g: number
  b: number
}
