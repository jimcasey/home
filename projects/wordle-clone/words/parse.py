import os
import sys

class printc:
  bright = '\033[1;36m'
  error = '\033[1;31m'
  gray = '\033[90m'
  normal = '\033[0m'
  warning = '\033[1;33m'

  def color(color, value): print(f'{color}{value}{printc.normal}')
  def act(value): printc.color(printc.bright, value)
  def cmd(value): printc.color(printc.gray, value)
  def err(value): printc.color(printc.error, value)
  def war(value): printc.color(printc.warning, value)

if len(sys.argv) <= 1:
  printc.war('Input path required')
  printc.cmd('Usage: python3 parse.py ~/Downloads/words.txt')
  sys.exit()

scriptPath = os.path.dirname(os.path.abspath(__file__))
inputPath = sys.argv[1]
outputPath = scriptPath + '/words.txt'

printc.act('Parsing file...')
printc.cmd(inputPath)

with open(inputPath) as file:
  words = file.read().splitlines()

printc.act('Writing file...')
printc.cmd(outputPath)

with open(outputPath, 'w') as file:
  for word in words:
    if word.startswith('#') or word.find("'") != -1:
      continue
    if len(word) == 5:
      file.write(word + '\n')

print('Done!')
