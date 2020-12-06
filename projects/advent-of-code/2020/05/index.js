const fs = require('fs')

const INPUT_PATH = `${__dirname}/input.txt`

const getLines = async () => {
  const file = await fs.readFileSync(INPUT_PATH, 'utf8')
  return file.split('\n').filter((line) => !!line)
}

const bisect = (line, indexStart, indexEnd, topChar, bottomChar, maxStart) => {
  let min = 0
  let max = maxStart
  for (let index = indexStart; index <= indexEnd; index++) {
    const offset = (max - min + 1) / 2
    switch (line[index]) {
      case topChar:
        min += offset
        break
      case bottomChar:
        max -= offset
        break
    }
  }
  return min
}

const parseLine = (line) => {
  return {
    row: bisect(line, 0, 6, 'B', 'F', 127),
    seat: bisect(line, 7, 9, 'R', 'L', 7),
  }
}

const run = async () => {
  const lines = await getLines()

  const rowSeatsObj = lines.reduce((seats, line) => {
    const { row, seat } = parseLine(line)
    if (!seats[row]) seats[row] = {}
    seats[row][seat] = true
    return seats
  }, {})

  const rowSeats = Object.keys(rowSeatsObj).reduce((seats, row) => {
    Object.keys(rowSeatsObj[row]).forEach((seat) => {
      seats.push({ row: Number(row), seat: Number(seat) })
    })
    return seats
  }, [])

  let { seat: previousSeat } = rowSeats[0]
  previousSeat -= 1

  let mySeat = {}
  for (const rowSeat of rowSeats) {
    const { row, seat } = rowSeat
    let testSeat = (previousSeat + 1) % 8
    if (seat !== testSeat) {
      mySeat = { row, seat: testSeat }
      break
    }
    previousSeat = seat
  }

  {
    const { row, seat } = mySeat
    const seatID = row * 8 + seat
    console.log(`My seat is row ${row}, seat ${seat}, ID ${seatID}`)
  }
}

run()
