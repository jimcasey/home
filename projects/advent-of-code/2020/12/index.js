const fs = require('fs')

const INPUT_PATH = `${__dirname}/input.txt`
const TEST_PATH = `${__dirname}/test.txt`

const readLines = async () => {
  const file = await fs.readFileSync(INPUT_PATH, 'utf8')
  return file.split('\n').filter((line) => !!line)
}

const rotateWaypoint = (waypoint, angle) => {
  const radians = (Math.PI / 180) * angle
  const cos = Math.cos(radians)
  const sin = Math.sin(radians)

  return [
    Math.round(cos * waypoint[0] + sin * waypoint[1]),
    Math.round(cos * waypoint[1] - sin * waypoint[0]),
  ]
}

const findNextPosition = (ship, waypoint, action, unit) => {
  switch (action) {
    case 'F':
      return {
        ship: [ship[0] + waypoint[0] * unit, ship[1] + waypoint[1] * unit],
        waypoint,
      }
    case 'N':
      return { ship, waypoint: [waypoint[0], waypoint[1] + unit] }
    case 'S':
      return { ship, waypoint: [waypoint[0], waypoint[1] - unit] }
    case 'E':
      return { ship, waypoint: [waypoint[0] + unit, waypoint[1]] }
    case 'W':
      return { ship, waypoint: [waypoint[0] - unit, waypoint[1]] }
    case 'R':
      return { ship, waypoint: rotateWaypoint(waypoint, unit) }
    case 'L':
      return { ship, waypoint: rotateWaypoint(waypoint, 0 - unit) }
  }
}

const run = async () => {
  const lines = await readLines()

  const actions = lines.map((line) => ({
    action: line.substr(0, 1),
    unit: Number(line.substr(1)),
  }))

  const position = actions.reduce(
    ({ ship, waypoint }, { action, unit }) =>
      findNextPosition(ship, waypoint, action, unit),
    { ship: [0, 0], waypoint: [10, 1] },
  )

  const answer = Math.abs(position.ship[0]) + Math.abs(position.ship[1])

  console.log(`The answer is ${answer}`)
}

run()
