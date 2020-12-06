const fs = require('fs')

const INPUT_PATH = `${__dirname}/input.txt`

const readLines = async () => {
  const file = await fs.readFileSync(INPUT_PATH, 'utf8')
  return file.split('\n').filter((line) => !!line)
}

const mapContainers = (lines) => {
  return lines.reduce((containers, line) => {
    const [container, items] = line
      .replace(/ bags*/g, '')
      .replace('.', '')
      .split(' contain ')

    containers[container] = []

    items.split(', ').forEach((item) => {
      if (item !== 'no other') {
        const split = item.split(' ')
        const count = Number(split.shift())
        const bag = split.join(' ')
        containers[container].push({ bag, count })
      }
    })

    return containers
  }, {})
}

const countItems = (containers, bag) => {
  let count = 0
  containers[bag].forEach((item) => {
    count += item.count + item.count * countItems(containers, item.bag)
  })

  return count
}

const run = async () => {
  const bag = 'shiny gold'

  const lines = await readLines()
  const containers = mapContainers(lines)

  const count = countItems(containers, bag)

  console.log(
    `${count} individual bags are required inside a single ${bag} bag.`,
  )
}

run()
