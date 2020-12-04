const fs = require('fs')

const INPUT_PATH = `${__dirname}/input.txt`

const getRecords = async () => {
  const file = await fs.readFileSync(INPUT_PATH, 'utf8')
  return file
    .split('\n\n')
    .filter((record) => !!record)
    .map(parseRecord)
}

const parseRecord = (recordStr) => {
  const fields = recordStr.split(/[\s,]+/)
  const record = fields.reduce((obj, field) => {
    if (field) {
      const kv = field.split(':')
      return { ...obj, [kv[0]]: kv[1] }
    }
    return obj
  }, {})

  const validations = getValidations(record)

  return {
    ...record,
    validations: {
      ...validations,
      isValid: Object.keys(validations).reduce(
        (isValid, key) => isValid && validations[key],
        true,
      ),
    },
  }
}

const getValidations = (record) => ({
  birthYearIsValid: yearIsValid(record.byr, 1920, 2002),
  issueYearIsValid: yearIsValid(record.iyr, 2010, 2020),
  expirationYearIsValid: yearIsValid(record.eyr, 2020, 2030),
  heightIsValid: heightIsValid(record.hgt),
  hairColorIsValid: hairColorIsValid(record.hcl),
  eyeColorIsValid: eyeColorIsValid(record.ecl),
  passportIDIsValid: passportIDIsValid(record.pid),
})

const yearIsValid = (yearStr, min, max) => {
  if (!yearStr) return false
  if (yearStr.length !== 4) return false
  const year = Number(yearStr)
  return min <= year && year <= max
}

const heightIsValid = (heightStr) => {
  if (!heightStr) return false
  if (!heightStr.match(/^\d+(in|cm)$/g)) return false

  const splitIndex = heightStr.length - 2
  const height = Number(heightStr.substr(0, splitIndex))
  const unit = heightStr.substr(splitIndex)

  switch (unit) {
    case 'cm':
      return 150 <= height && height <= 193
    case 'in':
      return 59 <= height && height <= 76
  }
}

const hairColorIsValid = (hairColor) => {
  if (!hairColor) return false
  return !!hairColor.match(/^#[0-9a-f]{6}/g)
}

const eyeColorIsValid = (eyeColor) => {
  if (!eyeColor) return false
  return ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'].includes(eyeColor)
}

const passportIDIsValid = (passportID) => {
  if (!passportID) return false
  return passportID.length === 9 && !!Number(passportID)
}

const run = async () => {
  const records = await getRecords()

  const validationCounts = {}
  records.forEach((record) => {
    const { validations } = record
    Object.keys(validations).forEach((key) => {
      if (validationCounts[key] === undefined) validationCounts[key] = 0
      if (validations[key]) validationCounts[key]++
    })
  })

  console.log(validationCounts)
  console.log(`Found ${validationCounts.isValid} valid records.`)
}

run()
