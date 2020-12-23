const fs = require('fs')
const util = require('util')

const TESTING = !!process.env.TEST // 306
const INPUT_PATH = `${__dirname}/${TESTING ? 'test1' : 'input'}.txt`

const split = (str, separator = '\n') => str.split(separator).filter((s) => !!s)
const log = (obj) => console.log(util.inspect(obj, false, null, true))

const readInput = async () => {
  const file = await fs.readFileSync(INPUT_PATH, 'utf8')
  return split(file, '\n\n')
}

const parseStartingHand = (input) => split(input).slice(1).map(Number)

const run = async () => {
  const input = await readInput()
  const hands = input.map(parseStartingHand)

  while (hands[0].length && hands[1].length) {
    const cards = [hands[0].shift(), hands[1].shift()]

    const index = cards[0] > cards[1] ? 0 : 1
    hands[index] = [...hands[index], cards[index], cards[(index + 1) % 2]]
  }

  const gameWinner = hands.reduce((winner, arr, index) =>
    arr.length ? index : winner,
  )

  const score = [...hands[gameWinner]]
    .reverse()
    .reduce((sum, card, index) => sum + card * (index + 1), 0)

  console.log(`Winner is Player ${gameWinner + 1} with a score of ${score}.`)
}

run()
