const fs = require('fs')

const INPUT_PATH = `${__dirname}/input.txt`
const TEST_PATH = `${__dirname}/test.txt`

const readLines = async () => {
  const file = await fs.readFileSync(INPUT_PATH, 'utf8')
  return file.split('\n').filter((line) => !!line)
}

const run = async () => {
  const lines = await readLines()
  const start = Number(lines[0])
  const busIDs = lines[1]
    .split(',')
    .reduce((ids, id) => {
      if (id !== 'x') ids.push(Number(id))
      return ids
    }, [])
    .sort((a, b) => a - b)

  let busDeparts = Number.MAX_SAFE_INTEGER
  let busID
  busIDs.forEach((id) => {
    const departs = start - (start % id) + id
    if (departs < busDeparts) {
      busDeparts = departs
      busID = id
    }
  })

  const answer = (busDeparts - start) * busID
  console.log(`The answer is ${answer}.`)
}

run()
