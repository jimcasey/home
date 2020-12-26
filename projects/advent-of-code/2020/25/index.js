const fs = require('fs')
const util = require('util')

const TESTING = !!process.env.TEST // 14897079
const INPUT_PATH = `${__dirname}/${TESTING ? 'test' : 'input'}.txt`

const split = (str, separator = '\n') => str.split(separator).filter((s) => !!s)
const log = (obj) => console.log(util.inspect(obj, false, null, true))

const readInput = async () => {
  const file = await fs.readFileSync(INPUT_PATH, 'utf8')
  return split(file)
}

const SUBJECT_NUMBER = 7
const DIVIDER = 20201227

const run = async () => {
  const input = await readInput()
  const [cardPK, doorPK] = input.map(Number)

  const cardEncryptionKey = transform(doorPK, findLoopSize(cardPK))
  const doorEncryptionKey = transform(cardPK, findLoopSize(doorPK))

  if (cardEncryptionKey !== doorEncryptionKey)
    console.log(
      `Card (${cardEncryptionKey}) and door (${doorEncryptionKey}) do not match.`,
    )
  else console.log(`Encryption key is: ${cardEncryptionKey}`)
}

const findLoopSize = (pk) => {
  let testPK = 1
  for (let loopSize = 1; ; loopSize++) {
    testPK = (testPK * SUBJECT_NUMBER) % DIVIDER
    if (testPK === pk) return loopSize
  }
}

const transform = (subjectNumber, loopSize) => {
  let pk = 1
  for (let n = 0; n < loopSize; n++) pk = (pk * subjectNumber) % DIVIDER
  return pk
}

run()
