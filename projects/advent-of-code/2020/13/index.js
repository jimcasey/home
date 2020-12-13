const fs = require('fs')

const INPUT_PATH = `${__dirname}/input.txt`
const TEST_PATH = `${__dirname}/test.txt`

const readLines = async () => {
  const file = await fs.readFileSync(INPUT_PATH, 'utf8')
  return file.split('\n').filter((line) => !!line)
}

const lcm = (...arr) => {
  const gcd = (x, y) => (!y ? x : gcd(y, x % y))
  return [...arr].reduce((x, y) => (x * y) / gcd(x, y))
}

const findTimestamp = (input) => {
  const buses = []
  const offsets = []

  input.split(',').forEach((id, offset) => {
    if (id !== 'x') {
      buses.push(Number(id))
      offsets.push(offset)
    }
  })

  let step = buses[0]
  let timestamp = 0
  for (let index = 1; index < buses.length; index++) {
    for (let ts = timestamp; ; ts += step) {
      if ((ts + offsets[index]) % buses[index] === 0) {
        timestamp = ts
        break
      }
    }
    step = lcm(...buses.slice(0, index + 1))
  }

  return timestamp
}

const run = async () => {
  const lines = await readLines()
  let timestamp = findTimestamp(lines[1])
  console.log(`The answer is ${timestamp}.`)
}

const TESTS = [
  ['7,13,x,x,59,x,31,19', 1068781],
  ['17,x,13,19', 3417],
  ['67,7,59,61', 754018],
  ['67,x,7,59,61', 779210],
  ['67,7,x,59,61', 1261476],
  ['1789,37,47,1889', 1202161486],
]

TESTS.forEach((test) => {
  if (findTimestamp(test[0]) !== test[1]) console.error('Test failed', test)
})

run()
