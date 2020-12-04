const fs = require('fs')

const INPUT_PATH = `${__dirname}/input.txt`

const REQUIRED_KEYS = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']

const getRecords = async () => {
  const file = await fs.readFileSync(INPUT_PATH, 'utf8')
  return file
    .split('\n\n')
    .filter((record) => !!record)
    .map(parseRecord)
}

const parseRecord = (record) => {
  const fields = record.split(/[\s,]+/)
  return fields.reduce((record, field) => {
    if (field) {
      const kv = field.split(':')
      return { ...record, [kv[0]]: kv[1] }
    }
    return record
  }, {})
}

const run = async () => {
  const records = await getRecords()
  const validCount = records.reduce((count, record) => {
    const keys = Object.keys(record)
    if (
      REQUIRED_KEYS.reduce((isValid, requiredKey) => {
        if (!isValid) return false
        if (!keys.includes(requiredKey)) return false
        return true
      }, true)
    ) {
      count++
    }
    return count
  }, 0)

  console.log(`Found ${validCount} valid records.`)
}

run()
