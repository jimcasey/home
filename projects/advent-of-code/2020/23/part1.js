const TESTING = !!process.env.TEST // 67384529

const MIN_CUP = 1
const MAX_CUP = 9
const ITERATIONS = 100

const run = async () => {
  let input = TESTING ? '389125467' : '157623984'

  const cups = input.split('').map(Number)
  const positions = cups.reduce((list, _, index) => {
    const next = index + 1
    list[index] = next === cups.length ? 0 : next
    return list
  }, {})

  let currentIndex = 0
  for (let n = 0; n < ITERATIONS; n++) {
    const sliceStart = positions[currentIndex]
    let sliceEnd = sliceStart
    for (let d = 0; d < 2; d++) sliceEnd = positions[sliceEnd]
    positions[currentIndex] = positions[sliceEnd]
    positions[sliceEnd] = undefined

    const sliceCups = []
    for (let i = sliceStart; i !== undefined; i = positions[i])
      sliceCups.push(cups[i])

    let searchCup = deiterateCup(cups[currentIndex])
    while (sliceCups.includes(searchCup)) searchCup = deiterateCup(searchCup)

    let destinationIndex = currentIndex
    while (cups[destinationIndex] !== searchCup)
      destinationIndex = positions[destinationIndex]

    positions[sliceEnd] = positions[destinationIndex]
    positions[destinationIndex] = sliceStart

    currentIndex = positions[currentIndex]
  }

  let answer = ''
  for (
    let index = positions[currentIndex];
    index !== currentIndex;
    index = positions[index]
  )
    answer += `${cups[index]}`
  console.log(`The answer is ${answer}.`)
}

const deiterateCup = (cup) => (--cup < MIN_CUP ? MAX_CUP : cup)

run()
