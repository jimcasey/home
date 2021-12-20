from functools import reduce
from math import ceil, floor
import os

scriptPath = os.path.dirname(os.path.abspath(__file__))
inputPath = scriptPath + '/input.txt'

with open(inputPath) as file:
  numbers = list(map(eval, file.read().splitlines()))

class NumberMap:
  items = []
  root = {}

  def set(self, number):
    self.root, self.items = self.parse(number)

  def parse(self, pair, parent=None, depth=0):
    nodes = []
    items = []
    for n in pair:
      if isinstance(n, list):
        node = {
            'type': 'list',
            'depth': depth,
            'parent': parent
        }
        depth += 1
        childNodes, childItems = self.parse(n, node, depth)
        depth -= 1

        node['children'] = childNodes
        nodes.append(node)
        items += childItems
      else:
        item = {
            'type': 'int',
            'depth': depth,
            'parent': parent,
            'value': n
        }
        nodes.append(item)
        items.append(item)
    return nodes, items

  def number(self, nodes=None):
    if nodes == None:
      return self.number(self.root)

    number = []
    for node in nodes:
      if node['type'] == 'list':
        number.append(self.number(node['children']))
      else:
        number.append(node['value'])
    return number

  def add(self, number):
    number = number if len(self.items) == 0 else [self.number()] + [number]
    self.set(number)
    self.reduce()

  def reduce(self):
    while True:
      didExplode = self.explode()
      if not didExplode:
        didSplit = self.split()
        if not didSplit:
          break

  def explode(self):
    didExplode = False

    for index in range(len(self.items)):
      item = self.items[index]
      if item['depth'] == 4:
        didExplode = True

        prevIndex = index - 1
        if prevIndex >= 0:
          self.items[prevIndex]['value'] += item['value']

        nextIndex = index + 2
        itemPair = self.items[index + 1]
        if nextIndex < len(self.items):
          self.items[nextIndex]['value'] += itemPair['value']

        parent = item['parent']

        node = {
            'type': 'int',
            'depth': 3,
            'parent': parent['parent'],
            'value': 0
        }

        childIndex = node['parent']['children'].index(parent)
        node['parent']['children'].remove(parent)
        node['parent']['children'].insert(childIndex, node)

        self.items.remove(item)
        self.items.remove(itemPair)
        self.items.insert(index, node)

        break

    return didExplode

  def split(self):
    didSplit = False

    index = 0
    while index < len(self.items):
      item = self.items[index]
      if item['value'] > 9:
        didSplit = True

        value = item['value']
        depth = item['depth']

        item['value'] = floor(value / 2)
        item['depth'] += 1

        itemPair = {
            'type': 'int',
            'depth': item['depth'],
            'value': ceil(value / 2)
        }

        index += 1
        self.items.insert(index, itemPair)

        parent = item['parent']
        node = {
            'type': 'list',
            'depth': depth,
            'parent': parent,
            'children': [item, itemPair]
        }
        item['parent'] = node
        itemPair['parent'] = node

        childIndex = parent['children'].index(item)
        parent['children'].remove(item)
        parent['children'].insert(childIndex, node)

        break

      index += 1

    return didSplit

  def magnitude(self, nodes=None):
    if nodes == None:
      return self.magnitude(self.root)

    left, right = list(map(
        lambda node: (
            node['value'] if node['type'] == 'int'
            else self.magnitude(node['children'])
        ),
        nodes
    ))

    return left * 3 + right * 2

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
