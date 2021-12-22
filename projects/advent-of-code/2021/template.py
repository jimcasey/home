import os

scriptPath = os.path.dirname(os.path.abspath(__file__))
inputPath = scriptPath + '/test.txt'

def main():
  pass

def readInput():
  with open(inputPath) as file:
    return file.read().splitlines()

main()
