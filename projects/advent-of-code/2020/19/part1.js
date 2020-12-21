const fs = require('fs')
const util = require('util')

const TESTING = false // 2
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

const buildRegex = (rules, rule) => {
  if (Array.isArray(rule)) {
    if (rule.length === 1) return buildRegex(rules, rule[0])
    if (rule.filter(Array.isArray).length)
      return `(${rule.map((subrule) => buildRegex(rules, subrule)).join('|')})`
    return `${rule.map((item) => buildRegex(rules, item)).join('')}`
  }
  if (Number.isInteger(rule)) return buildRegex(rules, rules[rule])
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
