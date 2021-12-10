import os

scriptPath = os.path.dirname(os.path.abspath(__file__))
inputPath = scriptPath + '/test.txt'

with open(inputPath) as file:
  lines = file.read().splitlines()
