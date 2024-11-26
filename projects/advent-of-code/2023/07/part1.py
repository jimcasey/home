from functools import cmp_to_key
from os import path

scriptPath = path.dirname(path.abspath(__file__))
inputPath = scriptPath + '/input.txt'


def getWinner(hand1, hand2):
  def getHandRank(hand):
    counts = {}
    for card in hand:
      counts[card] = counts.get(card, 0) + 1

    if len(counts) == 1:
      # five of a kind
      return 6
    elif len(counts) == 2:
      if 4 in counts.values():
        # four of a kind
        return 5
      else:
        # full house
        return 4
    elif len(counts) == 3:
      if 3 in counts.values():
        # three of a kind
        return 3
      else:
        # two pair
        return 2
    elif len(counts) == 4:
      # one pair
      return 1
    elif len(counts) == 5:
      # high card
      return 0
    else:
      raise ValueError("Invalid hand")

  rank1 = getHandRank(hand1)
  rank2 = getHandRank(hand2)

  if rank1 != rank2:
    return 1 if rank1 > rank2 else -1

  cardOrder = '23456789TJQKA'

  def compareCards(card1, card2):
    return cardOrder.index(card1) - cardOrder.index(card2)

  for card1, card2 in zip(hand1, hand2):
    if compareCards(card1, card2) != 0:
      return 1 if compareCards(card1, card2) > 0 else -1

  return 0


def main():
  hands = readInput()
  hands.sort(key=cmp_to_key(lambda hand1, hand2: getWinner(hand1.split()[0], hand2.split()[0])))

  score = 0
  for index, line in enumerate(hands):
    score += (index + 1) * int(line.split()[1])

  print(score)


def readInput():
  with open(inputPath) as file:
    return file.read().splitlines()


main()
