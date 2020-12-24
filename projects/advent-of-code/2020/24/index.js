const fs = require('fs')
const util = require('util')

const ITERATIONS = 16

const TESTING = !!process.env.TEST // 2208
const INPUT_PATH = `${__dirname}/${TESTING ? 'test' : 'input'}.txt`

const split = (str, separator = '\n') => str.split(separator).filter((s) => !!s)
const log = (obj) => console.log(util.inspect(obj, false, null, true))

const readInput = async () => {
  const file = await fs.readFileSync(INPUT_PATH, 'utf8')
  return split(file)
}

const run = async () => {
  const input = await readInput()
  const instructions = input.map(parseDirections)
  const positions = instructions.map(getPosition)
  let tiles = positions.reduce(flipTile, {})

  for (let n = 0; n < ITERATIONS; n++) {
    tiles = getEmptyTiles(tiles).reduce(addEmptyTile, tiles)
    tiles = Object.keys(tiles)
      .map(parseTileID)
      .filter((position) => shouldFlip(tiles, position))
      .reduce(flipTile, tiles)
  }

  const count = Object.values(tiles).filter((state) => !!state).length

  console.log(`There are ${count} black tiles after ${ITERATIONS} days.`)
}

const parseDirections = (input) =>
  Array.from(input.matchAll(/(se|sw|ne|nw|e|w)/g)).reduce(
    (directions, [direction]) => [...directions, direction],
    [],
  )

const getPosition = (directions) =>
  directions.map(getOffset).reduce(applyOffset, [0, 0, 0])

const OFFSETS = {
  ne: [0, 1, 1],
  e: [1, 1, 0],
  se: [1, 0, -1],
  sw: [0, -1, -1],
  w: [-1, -1, 0],
  nw: [-1, 0, 1],
}

const getOffset = (direction) => OFFSETS[direction]
const getOffsetPositions = (position) =>
  Object.values(OFFSETS).map((offset) => applyOffset(position, offset))
const applyOffset = ([x, y, z], [x1, y1, z1]) => [x + x1, y + y1, z + z1]

const getTileID = (position) => position.join(',')
const parseTileID = (id) => id.split(',').map(Number)
const getTileState = (tiles, position) => !!tiles[getTileID(position)]
const addEmptyTile = (tiles, position) => ({
  ...tiles,
  [getTileID(position)]: false,
})
const flipTile = (tiles, position) => ({
  ...tiles,
  [getTileID(position)]: !getTileState(tiles, position),
})

const getAdjacentCount = (tiles, position) =>
  getOffsetPositions(position).reduce(
    (count, positionO) => count + (getTileState(tiles, positionO) ? 1 : 0),
    0,
  )

const shouldFlip = (tiles, position) => {
  const count = getAdjacentCount(tiles, position)
  switch (getTileState(tiles, position)) {
    case true:
      return count === 0 || count > 2
    case false:
      return count === 2
  }
}

const getEmptyTiles = (tiles) =>
  Object.keys(tiles)
    .map(parseTileID)
    .reduce(
      (positions, position) => [
        ...positions,
        ...getOffsetPositions(position).filter(
          (positionO) => !getTileState(tiles, positionO),
        ),
      ],
      [],
    )

run()

const EXEC_TIME = {}
const execTime = (key, fn) => {
  const startMs = Date.now()
  const result = fn()
  if (!EXEC_TIME[key]) EXEC_TIME[key] = 0
  EXEC_TIME[key] += Date.now() - startMs
  return result
}
