const fs = require('fs')

const INPUT_PATH = `${__dirname}/input.txt`
const TEST_PATH = `${__dirname}/test.txt`

const readLines = async () => {
  const file = await fs.readFileSync(INPUT_PATH, 'utf8')
  return file.split('\n').filter((line) => !!line)
}

const getSeatState = (seatMap, seatIndex) => {
  const seat = seatMap[seatIndex[0]][seatIndex[1]]
  if (seat === '.') return '.'

  const adjacentSeats = getAdjacentSeats(seatMap, seatIndex)
  const occupiedCount = adjacentSeats.reduce(
    (count, adjacentSeat) => count + (adjacentSeat === '#'),
    0,
  )

  if (seat === 'L' && occupiedCount === 0) return '#'
  if (seat === '#' && occupiedCount >= 5) return 'L'

  return seat
}

const ADJACENT_VECTORS = {
  topLeft: [-1, -1],
  top: [-1, 0],
  topRight: [-1, 1],
  right: [0, 1],
  bottomRight: [1, 1],
  bottom: [1, 0],
  bottomLeft: [1, -1],
  left: [0, -1],
}

const getAdjacentSeats = (seatMap, seatIndex) =>
  Object.values(ADJACENT_VECTORS).reduce((adjacentSeats, vector) => {
    const adjacentSeat = findAdjacentSeat(seatMap, seatIndex, vector)
    if (adjacentSeat) {
      adjacentSeats.push(adjacentSeat)
    }
    return adjacentSeats
  }, [])

const findAdjacentSeat = (seatMap, seatIndex, vector, distance = 1) => {
  const testIndex = [
    seatIndex[0] + vector[0] * distance,
    seatIndex[1] + vector[1] * distance,
  ]

  const adjacentRow = seatMap[testIndex[0]]
  if (adjacentRow) {
    const adjacentSeat = adjacentRow[testIndex[1]]
    if (adjacentSeat === '.')
      return findAdjacentSeat(seatMap, seatIndex, vector, distance + 1)
    return adjacentSeat
  }
}

const run = async () => {
  let seatMap = await readLines()

  let changeCount
  while (changeCount !== 0) {
    changeCount = 0
    seatMap = seatMap.reduce((newMap, row, rowIndex) => {
      newMap.push(
        row.split('').reduce((newRow, seat, seatIndex) => {
          const newSeat = getSeatState(seatMap, [rowIndex, seatIndex])
          if (seat !== newSeat) changeCount++
          newRow += newSeat
          return newRow
        }, ''),
      )
      return newMap
    }, [])
  }

  const occupiedCount = seatMap.reduce(
    (count, row) => count + (row.match(/#/g) || []).length,
    0,
  )

  console.log(`There are ${occupiedCount} occupied seats.`)
}

run()
