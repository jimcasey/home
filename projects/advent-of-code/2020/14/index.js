const fs = require('fs')

const INPUT_PATH = `${__dirname}/input.txt`
const TEST_PATH = `${__dirname}/test.txt`

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

const getFloatingBits = (length) => {
  const bits = []
  for (let i = 0; ; i++) {
    const combo = i.toString(2).padStart(length, '0')

    if (combo.length > length) break
    bits.push(combo)
  }
  return bits
}

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
        const addressBin = op.address.toString(2).padStart(36, '0')
        const maskedBin = addressBin
          .split('')
          .reduce(
            (bin, bit, index) =>
              bin + (mask[index] === '0' ? bit : mask[index]),
            '',
          )
          .padStart(36, '0')

        getFloatingBits((maskedBin.match(/X/g) || []).length).forEach(
          (floatingBits) => {
            let index = 0
            const memoryAddressBin = maskedBin.split('').reduce((bin, bit) => {
              if (bit !== 'X') return bin + bit
              const floatingBit = floatingBits[index]
              index++
              return bin + floatingBit
            }, '')
            const memoryAddress = parseInt(memoryAddressBin, 2)
            memory[memoryAddress] = op.value
          },
        )

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
