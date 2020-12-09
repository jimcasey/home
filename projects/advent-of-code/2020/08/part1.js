const fs = require('fs')

const INPUT_PATH = `${__dirname}/input.txt`

const readLines = async () => {
  const file = await fs.readFileSync(INPUT_PATH, 'utf8')
  return file.split('\n').filter((line) => !!line)
}

const parseLines = (lines) =>
  lines.reduce((commands, line) => {
    const [op, arg] = line.split(' ')
    commands.push({ op, arg: Number(arg) })
    return commands
  }, [])

const run = async () => {
  const lines = await readLines()
  const commands = parseLines(lines)

  let index = 0
  let accumulator = 0
  let executed = new Set()

  while (!executed.has(index) && index < commands.length) {
    const { op, arg } = commands[index]
    executed.add(index)

    switch (op) {
      case 'acc':
        accumulator += arg
        index++
        break

      case 'jmp':
        index += arg
        break

      case 'nop':
        index++
        break
    }
  }

  console.log(
    `Loop encountered at index ${index}, accumulator is ${accumulator}.`,
  )
}

run()
