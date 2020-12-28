const fs = require('fs')

const INPUT_PATH = `${__dirname}/input.txt`
const TEST_PATH = `${__dirname}/test1.txt`

const readInput = async () => {
  const file = await fs.readFileSync(INPUT_PATH, 'utf8')
  const sections = split(file, '\n\n')
  return {
    fields: split(sections[0]),
    myTicket: split(sections[1])[1],
    tickets: split(sections[2]).filter((_, index) => index !== 0),
  }
}

const split = (str, separator = '\n') => str.split(separator).filter((s) => !!s)

const parseFields = (fields) =>
  fields.map((field) => {
    const matches = field.match(
      /^([a-z ]+): ([0-9]+)-([0-9]+) or ([0-9]+)-([0-9]+)$/,
    )
    return {
      name: matches[1],
      ranges: [
        { min: Number(matches[2]), max: Number(matches[3]) },
        { min: Number(matches[4]), max: Number(matches[5]) },
      ],
    }
  })

const parseTicket = (ticket) => ticket.split(',').map(Number)

const isValid = (validRanges, value) => {
  for (let range of validRanges) {
    if (range.min <= value && value <= range.max) return true
  }
  return false
}

const run = async () => {
  const input = await readInput()
  const fields = parseFields(input.fields)
  const myTicket = parseTicket(input.myTicket)
  const tickets = input.tickets.map(parseTicket)

  const validRanges = fields.reduce(
    (ranges, field) => [...ranges, ...field.ranges],
    [],
  )

  const invalidValues = tickets.reduce((arr, ticket) => {
    ticket.forEach((value) => {
      if (!isValid(validRanges, value)) arr.push(value)
    })
    return arr
  }, [])

  const answer = invalidValues.reduce((sum, value) => sum + value, 0)

  console.log(`The answer is ${answer}.`)
}

run()
