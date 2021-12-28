from collections import defaultdict
import os

scriptPath = os.path.dirname(os.path.abspath(__file__))
inputPath = scriptPath + '/input.txt'

def main():
  position1, position2 = readInput()
  game = Game(position1, position2)
  wins = game.play()

  print(f'The player with the most wins won in {max(wins)} universes.')

def readInput():
  with open(inputPath) as file:
    return tuple(
        int(line.split(': ')[1])
        for line in file.read().splitlines()
    )

class Game:
  wins = [0, 0]

  def __init__(self, position1, position2):
    self.games = defaultdict(int)
    self.games[((position1, 0), (position2, 0))] = 1

    self.rolls = defaultdict(int)
    for d1 in range(1, 4):
      for d2 in range(1, 4):
        for d3 in range(1, 4):
          self.rolls[d1 + d2 + d3] += 1

  def play(self):
    while len(self.games) > 0:
      self.round()
    return self.wins

  def round(self):
    previousGames = dict(self.games)
    self.games = defaultdict(int)
    for state, universes in previousGames.items():
      player1, player2 = state

      for roll1, rollUniverses1 in self.rolls.items():
        newPlayer1 = self.move(player1, roll1)
        newUniverses1 = universes * rollUniverses1
        if newPlayer1[1] >= 21:
          self.wins[0] += newUniverses1
        else:
          for roll2, rollUniverses2 in self.rolls.items():
            newPlayer2 = self.move(player2, roll2)
            newUniverses2 = newUniverses1 * rollUniverses2
            if newPlayer2[1] >= 21:
              self.wins[1] += newUniverses2
            else:
              self.games[(newPlayer1, newPlayer2)] += newUniverses2

  def move(self, player, roll):
    position, score = player
    newPosition = (position + roll - 1) % 10 + 1
    newScore = score + newPosition
    return (newPosition, newScore)

main()

# credit where credit is due:
# https://bit.ly/3HjuVk4
