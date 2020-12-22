const fs = require('fs')
const util = require('util')

const TESTING = !!process.env.TEST // 20899048083289
const INPUT_PATH = `${__dirname}/${TESTING ? 'test' : 'input'}.txt`

const split = (str, separator = '\n') => str.split(separator).filter((s) => !!s)
const log = (obj) => console.log(util.inspect(obj, false, null, true))

const DIRECTIONS = ['n', 'e', 's', 'w']

const SEA_MONSTER = [
  '..................#.',
  '#....##....##....###',
  '.#..#..#..#..#..#...',
]

const readInput = async () => {
  const file = await fs.readFileSync(INPUT_PATH, 'utf8')
  return split(file, '\n\n')
}

const parseTile = (input) => {
  const [_, data] = input.match(/^Tile [0-9]+:\n([\.#\n]*$)/)
  return split(data).map((row) => row.split(''))
}

const removeTile = (tiles, tile) => tiles.filter((t) => tile !== t)

const findNeighbor = (tiles, tile, direction) => {
  const edge = getEdge(tile, direction)
  const edgeReverse = edge.split('').reverse().join('')

  let neighborEdge
  let neighborDirection
  const neighbor = tiles.find((n) => {
    return DIRECTIONS.reduce((isMatch, d) => {
      const e = getEdge(n, d)
      if (e === edge || e === edgeReverse) {
        neighborEdge = e
        neighborDirection = d
        return true
      }
      return isMatch
    }, false)
  })

  let matrix
  if (neighbor) {
    matrix = neighbor

    const properDirection = getNeighborDirection(direction)
    const turns = getTurns(neighborDirection, properDirection)
    if (turns !== 0) {
      matrix = rotateMatrix(matrix, turns)
    }

    if (getEdge(matrix, properDirection) === edgeReverse) {
      matrix = flipMatrix(matrix, properDirection)
    }
  }

  return { neighbor, matrix }
}

const getNeighborDirection = (direction) =>
  DIRECTIONS[(DIRECTIONS.indexOf(direction) + 2) % 4]

const logMatrix = (matrix) => {
  if (!matrix) {
    console.log('matrix is undefined')
    return
  }

  const border = ` ${'-'.repeat(matrix[0].length + 2)} `
  console.log(border)
  matrix.forEach((row) => console.log(`| ${row.join('')} |`))
  console.log(border)
}

const getEdge = (tile, direction) => {
  if (direction.match(/[ns]/)) {
    return tile[direction === 's' ? 9 : 0].join('')
  }
  if (direction.match(/[ew]/)) {
    return tile.map((row) => row[direction === 'e' ? 9 : 0]).join('')
  }
}

const flipMatrix = (matrix, direction) => {
  if (direction.match(/[ns]/)) {
    return matrix.map((row) => [...row].reverse())
  }
  if (direction.match(/[ew]/)) {
    return [...matrix].reverse()
  }
}

const getTurns = (direction, properDirection) =>
  DIRECTIONS.indexOf(properDirection) - DIRECTIONS.indexOf(direction)

const rotateMatrix = (matrix, turns) => {
  let newMatrix = matrix
  for (let index = 0; index < (turns + 4) % 4; index++) {
    const lastIndex = matrix.length - 1
    newMatrix = newMatrix.map((row, rowIndex) =>
      row.map((_, colIndex) => newMatrix[lastIndex - colIndex][rowIndex]),
    )
  }
  return newMatrix
}

const createMatrix = (tileMatrix) =>
  tileMatrix.reduce((matrix, row) => {
    row.forEach((tile, rowIndex) => {
      const start = 1
      const length = 8
      const end = start + length
      tile.slice(start, end).forEach((cells, cellsIndex) => {
        const items = cells.slice(start, end)
        if (rowIndex === 0) matrix.push([...items])
        else matrix[matrix.length - length + cellsIndex].push(...items)
      })
    })
    return matrix
  }, [])

const findSeaMonsters = (tileMatrix) => {
  let matrix = createMatrix(tileMatrix)

  const flipDirections = ['n', 'e']
  for (let flipIndex = 0; flipIndex < 3; flipIndex++) {
    for (let rotateIndex = 0; rotateIndex < 4; rotateIndex++) {
      const count = countSeaMonsters(matrix)
      if (count) return { count, finalMatrix: matrix }
      matrix = rotateMatrix(matrix, 1)
    }

    if (flipIndex < 2) {
      matrix = flipMatrix(matrix, flipDirections[flipIndex])
    }
  }

  return { count: 0, finalMatrix: matrix }
}

const countSeaMonsters = (matrix) => {
  const str = matrix.map((row) => row.join('')).join('')

  const re = new RegExp(
    SEA_MONSTER.join(`.{${matrix.length - SEA_MONSTER[0].length}}`),
  )

  let match
  let count = 0
  let testStr = str

  while ((match = testStr.match(re)) !== null) {
    console.log(`Found match at ${match.index}.`)
    count++
    testStr = testStr.substring(match.index + 1)
  }

  return count
}

const countHashes = (matrix) =>
  matrix.reduce((count, row) => {
    const arr = Array.isArray(row) ? row : row.split('')
    return count + arr.filter((str) => str === '#').length
  }, 0)

const run = async () => {
  const input = await readInput()
  let tiles = input.map(parseTile)

  let tile
  const tileMatrix = []
  const seed = tiles[0]
  tileMatrix.push([seed])
  tiles = removeTile(tiles, seed)

  // find north until none are found
  tile = seed
  while (tile) {
    const { neighbor, matrix } = findNeighbor(tiles, tile, 'n')
    tile = matrix
    if (matrix) tileMatrix.unshift([matrix])
    if (neighbor) tiles = removeTile(tiles, neighbor)
  }

  // find south until none are found
  tile = seed
  while (tile) {
    const { neighbor, matrix } = findNeighbor(tiles, tile, 's')
    tile = matrix
    if (matrix) tileMatrix.push([matrix])
    if (neighbor) tiles = removeTile(tiles, neighbor)
  }

  // find west for each row until none is found
  tileMatrix.forEach((row) => {
    tile = row[0]
    while (tile) {
      const { neighbor, matrix } = findNeighbor(tiles, tile, 'w')
      tile = matrix
      if (matrix) row.unshift(matrix)
      if (neighbor) tiles = removeTile(tiles, neighbor)
    }
  })

  // find east for each row until none is found
  tileMatrix.forEach((row) => {
    tile = row[row.length - 1]
    while (tile) {
      const { neighbor, matrix } = findNeighbor(tiles, tile, 'e')
      tile = matrix
      if (matrix) row.push(matrix)
      if (neighbor) tiles = removeTile(tiles, neighbor)
    }
  })

  // find sea monsters
  const { count, finalMatrix } = findSeaMonsters(tileMatrix)

  if (!count) {
    console.log('Could not find any sea monsters.')
  } else {
    logMatrix(finalMatrix)

    hashCount = countHashes(finalMatrix) - countHashes(SEA_MONSTER) * count
    console.log(
      `Found ${count} sea monsters, leaving a total of ${hashCount} uncovered hashes.`,
    )
  }
}

run()
