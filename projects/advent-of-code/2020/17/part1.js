const fs = require('fs')

const INPUT_PATH = `${__dirname}/input.txt`
const TEST_PATH = `${__dirname}/test.txt`

const split = (str, separator = '\n') => str.split(separator).filter((s) => !!s)

const readInput = async () => {
  const file = await fs.readFileSync(INPUT_PATH, 'utf8')
  return split(file)
}

const parseInput = (input) =>
  input.reduce((cubes, line, x) => {
    line
      .split('')
      .forEach((state, y) => setActiveState(cubes, x, y, 0, state === '#'))
    return cubes
  }, {})

const getActiveState = (cubes, x, y, z) =>
  cubes[x] && cubes[x][y] && cubes[x][y][z]

const setActiveState = (cubes, x, y, z, active) => {
  if (!cubes[x]) cubes[x] = {}
  if (!cubes[x][y]) cubes[x][y] = {}
  cubes[x][y][z] = active
}

const getCoords = (cubes) =>
  Object.keys(cubes).reduce((coords, x) => {
    Object.keys(cubes[x]).forEach((y) =>
      Object.keys(cubes[x][y]).forEach((z) =>
        coords.push({
          x: Number(x),
          y: Number(y),
          z: Number(z),
          active: getActiveState(cubes, x, y, z),
        }),
      ),
    )
    return coords
  }, [])

const getAdjacentCoords = (x, y, z) => {
  const coords = []
  for (let offsetX = -1; offsetX <= 1; offsetX++) {
    for (let offsetY = -1; offsetY <= 1; offsetY++) {
      for (let offsetZ = -1; offsetZ <= 1; offsetZ++) {
        if (offsetX === 0 && offsetY === 0 && offsetZ === 0) continue
        coords.push({ x: x + offsetX, y: y + offsetY, z: z + offsetZ })
      }
    }
  }
  return coords
}

const setActiveStates = (cubes, coords) =>
  coords.forEach(({ x, y, z, active }) =>
    setActiveState(cubes, x, y, z, active),
  )

const run = async () => {
  const input = await readInput()
  let cubes = parseInput(input)

  for (let cycle = 0; cycle < 6; cycle++) {
    // add empty cubes around active ones
    getCoords(cubes).forEach(({ x, y, z, active }) => {
      if (!active) return
      getAdjacentCoords(x, y, z).forEach(({ x: x1, y: y1, z: z1 }) => {
        if (getActiveState(cubes, x1, y1, z1) === undefined)
          setActiveState(cubes, x1, y1, z1, false)
      })
    })

    // find cubes to update
    const updateCoords = []
    getCoords(cubes).forEach(({ x, y, z, active }) => {
      const adjacentActiveCount = getAdjacentCoords(x, y, z).reduce(
        (count, { x: x1, y: y1, z: z1 }) =>
          count + (getActiveState(cubes, x1, y1, z1) ? 1 : 0),
        0,
      )

      if (active && (adjacentActiveCount < 2 || 3 < adjacentActiveCount))
        updateCoords.push({ x, y, z, active: false })

      if (!active && adjacentActiveCount === 3)
        updateCoords.push({ x, y, z, active: true })
    })

    // update states
    setActiveStates(cubes, updateCoords)
  }

  const activeCount = getCoords(cubes).reduce(
    (count, { active }) => count + (active ? 1 : 0),
    0,
  )
  console.log(`The number of active cubes is ${activeCount}.`)
}

run()
