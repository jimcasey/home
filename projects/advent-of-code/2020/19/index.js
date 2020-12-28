const fs = require('fs')
const util = require('util')

const TESTING = false // part1: 3, part2: 12
const INPUT_PATH = `${__dirname}/${TESTING ? 'test' : 'input'}.txt`

const split = (str, separator = '\n') => str.split(separator).filter((s) => !!s)
const log = (obj) => console.log(util.inspect(obj, false, null, true))

const readInput = async () => {
  const file = await fs.readFileSync(INPUT_PATH, 'utf8')
  return split(file, '\n\n')
}

const parseRules = (input) =>
  split(input).reduce((obj, str) => {
    const [idStr, ruleStr] = str.split(': ')
    obj[Number(idStr)] = parseRule(ruleStr)
    return obj
  }, {})

const parseRule = (str) => {
  if (str.startsWith('"')) return str.replaceAll('"', '')
  return str.split(' | ').map((subrule) => subrule.split(' ').map(Number))
}

const buildRegex = (rules, rule, breaker = 0) => {
  if (Array.isArray(rule)) {
    if (rule.length === 1) return buildRegex(rules, rule[0], breaker)
    if (rule.filter(Array.isArray).length)
      return `(${rule
        .map((subrule) => buildRegex(rules, subrule, breaker))
        .join('|')})`
    return `${rule.map((item) => buildRegex(rules, item, breaker)).join('')}`
  }
  if (Number.isInteger(rule)) {
    if (breaker > 10) return ''
    switch (rule) {
      case 8:
        return buildRegex(rules, parseRule('42 | 42 8'), ++breaker)
      case 11:
        return buildRegex(rules, parseRule('42 31 | 42 11 31'), ++breaker)
      default:
        return buildRegex(rules, rules[rule], breaker)
    }
  }
  return rule
}

const run = async () => {
  const input = await readInput()
  const rules = parseRules(input[0])
  const reStr = `^${buildRegex(rules, rules[0])}$`
  const re = new RegExp(reStr)
  const messages = split(input[1])

  const answer = messages.reduce(
    (count, message) => (count += re.test(message) ? 1 : 0),
    0,
  )
  console.log(`The number of valid messages is ${answer}.`)
}

run()
