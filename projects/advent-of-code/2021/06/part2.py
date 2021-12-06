import os

scriptPath = os.path.dirname(os.path.abspath(__file__))
inputPath = scriptPath + '/input.txt'

with open(inputPath) as file:
  initial = list(map(int, file.read().splitlines()[0].split(',')))

def addTo(dictionary, key, value):
  dictionary[key] = value if key not in dictionary else dictionary[key] + value

current = {}
for key in initial:
  addTo(current, key, 1)

for _ in range(256):
  born = 0
  next = {}
  for key in current.keys():
    timer = key - 1
    if timer < 0:
      timer = 6
      born += current[key]
    addTo(next, timer, current[key])
  if born:
    next[8] = born
  current = next

count = 0
for value in current.values():
  count += value

print('There are {0} fish.'.format(count))
