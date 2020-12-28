const INPUT = '14,8,16,0,1,17' // 505
const TEST = '0,3,6' // 436

const ANSWER_POSITION = 30000000

const addIndex = (numMap, num, index) =>
  numMap.set(num, !numMap.has(num) ? [index] : [index, numMap.get(num)[0]])

const findAnswer = (input) => {
  const nums = input.split(',').map(Number)
  let numMap = new Map()
  let lastNum

  nums.forEach((num, index) => {
    addIndex(numMap, num, index)
    lastNum = num
  })

  for (let index = nums.length; index < ANSWER_POSITION; index++) {
    const indexes = numMap.get(lastNum) || []
    lastNum = indexes.length === 1 ? 0 : indexes[0] - indexes[1]
    addIndex(numMap, lastNum, index)
  }

  return lastNum
}

const run = async () => {
  const answer = findAnswer(INPUT)
  console.log(`The answer is ${answer}.`)
}

run()
