from os import path
import re

scriptPath = path.dirname(path.abspath(__file__))
inputPath = scriptPath + '/input.txt'


def main():
  lines = readInput()
  times = [int(n) for n in re.findall(r'\d+', lines[0])]
  records = [int(n) for n in re.findall(r'\d+', lines[1])]

  score = None
  for race in range(0, len(times)):
    beats = 0
    time = times[race]
    record = records[race]
    for speed in range(1, time + 1):
      distance = speed * (time - speed)
      if distance > record:
        beats += 1
    if score is None:
      score = beats
    else:
      score *= beats
  print(score)


def readInput():
  with open(inputPath) as file:
    return file.read().splitlines()


main()
