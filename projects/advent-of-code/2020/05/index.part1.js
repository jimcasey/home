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
  const maxSeatID = lines.reduce((max, line) => {
    const { row, seat } = parseLine(line)
    const seatID = row * 8 + seat
    return Math.max(seatID, max)
  }, 0)

  console.log(`Max seat ID is ${maxSeatID}`)
}

run()
