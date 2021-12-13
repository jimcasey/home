import os
import re

scriptPath = os.path.dirname(os.path.abspath(__file__))
inputPath = scriptPath + '/input.txt'

def lmap(func, iterable): return list(map(func, iterable))

with open(inputPath) as file:
  dots, folds = file.read().split('\n\n')

  def parseDot(line): return lmap(int, line.split(','))
  dots = lmap(parseDot, dots.splitlines())

  def parseFold(line):
    axis, pos = re.match('fold along (x|y)=(\d+)', line).group(1, 2)
    return [axis, int(pos)]
  folds = lmap(parseFold, folds.splitlines())

class Paper:
  def __init__(self, dots):
    self.paper = {}
    for x, y in dots:
      self.set(x, y)

  def set(self, x, y):
    self.paper[f'{x},{y}'] = [x, y]

  def fold(self, axis, pos):
    dots = self.paper.values()
    self.paper = {}
    for x, y in dots:
      newX, newY = self.translate(x, y, axis, pos)
      self.set(newX, newY)

  def translate(self, x, y, axis, pos):
    if axis == 'x':
      return [self.calculate(x, pos), y]
    else:
      return [x, self.calculate(y, pos)]

  def calculate(self, point, pos):
    return point if point < pos else pos - (point - pos)

  def count(self):
    return len(self.paper)

paper = Paper(dots)

axis, pos = folds[0]
paper.fold(axis, pos)

print(f'{paper.count()} dots are visible.')
