const fs = require('fs')

const INPUT_PATH = `${__dirname}/input.txt`

const readLines = async () => {
  const file = await fs.readFileSync(INPUT_PATH, 'utf8')
  return file.split('\n').filter((line) => !!line)
}

const findNextAdapter = (adapters, lastAdapter) =>
  adapters
    .filter((adapter) => lastAdapter < adapter && adapter <= lastAdapter + 3)
    .reduce((min, adapter) => Math.min(min, adapter), Number.MAX_SAFE_INTEGER)

const run = async () => {
  const lines = await readLines()
  const adapters = lines.map(Number)
  deviceRating =
    adapters.reduce((max, adapter) => Math.max(max, adapter), 0) + 3
  adapters.push(deviceRating)

  let lastAdapter = 0
  const differences = { [1]: 0, [3]: 0 }
  while (lastAdapter < deviceRating) {
    const nextAdapter = findNextAdapter(adapters, lastAdapter)
    differences[nextAdapter - lastAdapter]++
    lastAdapter = nextAdapter
  }

  console.log(`The answer is ${differences[1] * differences[3]}.`)
}

run()
