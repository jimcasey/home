const fs = require('fs')
const util = require('util')

const TESTING = !!process.env.TEST // 20
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

  const tiles = positions
    .map((position) => position.join(','))
    .reduce((map, id) => ({ ...map, [id]: !map[id] }), {})

  const count = Object.values(tiles).filter((state) => state).length

  console.log(`Floor contains ${count} black tiles.`)
}

const parseDirections = (input) =>
  Array.from(input.matchAll(/(se|sw|ne|nw|e|w)/g)).reduce(
    (directions, [direction]) => [...directions, direction],
    [],
  )

const getPosition = (directions) =>
  directions
    .map(getOffset)
    .reduce(([x, y, z], [x1, y1, z1]) => [x + x1, y + y1, z + z1], [0, 0, 0])

const getOffset = (direction) => {
  switch (direction) {
    case 'ne':
      return [0, 1, 1]
    case 'e':
      return [1, 1, 0]
    case 'se':
      return [1, 0, -1]
    case 'sw':
      return [0, -1, -1]
    case 'w':
      return [-1, -1, 0]
    case 'nw':
      return [-1, 0, 1]
  }
}

run()
