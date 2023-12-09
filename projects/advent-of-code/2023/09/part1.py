from os import path

scriptPath = path.dirname(path.abspath(__file__))
inputPath = scriptPath + '/input.txt'


def main():
  lines = readInput()
  sequences = [[int(s) for s in line.split()] for line in lines]

  sum = 0
  for sequence in sequences:
    differences = [[sequence[i+1] - sequence[i] for i in range(0, len(sequence) - 1)]]

    searching = True
    while searching:
      differences.append([differences[-1][i+1] - differences[-1][i] for i in range(0, len(differences[-1]) - 1)])

      done = True
      for d in differences[-1]:
        if d != 0:
          done = False
          break
      if done:
        searching = False

    next = 0
    while len(differences) > 0:
      next += differences[-1][-1]
      differences.pop()
    next += sequence[-1]
    sum += next

  print(sum)


def readInput():
  with open(inputPath) as file:
    return file.read().splitlines()


main()
