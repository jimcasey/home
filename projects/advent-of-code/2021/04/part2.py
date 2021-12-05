import os

scriptPath = os.path.dirname(os.path.abspath(__file__))
inputPath = scriptPath + '/input.txt'

with open(inputPath) as file:
  selections = list(map(int, file.readline().replace('\n', '').split(',')))
  boards = []
  fills = []
  for line in file.read().splitlines():
    if line == '':
      boards.append([])
      fills.append([0] * 10)
    else:
      row = []
      boards[len(boards) - 1].append(row)
      for n in range(5):
        start = n * 3
        row.append(int(line[start:start + 2]))

hasWon = [False] * len(boards)
for selection in selections:
  lastSelection = selection
  for boardIndex, board in enumerate(boards):
    if hasWon[boardIndex]:
      continue
    for rowIndex, row in enumerate(board):
      try:
        valueIndex = row.index(selection)
        row[valueIndex] = None
        fills[boardIndex][rowIndex] += 1
        fills[boardIndex][valueIndex + 5] += 1
        for count in fills[boardIndex]:
          if count == 5:
            hasWon[boardIndex] = True
            lastWinner = boardIndex
            break
        break
      except ValueError:
        continue
  try:
    hasWon.index(False)
  except ValueError:
    break

score = 0
for row in boards[lastWinner]:
  for value in row:
    if value != None:
      score += value
score = score * lastSelection

print('The last winner score is ' + str(score) + '.')
