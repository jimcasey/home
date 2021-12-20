from functools import reduce
from math import ceil, floor
import os

scriptPath = os.path.dirname(os.path.abspath(__file__))
inputPath = scriptPath + '/input.txt'

with open(inputPath) as file:
  # eval the input to get numbers
  numbers = list(map(eval, file.read().splitlines()))

class NumberMap:
  rootPair = []   # root node pair
  leafNodes = []  # ordered list of leaf nodes

  # parses the number and sets the root and items
  def setNumber(self, number):
    self.rootPair, self.leafNodes = self.parse(number)

  # parses a number pair into a node pair and leaf nodes
  def parse(self, numberPair, parentNode=None, depth=0):
    nodePair = []
    leafNodes = []

    for number in numberPair:
      if isinstance(number, list):
        # node is a parent
        node = {
            'type': 'parent',
            'depth': depth,
            'parentNode': parentNode
        }

        # get child nodes, all child leaf nodes
        childNodes, childLeafNodes = self.parse(number, node, depth + 1)
        node['childNodes'] = childNodes

        # append to output
        nodePair.append(node)
        leafNodes += childLeafNodes
      else:
        # node is a leaf
        node = {
            'type': 'leaf',
            'depth': depth,
            'parentNode': parentNode,
            'value': number
        }

        # append to output
        nodePair.append(node)
        leafNodes.append(node)
    return nodePair, leafNodes

  # returns the number for the current number state
  def number(self, nodePair=None):
    if nodePair == None:
      # start with the root pair if node pair is not provided
      return self.number(self.rootPair)

    number = []
    for node in nodePair:
      if node['type'] == 'parent':
        # append the numbers for all child nodes
        number.append(self.number(node['childNodes']))
      else:
        # append the number for leaf
        number.append(node['value'])

    return number

  # adds a number to the current number state
  def add(self, number):
    # add numbers together if not in an empty state
    number = number if len(self.leafNodes) == 0 else [self.number()] + [number]

    # set the new number
    self.setNumber(number)

    # kick off a reduction
    self.reduce()

  # reduces the current number state
  def reduce(self):
    while True:
      # explode the number
      didExplode = self.explode()
      if not didExplode:
        # no more explosions possible, split the number
        didSplit = self.split()
        if not didSplit:
          # no more splits possible
          break

  # explodes the current number state
  def explode(self):
    didExplode = False

    # iterate through all leaves in order
    for leafIndex in range(len(self.leafNodes)):
      node = self.leafNodes[leafIndex]
      if node['depth'] == 4:
        # found a node to explode
        didExplode = True

        # find and update the previous leaf value, if available
        leftNode = node
        prevLeafIndex = leafIndex - 1
        if prevLeafIndex >= 0:
          self.leafNodes[prevLeafIndex]['value'] += leftNode['value']

        # find and update the next leaf value, if available
        rightNode = self.leafNodes[leafIndex + 1]
        nextLeafIndex = leafIndex + 2
        if nextLeafIndex < len(self.leafNodes):
          self.leafNodes[nextLeafIndex]['value'] += rightNode['value']

        # get the parent node
        parentNode = leftNode['parentNode']

        # create the replacement node with zero value one level up
        replacementNode = {
            'type': 'leaf',
            'depth': 3,
            'parentNode': parentNode['parentNode'],
            'value': 0
        }

        # remove parent node from its siblings and add the replacement
        childNodes = replacementNode['parentNode']['childNodes']
        childIndex = childNodes.index(parentNode)
        childNodes.remove(parentNode)
        childNodes.insert(childIndex, replacementNode)

        # remove the exploded leaf nodes and add the replacement
        self.leafNodes.remove(leftNode)
        self.leafNodes.remove(rightNode)
        self.leafNodes.insert(leafIndex, replacementNode)

        break

    return didExplode

  # splits the current number state
  def split(self):
    didSplit = False

    leafIndex = 0
    while leafIndex < len(self.leafNodes):
      node = self.leafNodes[leafIndex]
      if node['value'] > 9:
        # found a node to split
        didSplit = True

        # get properties from the current node
        value = node['value']
        depth = node['depth']
        parentNode = node['parentNode']

        # appropriate the node for the new left node
        leftNode = node
        leftNode['value'] = floor(value / 2)
        leftNode['depth'] = depth + 1

        # create the new right node
        rightNode = {
            'type': 'leaf',
            'depth': depth + 1,
            'value': ceil(value / 2)
        }

        # insert the new right node into the leaf nodes
        leafIndex += 1
        self.leafNodes.insert(leafIndex, rightNode)

        # create the replacement parent node
        replacementNode = {
            'type': 'parent',
            'depth': depth,
            'parentNode': parentNode,
            'childNodes': [leftNode, rightNode]
        }
        leftNode['parentNode'] = replacementNode
        rightNode['parentNode'] = replacementNode

        # remove the split node and add the new parent node
        childIndex = parentNode['childNodes'].index(node)
        parentNode['childNodes'].remove(node)
        parentNode['childNodes'].insert(childIndex, replacementNode)

        break

      leafIndex += 1

    return didSplit

  # gets the magnitude for the current number state
  def magnitude(self, nodePair=None):
    if nodePair == None:
      # start with the root pair if node pair is not provided
      return self.magnitude(self.rootPair)

    # get left and right values
    leftValue, rightValue = list(map(
        lambda node: (
            node['value'] if node['type'] == 'leaf'
            else self.magnitude(node['childNodes'])
        ),
        nodePair
    ))

    return leftValue * 3 + rightValue * 2

maxMagnitude = 0
for a in range(len(numbers)):
  for b in range(len(numbers)):
    if a == b:
      continue

    numberMap = NumberMap()
    numberMap.add(numbers[a])
    numberMap.add(numbers[b])
    maxMagnitude = max(maxMagnitude, numberMap.magnitude())

print(f'Largest mangnitude any two numbers is {maxMagnitude}.')
