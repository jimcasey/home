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
    const commonAnswers = new Set()
    forms.forEach((form, index) => {
      if (index === 0) {
        for (const answer of form) commonAnswers.add(answer)
      } else if (form) {
        let removeAnswers = ''
        for (const answer of commonAnswers) {
          if (!form.includes(answer)) removeAnswers += answer
        }
        for (const answer of removeAnswers) commonAnswers.delete(answer)
      }
    })
    count += commonAnswers.size
  })

  console.log(`Sum of common answers is ${count}`)
}

run()
