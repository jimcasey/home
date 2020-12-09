const fs = require('fs')

const INPUT_PATH = `${__dirname}/input.txt`
const START_POSITION = 0
const DOWN_MOVEMENT = 1
const RIGHT_MOVEMENT = 3
const TREE_CHAR = '#'

const getLines = async () => {
  const file = await fs.readFileSync(INPUT_PATH, 'utf8')
  const lines = file.split('\n')
  return lines.filter((line) => !!line)
}

const run = async () => {
  const lines = await getLines()

  let position = START_POSITION
  let count = 0

  for (let index = 0; index < lines.length; index += DOWN_MOVEMENT) {
    const line = lines[index]
    checkIndex = position % line.length
    if (line.charAt(checkIndex) === TREE_CHAR) count++
    position += RIGHT_MOVEMENT
  }

  console.log(`Encountered ${count} trees.`)
}

run()
