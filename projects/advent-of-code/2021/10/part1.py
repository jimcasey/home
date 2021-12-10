import os

scriptPath = os.path.dirname(os.path.abspath(__file__))
inputPath = scriptPath + '/input.txt'

with open(inputPath) as file:
  lines = file.read().splitlines()

open = ['(', '[', '{', '<']
close = [')', ']', '}', '>']
points = {
    ')': 3,
    ']': 57,
    '}': 1197,
    '>': 25137,
}

score = 0
for line in lines.copy():
  chunks = []
  for c in line:
    if c in open:
      chunks.append(c)
    else:
      * _, last = chunks
      if open[close.index(c)] != last:
        score += points[c]
        break
      chunks.pop()

print(f'Score is {score}.')
