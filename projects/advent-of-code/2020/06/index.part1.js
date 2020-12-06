const fs = require('fs')

const INPUT_PATH = `${__dirname}/input.txt`

const readGroups = async () => {
  const file = await fs.readFileSync(INPUT_PATH, 'utf8')
  return file.split('\n\n').filter((group) => !!group)
}

const run = async () => {
  const groups = await readGroups()
  let count = 0
  groups.forEach((group) => {
    const forms = group.split('\n')
    const uniqueAnswers = new Set()
    forms.forEach((form) => {
      for (const answer of form) uniqueAnswers.add(answer)
    })
    count += uniqueAnswers.size
  })

  console.log(`Sum of unique answers is ${count}`)
}

run()
