const fs = require('fs')

const TESTING = false // 694173
const INPUT_PATH = `${__dirname}/${TESTING ? 'test' : 'input'}.txt`

const split = (str, separator = '\n') => str.split(separator).filter((s) => !!s)

const readInput = async () => {
  const file = await fs.readFileSync(INPUT_PATH, 'utf8')
  return split(file)
}

const parseExpr = (expr) => {
  const ops = []
  let parenCount = 0
  let parenStart
  for (let index = 0; index < expr.length; index++) {
    const char = expr[index]

    if (char === '(') {
      if (parenCount === 0) parenStart = index + 1
      parenCount++
    }

    if (parenCount === 0) {
      const num = Number(char)
      ops.push(isNaN(num) ? char : num)
    }

    if (char === ')') {
      parenCount--
      if (parenCount === 0) {
        ops.push(parseExpr(expr.substring(parenStart, index)))
        parenStart = undefined
      }
    }
  }
  return ops
}

const evaluateExpr = (ops) => {
  const evalOps = []

  for (let index = 0; index < ops.length; index++) {
    const op = ops[index]
    if (op === '+') {
      index++
      evalOps[evalOps.length - 1] += evaluateOp(ops[index])
    } else {
      evalOps.push(evaluateOp(op))
    }
  }

  let answer = evalOps[0]
  for (let index = 1; index < evalOps.length; index += 2) {
    answer *= evalOps[index + 1]
  }

  return answer
}

const evaluateOp = (op) => (Array.isArray(op) ? evaluateExpr(op) : op)

const run = async () => {
  const input = await readInput()
  const exprs = input.map((expr) => expr.replaceAll(' ', ''))

  const answer = exprs.reduce(
    (n, expr) => (n += evaluateExpr(parseExpr(expr))),
    0,
  )
  console.log(`The sum of all evaluated expressions is ${answer}.`)
}

run()

const EXEC_TIME = {}
const execTime = (key, fn) => {
  const startMs = Date.now()
  const result = fn()
  if (!EXEC_TIME[key]) EXEC_TIME[key] = 0
  EXEC_TIME[key] += Date.now() - startMs
  return result
}
