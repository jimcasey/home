from os import path
import re

scriptPath = path.dirname(path.abspath(__file__))
inputPath = scriptPath + '/input.txt'


def fixRules(update, rules):
  pages = update.split(',')
  for rule in rules:
    parts = rule.split('|')
    if parts[0] in pages and parts[1] in pages:
      if pages.index(parts[0]) > pages.index(parts[1]):
        pages.remove(parts[1])
        pages.insert(pages.index(parts[0]) + 1, parts[1])
  return ','.join(pages)


def main():
  input = readInput()

  rules = []
  updates = []
  section = 'rules'
  for line in input:
    if line == '':
      section = 'updates'
    elif section == 'rules':
      rules.append(line)
    elif section == 'updates':
      updates.append(line)

  invalid = []
  for update in updates:
    isValid = True
    while True:
      fixed = fixRules(update, rules)
      if fixed == update:
        break
      isValid = False
      update = fixed

    if not isValid:
      invalid.append(update)

  answer = 0
  for update in invalid:
    pages = update.split(',')
    answer += int(pages[len(pages)//2])

  print(answer)


def readInput():
  with open(inputPath) as file:
    return file.read().splitlines()


main()
