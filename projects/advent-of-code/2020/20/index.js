const fs = require('fs')
const util = require('util')

const TESTING = !!process.env.TEST // 20899048083289
const INPUT_PATH = `${__dirname}/${TESTING ? 'test' : 'input'}.txt`

const split = (str, separator = '\n') => str.split(separator).filter((s) => !!s)
const log = (obj) => console.log(util.inspect(obj, false, null, true))

const EMPTY_ARRAY = new Array(4).fill(undefined)

const readInput = async () => {
  const file = await fs.readFileSync(INPUT_PATH, 'utf8')
  return split(file, '\n\n')
}

const parseTile = (input) => {
  const [_, id, data] = input.match(/^Tile ([0-9]+):\n([\.#\n]*$)/)
  const tile = split(data).map((row) => row.split(''))

  const map = []
  for (let rowIndex = 1; rowIndex < 9; rowIndex++) {
    const row = []
    for (let colIndex = 1; colIndex < 9; colIndex++) {
      row.push(tile[rowIndex][colIndex])
    }
    map.push(row)
  }

  return {
    id: Number(id),
    matrix: split(data).map((row) => row.split('')),
    neighbors: [...EMPTY_ARRAY],
  }
}

const getEdge = (tile, position) => {
  switch (position) {
    case 0:
      return tile.matrix[0].join('')
    case 1:
      return tile.matrix.map((row) => row[9]).join('')
    case 2:
      return tile.matrix[9].join('')
    case 3:
      return tile.matrix.map((row) => row[0]).join('')
  }
}

const reverse = (str) => str.split('').reverse().join('')

const findNewNeighbors = (tiles, tile) =>
  tile.neighbors.reduce((newNeighbors, neighbor, position) => {
    if (!neighbor) {
      const edge = getEdge(tile, position)
      const edgeReverse = reverse(edge)

      for (let indexP = 0; indexP < tiles.length; indexP++) {
        const tileP = tiles[indexP]
        if (tile.id === tileP.id) continue

        for (
          let positionP = 0;
          positionP < tileP.neighbors.length;
          positionP++
        ) {
          const neighborP = tileP.neighbors[positionP]
          if (neighborP) continue

          const edgeP = getEdge(tileP, positionP)
          if (edge === edgeP || edgeReverse === edgeP) {
            newNeighbors.push({
              position,
              neighborID: tileP.id,
              neighborPosition: positionP,
            })
            break
          }
        }
      }
    }

    return newNeighbors
  }, [])

const getRightTiles = (tileMap, tile) => {
  let currentTile = tile
  const arr = []
  while (currentTile) {
    arr.push(currentTile)
    currentTile = getRightTile(tileMap, currentTile)
  }
  return arr
}

const getRightTile = (tileMap, tile) => {
  const rightID = tile.neighbors[1]
  if (!rightID) return

  let rightTile = tileMap[rightID]

  const leftPosition = rightTile.neighbors.indexOf(tile.id)
  if (leftPosition !== 3) {
    const turns = 3 - leftPosition
    rightTile = {
      id: rightTile.id,
      matrix: rotateMatrix(rightTile.matrix, turns),
      neighbors: rotateArray(rightTile.neighbors, turns),
    }
  }

  if (getEdge(tile, 1) !== getEdge(rightTile, 3)) {
    rightTile = {
      id: rightTile.id,
      matrix: [...rightTile.matrix].reverse(),
      neighbors: [2, 1, 0, 3].map((index) => rightTile.neighbors[index]),
    }
  }

  return rightTile
}

const getStartTiles = (tileMap, tile) => {
  let currentTile = tile
  const arr = []
  while (currentTile) {
    arr.push(currentTile)
    currentTile = getBottomTile(tileMap, currentTile)
  }
  return arr
}

const getBottomTile = (tileMap, tile) => {
  const bottomID = tile.neighbors[2]
  if (!bottomID) return

  let bottomTile = tileMap[bottomID]

  const topPosition = bottomTile.neighbors.indexOf(tile.id)
  if (topPosition !== 0) {
    const turns = 0 - topPosition
    bottomTile = {
      id: bottomTile.id,
      matrix: rotateMatrix(bottomTile.matrix, turns),
      neighbors: rotateArray(bottomTile.neighbors, turns),
    }
  }

  if (getEdge(tile, 2) !== getEdge(bottomTile, 0)) {
    bottomTile = {
      id: bottomTile.id,
      matrix: matrix.map((row) => [...row].reverse()),
      neighbors: [0, 3, 2, 1].map((index) => bottomTile.neighbors[index]),
    }
  }

  return bottomTile
}

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

const rotateArray = (array, turns) => {
  return array.reduce(
    (newArray, item, index) => {
      newArray[(index + turns + 4) % 4] = item
      return newArray
    },
    [...EMPTY_ARRAY],
  )
}

const SEA_MONSTER = [
  '..................#.',
  '#....##....##....###',
  '.#..#..#..#..#..#...',
]

const matchesSeaMonster = (matrix, start) =>
  [0, 1, 2].reduce(
    (matches, index) =>
      matches &&
      new RegExp(SEA_MONSTER[index]).test(matrix[start + index].join('')),
    true,
  )

const countSeaMonsters = (matrix) => {
  let count = 0
  for (let index = 0; index < matrix.length - 2; index++) {
    if (matchesSeaMonster(matrix, index)) count++
  }
  return count
}

const run = async () => {
  const input = await readInput()
  const tiles = input.map(parseTile)
  const tileMap = tiles.reduce((obj, tile) => ({ ...obj, [tile.id]: tile }), {})

  tiles.forEach((tile) => {
    findNewNeighbors(tiles, tile).forEach(
      ({ position, neighborID, neighborPosition }) => {
        tile.neighbors[position] = neighborID
        tileMap[neighborID].neighbors[neighborPosition] = tile.id
      },
    )
  })

  const topLeftTile = tiles.find(
    ({ neighbors }) => !neighbors[0] && !neighbors[3],
  )
  const tileMatrix = getStartTiles(tileMap, topLeftTile).map((startTile) =>
    getRightTiles(tileMap, startTile),
  )

  let matrix = tileMatrix.reduce((m, row) => {
    row.forEach((tile, rowIndex) => {
      tile.matrix.slice(1, 9).forEach((cells, cellsIndex) => {
        const items = cells.slice(1, 9)
        if (rowIndex === 0) m.push([...items])
        else m[m.length - 8 + cellsIndex].push(...items)
      })
    })
    return m
  }, [])

  matrix.forEach((row) => console.log(row.join('')))

  let count = 0
  for (let index = 0; index < 12; index++) {
    count = countSeaMonsters(matrix)
    if (count) break
    matrix = rotateMatrix(matrix, 1)

    if (index === 4 || index === 7) {
      matrix = matrix.map((row) => [...row].reverse())
    }
  }

  console.log(count)
}

const TEST_MATRIX = [
  '.####...#####..#...###..',
  '#####..#..#.#.####..#.#.',
  '.#.#...#.###...#.##.##..',
  '#.#.##.###.#.##.##.#####',
  '..##.###.####..#.####.##',
  '...#.#..##.##...#..#..##',
  '#.##.#..#.#..#..##.#.#..',
  '.###.##.....#...###.#...',
  '#.####.#.#....##.#..#.#.',
  '##...#..#....#..#...####',
  '..#.##...###..#.#####..#',
  '....#.##.#.#####....#...',
  '..##.##.###.....#.##..#.',
  '#...#...###..####....##.',
  '.#.##...#.##.#.#.###...#',
  '#.###.#..####...##..#...',
  '#.###...#.##...#.######.',
  '.###.###.#######..#####.',
  '..##.#..#..#.#######.###',
  '#.#..##.########..#..##.',
  '#.#####..#.#...##..#....',
  '#....##..#.#########..##',
  '#...#.....#..##...###.##',
  '#..###....##.#...##.##.#',
].map((row) => row.split(''))

console.log(countSeaMonsters(TEST_MATRIX))

run()
