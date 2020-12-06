const fs = require('fs')

const INPUT_PATH = `${__dirname}/input.txt`
const TEST_PATH = `${__dirname}/test.txt`

const readLines = async () => {
  const file = await fs.readFileSync(INPUT_PATH, 'utf8')
  return file.split('\n').filter((line) => !!line)
}

const DIRECTIONS = ['N', 'E', 'S', 'W']

const findNewDirection = (direction, action, angle) => {
  let rotateOffset = angle / 90
  if (action === 'L') rotateOffset = 0 - rotateOffset

  let index = (DIRECTIONS.indexOf(direction) + rotateOffset) % DIRECTIONS.length
  if (index < 0) index += DIRECTIONS.length

  return DIRECTIONS[index]
}

const run = async () => {
  const lines = await readLines()

  const actions = lines.map((line) => ({
    action: line.substr(0, 1),
    distance: Number(line.substr(1)),
  }))

  let currentDirection = 'E'
  let position = actions.reduce(
    (pos, { action, distance }) => {
      switch (action === 'F' ? currentDirection : action) {
        case 'N':
          return [pos[0] - distance, pos[1]]
        case 'S':
          return [pos[0] + distance, pos[1]]
        case 'E':
          return [pos[0], pos[1] + distance]
        case 'W':
          return [pos[0], pos[1] - distance]
      }

      currentDirection = findNewDirection(currentDirection, action, distance)

      return pos
    },
    [0, 0],
  )

  const answer = position.reduce((pos, value) => pos + Math.abs(value))

  console.log(`The answer is ${answer}`)
}

run()
