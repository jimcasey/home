const fs = require('fs')

const INPUT_PATH = `${__dirname}/input.txt`

const PREAMPLE_LENGTH = 25

const readLines = async () => {
  const file = await fs.readFileSync(INPUT_PATH, 'utf8')
  return file.split('\n').filter((line) => !!line)
}

const findValidNumbers = (numbers, currentIndex) => {
  const end = currentIndex
  const start = currentIndex - PREAMPLE_LENGTH
  const preampleNumbers = numbers.slice(start, end)
  return preampleNumbers.reduce((validNumbers, valueA, index) => {
    preampleNumbers
      .slice(index + 1)
      .forEach((valueB) => validNumbers.push(valueA + valueB))
    return validNumbers
  }, [])
}

const findInvalidNumber = (numbers) => {
  for (let index = PREAMPLE_LENGTH; index < numbers.length; index++) {
    const validNumbers = findValidNumbers(numbers, index)
    const number = numbers[index]

    if (!validNumbers.includes(number)) return number
  }
}

const findContiguousSum = (numbers, testNumber) => {
  for (let startIndex = 0; startIndex < numbers.length; startIndex++) {
    let sum = 0
    let min = Number.MAX_SAFE_INTEGER
    let max = Number.MIN_SAFE_INTEGER

    for (let index = startIndex; index < numbers.length; index++) {
      const number = numbers[index]
      sum += number
      min = Math.min(number, min)
      max = Math.max(number, max)
      if (sum === testNumber) return min + max
    }
  }
}

const run = async () => {
  const lines = await readLines()
  const numbers = lines.map(Number)
  const invalidNumber = findInvalidNumber(numbers)
  const answer = findContiguousSum(numbers, invalidNumber)
  console.log(`The answer is ${answer}.`)
}

run()
