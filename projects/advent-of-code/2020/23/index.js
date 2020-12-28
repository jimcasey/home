const TESTING = !!process.env.TEST // 934001 * 159792 = 149245887792

const MIN_CUP = 1
const MAX_CUP = 1000000
const ITERATIONS = 10000000

const run = async () => {
  let input = TESTING ? '389125467' : '157623984'

  const cups = input.split('').map(Number)
  for (let cup = 10; cup <= MAX_CUP; cup++) cups.push(cup)

  const cupPositions = {}
  const positions = {}

  const setNextPosition = (index, next) => {
    positions[index] = next
    cupPositions[cups[index]] = index
  }
  const getNextPosition = (index) => positions[index]
  const getCupPosition = (cup) => cupPositions[cup]

  cups.forEach((cup, index) => {
    const next = index + 1
    setNextPosition(index, next === cups.length ? 0 : next)
  })

  let currentIndex = 0
  for (let n = 0; n < ITERATIONS; n++) {
    const sliceStart = getNextPosition(currentIndex)
    let sliceEnd = sliceStart
    for (let d = 0; d < 2; d++) sliceEnd = getNextPosition(sliceEnd)
    setNextPosition(currentIndex, getNextPosition(sliceEnd))
    setNextPosition(sliceEnd, undefined)

    const sliceCups = []
    for (let i = sliceStart; i !== undefined; i = getNextPosition(i))
      sliceCups.push(cups[i])

    let findCup = deiterateCup(cups[currentIndex])
    while (sliceCups.includes(findCup)) findCup = deiterateCup(findCup)

    const destinationIndex = getCupPosition(findCup)

    setNextPosition(sliceEnd, getNextPosition(destinationIndex))
    setNextPosition(destinationIndex, sliceStart)

    currentIndex = getNextPosition(currentIndex)
  }

  let nextIndex = getNextPosition(getCupPosition(1))
  const answer = cups[nextIndex] * cups[getNextPosition(nextIndex)]

  console.log(`The answer is ${answer}.`)
}

const deiterateCup = (cup) => (--cup < MIN_CUP ? MAX_CUP : cup)

run()
