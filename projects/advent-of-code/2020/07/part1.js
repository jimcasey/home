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

const getPossibleContainers = (containers, bag) => {
  const possibleContainers = Object.entries(containers).reduce(
    (arr, [key, value]) => {
      if (!!value.find((item) => item.bag === bag)) {
        arr.push(key)
        arr.push(...getPossibleContainers(containers, key))
      }
      return arr
    },
    [],
  )
  return Array.from(new Set(possibleContainers).values())
}

const run = async () => {
  const bag = 'shiny gold'

  const lines = await readLines()
  const containers = mapContainers(lines)
  const possibleContainers = getPossibleContainers(containers, bag)

  console.log(`${possibleContainers.length} bags can contain '${bag}'.`)
}

run()
