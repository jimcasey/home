const fs = require('fs')

const INPUT_PATH = `${__dirname}/input.txt`
const TEST_PATH = `${__dirname}/test.txt`

const readLines = async () => {
  const file = await fs.readFileSync(INPUT_PATH, 'utf8')
  return file.split('\n').filter((line) => !!line)
}

const getSeatState = (seatMap, rowIndex, seatIndex) => {
  const seat = seatMap[rowIndex][seatIndex]
  if (seat === '.') return '.'

  const adjacentSeats = getAdjacentSeats(seatMap, rowIndex, seatIndex)
  const occupiedCount = adjacentSeats.reduce(
    (count, adjacentSeat) => count + (adjacentSeat === '#'),
    0,
  )

  if (seat === 'L' && occupiedCount === 0) return '#'
  if (seat === '#' && occupiedCount >= 4) return 'L'

  return seat
}

const ADJACENT_OFFSETS = [-1, 0, 1]
const getAdjacentSeats = (seatMap, rowIndex, seatIndex) =>
  ADJACENT_OFFSETS.reduce((adjacentSeats, rowOffset) => {
    ADJACENT_OFFSETS.forEach((seatOffset) => {
      const rowTest = rowIndex + rowOffset
      const seatTest = seatIndex + seatOffset

      if (rowTest === rowIndex && seatTest === seatIndex) return

      const adjacentRow = seatMap[rowTest]
      if (adjacentRow === undefined) return

      const adjacentSeat = adjacentRow[seatTest]
      if (adjacentSeat === undefined) return

      adjacentSeats.push(adjacentSeat)
    })
    return adjacentSeats
  }, [])

const run = async () => {
  let seatMap = await readLines()

  let changeCount
  while (changeCount !== 0) {
    changeCount = 0
    seatMap = seatMap.reduce((newMap, row, rowIndex) => {
      newMap.push(
        row.split('').reduce((newRow, seat, seatIndex) => {
          const newSeat = getSeatState(seatMap, rowIndex, seatIndex)
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
