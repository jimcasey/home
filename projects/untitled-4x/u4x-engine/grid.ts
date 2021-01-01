export type Axial = [number, number] // q, r

export const getAxialID = (axial: Axial) => axial.join(',')
export const getAxial = (id: string) => id.split(',').map(Number) as Axial

const DIRECTIONS = ['E', 'SE', 'SW', 'W', 'NW', 'NE']
type Direction = typeof DIRECTIONS[number]

const DIRECTION_OFFSETS = {
  E: [1, 0],
  SE: [0, 1],
  SW: [-1, 1],
  W: [-1, 0],
  NW: [0, -1],
  NE: [1, -1],
}

export const getNeighbor = (
  [q, r]: Axial,
  direction: Direction,
  distance = 1,
): Axial => {
  const [q1, r1] = DIRECTION_OFFSETS[direction]
  return [q + q1 * distance, r + r1 * distance]
}

export const getRing = (center: Axial, radius: number) => {
  if (radius === 0) return [center]

  let axial = getNeighbor(center, 'NW', radius)
  return DIRECTIONS.reduce((ring: Axial[], direction) => {
    for (let r = 0; r < radius; r++) {
      ring.push(axial)
      axial = getNeighbor(axial, direction)
    }
    return ring
  }, [])
}

export const getArea = (center: Axial, radius: number) => {
  let area: Axial[] = []
  for (let r = 0; r <= radius; r++) area.push(...getRing(center, r))
  return area
}

export interface GridItem<T = void> {
  axial: Axial
  data: T | undefined
}

export interface GridMap<T = void> {
  [id: string]: GridItem<T>
}

export const createMap = <T = void>(axials: Axial[]) =>
  axials.reduce((grid: GridMap<T>, axial) => {
    grid[getAxialID(axial)] = { axial, data: undefined }
    return grid
  }, {})
