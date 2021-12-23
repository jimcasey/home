import os

scriptPath = os.path.dirname(os.path.abspath(__file__))
inputPath = scriptPath + '/input.txt'

def main():
  players = readInput()

  turn = 0
  die = Die()
  while True:
    player = players[turn % 2]
    player.move(die.rolls(3))

    if players[0].score >= 1000 or players[1].score >= 1000:
      break

    turn += 1

  winner = players[(turn) % 2]
  loser = players[(turn + 1) % 2]
  print(winner.score, loser.score, die.total, loser.score * die.total)

class Die:
  total = 0

  def roll(self):
    self.total += 1
    return mod1(self.total, 100)

  def rolls(self, count):
    return [self.roll() for _ in range(count)]

class Player:
  score = 0

  def __init__(self, position):
    self.position = position

  def move(self, rolls):
    self.position = mod1(self.position + sum(rolls), 10)
    self.score += self.position

def mod1(n, mod):
  return mod if n % mod == 0 else n % mod

def readInput():
  with open(inputPath) as file:
    return tuple(
        Player(int(line.split(': ')[1]))
        for line in file.read().splitlines()
    )

main()
