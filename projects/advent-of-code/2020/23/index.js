const TESTING = !!process.env.TEST // 67384529

const run = async () => {
  let input = TESTING ? '389125467' : '157623984'
  let cups = input.split('').map(Number)

  let cup = cups[0]
  for (let index = 0; index < 100; index++) ({ cups, cup } = move(cups, cup))

  const answerIndex = findCup(cups, 1)
  const answer = [...cups.slice(answerIndex + 1), ...cups.slice(0, answerIndex)]

  console.log(`The answer is ${answer.join('')}.`)
}

const move = (cups, cup) => {
  const currentIndex = findCup(cups, cup)

  const removeIndexes = getClockwise(cups, currentIndex)
  const removed = removeIndexes.map((index) => cups[index])

  cups = cups.filter((_, index) => !removeIndexes.includes(index))

  const destinationIndex = findDestination(cups, cup)

  cups = [
    ...cups.slice(0, destinationIndex + 1),
    ...removed,
    ...cups.slice(destinationIndex + 1),
  ]
  cup = cups[(findCup(cups, cup) + 1) % cups.length]

  return { cups, cup }
}

const findCup = (cups, cup) => cups.indexOf(cup)

const getClockwise = (cups, currentCup) =>
  [1, 2, 3].map((index) => (currentCup + index) % cups.length)

const findDestination = (cups, cup) => {
  const [min, max] = cups.reduce(
    (arr, value) => [Math.min(value, arr[0]), Math.max(value, arr[1])],
    [10, 0],
  )
  let nextCup = cup - 1
  if (nextCup < min) nextCup = max

  const destination = findCup(cups, nextCup)
  return destination < 0 ? findDestination(cups, nextCup) : destination
}

run()
