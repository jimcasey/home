const fs = require('fs')
const util = require('util')

const TESTING = false // 20899048083289
const INPUT_PATH = `${__dirname}/${TESTING ? 'test' : 'input'}.txt`

const split = (str, separator = '\n') => str.split(separator).filter((s) => !!s)
const log = (obj) => console.log(util.inspect(obj, false, null, true))

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
    edges: [
      tile[0].join(''),
      tile.map((row) => row[9]).join(''),
      tile[9].join(''),
      tile.map((row) => row[0]).join(''),
    ],
    map,
    neighbors: new Array(4).fill(undefined),
  }
}

const findEmptyNeighbors = ({ neighbors }) =>
  neighbors.reduce(
    (indexes, neighbor, index) =>
      neighbor === undefined ? [...indexes, index] : indexes,
    [],
  )

const nextTile = (tiles) =>
  tiles.find((tile) => findEmptyNeighbors(tile).length)

const assignNeighbors = (tiles, searchTile) => {
  searchTile.neighbors.forEach((searchNeighbor, searchIndex) => {
    if (searchNeighbor) return
    const searchEdge = searchTile.edges[searchIndex]
    const searchReverse = searchEdge.split('').reverse().join('')
    tiles.forEach((tile) => {
      if (searchTile.id === tile.id) return
      tile.neighbors.forEach((neighbor, index) => {
        if (neighbor) return
        if (
          tile.edges[index] === searchEdge ||
          tile.edges[index] === searchReverse
        ) {
          searchTile.neighbors[searchIndex] = tile.id
          tile.neighbors[index] = searchTile.id
        }
      })
    })
  })
  searchTile.neighbors = searchTile.neighbors.map((neighbor) =>
    neighbor === undefined ? null : neighbor,
  )
}

const run = async () => {
  const input = await readInput()
  const tiles = input.map(parseTile)

  let tile = nextTile(tiles)
  while (tile) {
    assignNeighbors(tiles, tile)
    tile = nextTile(tiles)
  }

  const corners = tiles.filter(
    ({ neighbors }) =>
      neighbors.filter((neighbor) => neighbor === null).length === 2,
  )

  const answer = corners.reduce(
    (product, { id }) => (!product ? id : product * id),
    undefined,
  )
  console.log(`The product of every corner ID is ${answer}.`)
}

run()
