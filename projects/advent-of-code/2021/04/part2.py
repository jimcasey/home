import os
import re

scriptPath = os.path.dirname(os.path.abspath(__file__))
inputPath = scriptPath + '/input.txt'

with open(inputPath) as file:
  # parse the list of called numbers
  calledNumbers = list(map(int, file.readline().replace('\n', '').split(',')))

  # parse the boards
  boards = []
  for line in file.read().splitlines():
    if line == '':
      # blank line, add a new board
      boards.append([])
    else:
      # add a new row to the last board
      boards[len(boards) - 1].append(list(map(int, re.findall('\d+', line))))

# find the size of the board
boardSize = len(boards[0][0])

# initialize counts for possible wins in each board
selectionCounts = [[0] * boardSize * 2 for _ in boards]

# track whether we've found a solution for each board
hasWon = [False] * len(boards)

for calledNumber in calledNumbers:
  # keep track of the last called number for calculating score
  lastCalledNumber = calledNumber

  for boardIndex, board in enumerate(boards):
    if hasWon[boardIndex]:
      # we don't care about this board since we've found a solution
      continue

    for rowIndex, row in enumerate(board):
      if calledNumber in row:
        # called number is in this row, get the index
        valueIndex = row.index(calledNumber)

        # unset the value so we don't calculate it in the score
        row[valueIndex] = None

        # count this selection for this row
        selectionCounts[boardIndex][rowIndex] += 1
        rowCount = selectionCounts[boardIndex][rowIndex]

        # count this selection for this column
        selectionCounts[boardIndex][valueIndex + boardSize] += 1
        columnCount = selectionCounts[boardIndex][valueIndex + boardSize]

        if rowCount == boardSize or columnCount == boardSize:
          # we've got a winner
          hasWon[boardIndex] = True
          lastWinner = boardIndex

        break

  if False not in hasWon:
    # all boards have won
    break

# calculate the score
score = 0
for row in boards[lastWinner]:
  for value in row:
    if value != None:
      score += value
score = score * lastCalledNumber

print('The last winner score is ' + str(score) + '.')
