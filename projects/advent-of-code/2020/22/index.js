const fs = require('fs')
const util = require('util')

const TESTING = !!process.env.TEST // 291
const INPUT_PATH = `${__dirname}/${TESTING ? 'test' : 'input'}.txt`

const split = (str, separator = '\n') => str.split(separator).filter((s) => !!s)
const log = (obj) => console.log(util.inspect(obj, false, null, true))

const readInput = async () => {
  const file = await fs.readFileSync(INPUT_PATH, 'utf8')
  return split(file, '\n\n')
}

const parseStartingHand = (input) => split(input).slice(1).map(Number)

const playGame = (startingHands) => {
  const hands = startingHands.map((hand) => [...hand])
  const previousHands = Array(2).fill([])

  while (hands[0].length && hands[1].length) {
    const hasPrevious = hands.reduce(
      (p, hand, index) => p || previousHands[index].includes(hand.join(',')),
      false,
    )

    if (!hasPrevious)
      hands.forEach((hand, index) => previousHands[index].push(hand.join(',')))

    const cards = [hands[0].shift(), hands[1].shift()]

    let roundWinner
    if (hasPrevious) {
      roundWinner = 0
    } else if (cards[0] <= hands[0].length && cards[1] <= hands[1].length) {
      const subHands = hands.map((hand, index) => hand.slice(0, cards[index]))
      roundWinner = playGame(subHands).gameWinner
    } else {
      roundWinner = cards[0] > cards[1] ? 0 : 1
    }

    hands[roundWinner] = [
      ...hands[roundWinner],
      cards[roundWinner],
      cards[(roundWinner + 1) % 2],
    ]
  }

  const gameWinner = hands.reduce(
    (winner, arr, index) => (arr.length ? index : winner),
    0,
  )

  const score = [...hands[gameWinner]]
    .reverse()
    .reduce((sum, card, index) => sum + card * (index + 1), 0)

  return { gameWinner, score }
}

const run = async () => {
  const input = await readInput()
  const hands = input.map(parseStartingHand)
  const { gameWinner, score } = playGame(hands)
  console.log(`Winner is Player ${gameWinner + 1} with a score of ${score}.`)
}

run()
