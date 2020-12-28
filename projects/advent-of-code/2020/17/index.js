const fs = require('fs')

const TESTING = false
const INPUT_PATH = `${__dirname}/${TESTING ? 'test' : 'input'}.txt`

const split = (str, separator = '\n') => str.split(separator).filter((s) => !!s)

const readInput = async () => {
  const file = await fs.readFileSync(INPUT_PATH, 'utf8')
  return split(file)
}

const createID = (x, y, z, w) => `${x},${y},${z},${w}`
const parseID = (id) => id.split(',').map(Number)

const parseInput = (input) =>
  input.reduce((cubes, line, x) => {
    line
      .split('')
      .forEach((state, y) => cubes.set(createID(x, y, 0, 0), state === '#'))
    return cubes
  }, new Map())

const OFFSETS = [-1, 0, 1]
const getAdjacentIDs = (id) => {
  const [x, y, z, w] = parseID(id)
  const ids = []
  OFFSETS.forEach((xo) =>
    OFFSETS.forEach((yo) =>
      OFFSETS.forEach((zo) =>
        OFFSETS.forEach((wo) => {
          if (xo === 0 && yo === 0 && zo === 0 && wo === 0) return
          ids.push(createID(x + xo, y + yo, z + zo, w + wo))
        }),
      ),
    ),
  )
  return ids
}

const run = async () => {
  const input = await readInput()
  let cubes = parseInput(input)

  for (let cycle = 0; cycle < 6; cycle++) {
    // add empty cubes around active ones

    cubes.forEach((active, id) => {
      if (!active) return
      getAdjacentIDs(id).forEach((adjacentID) => {
        if (!cubes.has(adjacentID)) {
          cubes.set(adjacentID, false)
        }
      })
    })

    // find cubes to update
    const updates = []

    cubes.forEach((active, id) => {
      activeCount = getAdjacentIDs(id).reduce(
        (count, id) => count + (cubes.get(id) ? 1 : 0),
        0,
      )

      if (active && (activeCount < 2 || 3 < activeCount))
        updates.push({ id, active: false })
      if (!active && activeCount === 3) updates.push({ id, active: true })
    })

    // update states
    updates.forEach(({ id, active }) => cubes.set(id, active))
  }

  const answer = Array.from(cubes.values()).reduce(
    (count, active) => count + (active ? 1 : 0),
    0,
  )
  console.log(`The number of active cubes is ${answer}.`)
}

run()

const EXEC_TIME = {}
const execTime = (key, fn) => {
  const startMs = Date.now()
  const result = fn()
  if (!EXEC_TIME[key]) EXEC_TIME[key] = 0
  EXEC_TIME[key] += Date.now() - startMs
  return result
}
