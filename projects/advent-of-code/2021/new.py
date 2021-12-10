import os
import sys
from shutil import copyfile

class printc:
  bright = "\033[1;36m"
  error = "\033[1;31m"
  gray = "\033[90m"
  normal = "\033[0m"
  warning = "\033[1;33m"

  def color(color, value): print(f'{color}{value}{printc.normal}')
  def act(value): printc.color(printc.bright, value)
  def cmd(value): printc.color(printc.gray, value)
  def err(value): printc.color(printc.error, value)
  def war(value): printc.color(printc.warning, value)

if len(sys.argv) <= 1:
  printc.war('Folder name requred.')
  printc.cmd('Usage: python3 new.py 06')
  sys.exit()

scriptPath = os.path.dirname(os.path.abspath(__file__))
folderPath = f'{scriptPath}/{sys.argv[1]}'

if os.path.isdir(folderPath):
  printc.war('Folder already exists.')
  printc.cmd(folderPath)
  sys.exit()

printc.act('Creating new folder and files...')

templatePath = f'{scriptPath}/template.py'
part1Path = f'{folderPath}/part1.py'
testPath =f'{folderPath}/test.txt'
inputPath =f'{folderPath}/input.txt'

os.mkdir(folderPath)
copyfile(templatePath, part1Path)
open(testPath, 'a').close()
open(inputPath, 'a').close()

os.system(f'code {part1Path}')
os.system(f'code {testPath}')
os.system(f'code {inputPath}')

print('Done!')
