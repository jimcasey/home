from os import path

scriptPath = path.dirname(path.abspath(__file__))
inputPath = scriptPath + '/test.txt'

# #############
# #...........#
# ###1#3#5#7###
#   #0#2#4#6#
#   #########

def main():
  pass

def readInput():
  with open(inputPath) as file:
    return file.read().splitlines()

main()
