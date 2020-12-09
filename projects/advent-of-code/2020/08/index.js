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

const execute = (commands) => {
  let index = 0
  let accumulator = 0
  let success = false
  let executed = new Set()

  while (!executed.has(index) && !success) {
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

    success = index >= commands.length
  }

  return { accumulator, success }
}

const run = async () => {
  const lines = await readLines()
  const commands = parseLines(lines)

  const toTest = commands.reduce((indexes, { op }, index) => {
    if (op !== 'acc') indexes.push(index)
    return indexes
  }, [])

  for (let index = 0; index < toTest.length; index++) {
    const testCommands = [...commands]
    switchOp = testCommands[toTest[index]]
    testCommands[toTest[index]] = {
      ...switchOp,
      op: switchOp.op === 'jmp' ? 'nop' : 'jmp',
    }

    const { accumulator, success } = execute(testCommands)
    if (success) {
      console.log(`Program was successful when accumulator is ${accumulator}.`)
      return
    }
  }
}

run()
