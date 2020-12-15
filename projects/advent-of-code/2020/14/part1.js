const fs = require('fs')

const INPUT_PATH = `${__dirname}/input.txt`
const TEST_PATH = `${__dirname}/test2.txt`

const readLines = async () => {
  const file = await fs.readFileSync(INPUT_PATH, 'utf8')
  return file.split('\n').filter((line) => !!line)
}

const parseProgram = (lines) =>
  lines.reduce((ops, line) => {
    if (line.startsWith('mask')) {
      ops.push({
        type: 'update-mask',
        mask: line.match(/^mask = ([X01]+$)/)[1],
      })
    }

    if (line.startsWith('mem')) {
      const match = line.match(/^mem\[([0-9]+)\] = ([0-9]+$)/)
      ops.push({
        type: 'write',
        address: Number(match[1]),
        value: Number(match[2]),
      })
    }

    return ops
  }, [])

const run = async () => {
  const lines = await readLines()
  const ops = parseProgram(lines)

  let mask
  const memory = {}

  ops.forEach((op) => {
    switch (op.type) {
      case 'update-mask':
        mask = op.mask
        break

      case 'write':
        const opBin = op.value.toString(2).padStart(36, '0')

        const maskedBin = opBin
          .split('')
          .reduce(
            (bin, bit, index) =>
              bin + (mask[index] === 'X' ? bit : mask[index]),
            '',
          )
          .padStart(36, '0')

        memory[op.address] = parseInt(maskedBin, 2)
        break
    }
  })

  const answer = Object.keys(memory).reduce(
    (sum, address) => sum + memory[address],
    0,
  )

  console.log(`The answer is ${answer}.`)
}

run()
