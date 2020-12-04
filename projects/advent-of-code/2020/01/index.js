const fs = require('fs')

const INPUT_PATH = `${__dirname}/input.txt`
const TEST_VALUE = 2020

const getValues = async () => {
  const file = await fs.readFileSync(INPUT_PATH, 'utf8')
  return file.split('\n').reduce((values, line) => {
    if (line) return [...values, Number(line)]
    return values
  }, [])
}

const getAnswer = (values) => {
  let answer = undefined
  values.some((a, aIndex) => {
    values.some((b, bIndex) => {
      values.some((c, cIndex) => {
        if (aIndex === bIndex || aIndex === cIndex || bIndex === cIndex) {
          return
        }
        if (a + b + c === TEST_VALUE) {
          answer = { a, b, c }
          return true
        }
      })
      if (answer) return true
    })

    if (answer) return true
  })
  return answer
}

const run = async () => {
  const values = await getValues()
  const { a, b, c } = getAnswer(values)

  console.log(`${a} + ${b} + ${c} = ${a + b + c}`)
  console.log(`${a} * ${b} * ${c} = ${a * b * c}`)
}

run()
