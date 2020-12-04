const fs = require('fs')

const INPUT_PATH = `${__dirname}/input.txt`

const parseLine = (line) => {
  const fields = line.split(' ')
  const bounds = fields[0].split('-')
  return {
    char: fields[1][0],
    line,
    index1: Number(bounds[1]),
    index2: Number(bounds[0]),
    password: fields[2],
  }
}

const getRecords = async () => {
  const file = await fs.readFileSync(INPUT_PATH, 'utf8')
  return file.split('\n').reduce((records, line) => {
    if (line) {
      return [...records, parseLine(line)]
    }
    return records
  }, [])
}

const isPasswordValid = (record) => {
  const { char, index1, index2, password } = record
  const char1 = password[index1 - 1]
  const char2 = password[index2 - 1]
  return (char1 === char || char2 === char) && char1 !== char2
}

const run = async () => {
  const records = await getRecords()
  const validCount = records.reduce(
    (count, record) => count + (isPasswordValid(record) ? 1 : 0),
    0,
  )

  console.log(`${validCount} valid passwords`)
}

run()
