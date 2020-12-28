const fs = require('fs')

const TESTING = false // 26457
const INPUT_PATH = `${__dirname}/${TESTING ? 'test' : 'input'}.txt`

const split = (str, separator = '\n') => str.split(separator).filter((s) => !!s)

const readInput = async () => {
  const file = await fs.readFileSync(INPUT_PATH, 'utf8')
  return split(file)
}

const OPER_ADD = '+'
const OPER_MULTIPLY = '*'

const parseExpr = (expr) => {
  const ops = []
  for (let index = 0; index < expr.length; index++) {
    const char = expr[index]
    const oper = expr[index - 1]

    let value
    if (Number(char) !== NaN) value = Number(char)
    if (char === '(') {
      const { subOps, offset } = parseSubExpr(expr, index)
      index += offset
      value = subOps
    }

    index++
    ops.push({
      value,
      oper,
    })
  }
  return ops
}

const parseSubExpr = (expr, index) => {
  let parenCount = 0
  const subExpr = expr
    .substr(index + 1)
    .split('')
    .reduce((e, c) => {
      if (parenCount < 0) return e
      switch (c) {
        case '(':
          parenCount++
          break
        case ')':
          parenCount--
          break
      }
      if (parenCount < 0) return e
      return e + c
    }, '')

  return {
    subOps: parseExpr(subExpr),
    offset: subExpr.length + 1,
  }
}

const evaluateExpr = (expr) => {
  const ops = Array.isArray(expr) ? expr : parseExpr(expr)
  return ops.reduce((n, { oper, value }) => {
    const v = Array.isArray(value) ? evaluateExpr(value) : value
    switch (oper) {
      case OPER_MULTIPLY:
        return n * v
      case OPER_ADD:
      default:
        return n + v
    }
  }, 0)
}

const run = async () => {
  const input = await readInput()
  const exprs = input.map((expr) => expr.replaceAll(' ', ''))

  const answer = exprs.reduce((sum, expr) => sum + evaluateExpr(expr), 0)

  console.log(`The sum of all expressions is ${answer}`)
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
