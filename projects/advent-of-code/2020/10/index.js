const fs = require('fs')

const INPUT_PATH = `${__dirname}/input.txt`

const readLines = async () => {
  const file = await fs.readFileSync(INPUT_PATH, 'utf8')
  return file.split('\n').filter((line) => !!line)
}

// confession: had to look up a few hints to figure out this one
const TRIBONACCI_SEQUENCE = [1, 1, 2, 4, 7, 13, 24, 44, 81, 149]

const run = async () => {
  const lines = await readLines()
  const sequence = lines.map(Number).sort((a, b) => a - b)
  const joltages = [0, ...sequence, sequence[sequence.length - 1] + 3]

  let singleDiffCount = 0
  const answer = joltages.reduce((multiplier, joltage) => {
    if (sequence.includes(joltage + 1)) singleDiffCount++
    else {
      multiplier *= TRIBONACCI_SEQUENCE[singleDiffCount]
      singleDiffCount = 0
    }
    return multiplier
  }, 1)

  console.log(`The answer is ${answer}.`)
}

run()
