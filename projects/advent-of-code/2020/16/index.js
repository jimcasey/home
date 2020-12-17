const fs = require('fs')

const INPUT_PATH = `${__dirname}/input.txt`
const TEST_PATH = `${__dirname}/test2.txt`

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
  fields.reduce((map, field) => {
    const matches = field.match(
      /^([a-z ]+): ([0-9]+)-([0-9]+) or ([0-9]+)-([0-9]+)$/,
    )
    map.set(matches[1], [
      { min: Number(matches[2]), max: Number(matches[3]) },
      { min: Number(matches[4]), max: Number(matches[5]) },
    ])
    return map
  }, new Map())

const parseTicket = (ticket) => ticket.split(',').map(Number)

const isValueValid = (ranges, value) => {
  for (let range of ranges) {
    if (range.min <= value && value <= range.max) return true
  }
  return false
}

const isTicketValid = (fields, ticket) => {
  const validRanges = []
  fields.forEach((ranges) => validRanges.push(...ranges))

  for (let value of ticket) {
    if (!isValueValid(validRanges, value)) return false
  }
  return true
}

const run = async () => {
  const input = await readInput()
  const fields = parseFields(input.fields)
  const fieldNames = Array.from(fields.keys())
  const myTicket = parseTicket(input.myTicket)
  const tickets = input.tickets
    .map(parseTicket)
    .filter((ticket) => isTicketValid(fields, ticket))

  const foundPositions = new Map()
  const possiblePositions = new Map()
  const defaultIndexes = myTicket.reduce((arr, _, index) => [...arr, index], [])
  fieldNames.forEach((fieldName) =>
    possiblePositions.set(fieldName, new Set(defaultIndexes)),
  )

  while (foundPositions.size < myTicket.length) {
    possiblePositions.forEach((possibleIndexes, fieldName) => {
      const ranges = fields.get(fieldName)
      possibleIndexes.forEach((index) => {
        if (foundPositions.has(index)) {
          possibleIndexes.delete(index)
        }
        tickets.forEach((ticket) => {
          if (!isValueValid(ranges, ticket[index])) {
            possibleIndexes.delete(index)
            return
          }
        })
      })
      if (possibleIndexes.size === 1) {
        const index = Array.from(possibleIndexes.values())[0]
        foundPositions.set(index, fieldName)
        possiblePositions.delete(fieldName)
      }
    })
  }

  let answer
  console.log('[Ticket]')
  myTicket.forEach((value, index) => {
    const fieldName = foundPositions.get(index)
    if (fieldName.startsWith('departure'))
      answer = !answer ? value : answer * value
    console.log(fieldName.padEnd(20), value)
  })

  console.log(`The answer is ${answer}.`)
}

run()
