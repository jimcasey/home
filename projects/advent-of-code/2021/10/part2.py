import os

scriptPath = os.path.dirname(os.path.abspath(__file__))
inputPath = scriptPath + '/input.txt'

with open(inputPath) as file:
  lines = file.read().splitlines()

open = ['(', '[', '{', '<']
close = [')', ']', '}', '>']
points = {
    ')': 1,
    ']': 2,
    '}': 3,
    '>': 4,
}

scores = []
for line in lines.copy():
  chunks = []
  corrupt = False
  for c in line:
    if c in open:
      chunks.append(c)
    else:
      * _, last = chunks
      if open[close.index(c)] != last:
        corrupt = True
        break
      chunks.pop()
  if not corrupt:
    closers = []
    chunks.reverse()
    for c in chunks:
      closers.append(close[open.index(c)])

    score = 0
    for c in closers:
      score *= 5
      score += points[c]
    scores.append(score)

median = sorted(scores)[int(len(scores) / 2)]

print(f'Median score is {median}.')
