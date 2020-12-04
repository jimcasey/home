const fs = require('fs')

const INPUT_PATH = `${__dirname}/input.txt`
const START_POSITION = 0
const TREE_CHAR = '#'

const ANGLES = [
  { right: 1, down: 1 },
  { right: 3, down: 1 },
  { right: 5, down: 1 },
  { right: 7, down: 1 },
  { right: 1, down: 2 },
]

const getLines = async () => {
  const file = await fs.readFileSync(INPUT_PATH, 'utf8')
  const lines = file.split('\n')
  return lines.filter((line) => !!line)
}

const run = async () => {
  const lines = await getLines()
  let countsMultiplied

  ANGLES.forEach((angle) => {
    const { right, down } = angle
    let position = START_POSITION
    let count = 0

    for (let index = 0; index < lines.length; index += down) {
      const line = lines[index]
      checkIndex = position % line.length
      if (line.charAt(checkIndex) === TREE_CHAR) count++
      position += right
    }

    console.log(
      `Angle (right ${right}, down ${down}) encountered ${count} trees.`,
    )

    if (!countsMultiplied) countsMultiplied = count
    else countsMultiplied *= count
  })

  console.log(`Answer: ${countsMultiplied}`)
}

run()
