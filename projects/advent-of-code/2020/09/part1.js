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

const run = async () => {
  const lines = await readLines()
  const numbers = lines.map(Number)
  const invalidNumber = findInvalidNumber(numbers)

  console.log(`The first invalid number is ${invalidNumber}.`)
}

run()
