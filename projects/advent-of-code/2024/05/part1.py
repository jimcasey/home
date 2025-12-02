from os import path

scriptPath = path.dirname(path.abspath(__file__))
inputPath = scriptPath + '/input.txt'


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

  valid = []
  for update in updates:
    isValid = True
    pages = update.split(',')
    for rule in rules:
      parts = rule.split('|')

      if parts[0] in pages and parts[1] in pages:
        if pages.index(parts[0]) > pages.index(parts[1]):
          isValid = False
          break

    if isValid:
      valid.append(update)

  answer = 0
  for update in valid:
    pages = update.split(',')
    answer += int(pages[len(pages)//2])

  print(answer)


def readInput():
  with open(inputPath) as file:
    return file.read().splitlines()


main()
