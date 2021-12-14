file = open('day-14.txt', 'r')
polymer = None
rules = {}
for line in file:
  line = line.strip()
  if not polymer:
    polymer = line
  elif not len(line):
    continue
  else:
    (left, right) = line.split(' -> ')
    rules[left] = right
file.close()

print(polymer, rules )

for count in range(10):
  inserts = []
  for i in range(len(polymer)):
    cur = polymer[i:i+2]
    if cur in rules:
      inserts.append((i+1, rules[cur]))

  #print( inserts )

  while len(inserts):
    (i, val) = inserts.pop()
    polymer = polymer[:i] + val + polymer[i:]

  #print( count, polymer )

counts = {}
for letter in polymer:
  if not letter in counts:
    counts[letter] = 1
  else:
    counts[letter] += 1

print( polymer )
print( counts )

count_min = count_max = None
for k, v in counts.items():
  if not count_min:
    count_min = v
  if not count_max:
    count_max = v

  if v < count_min:
    count_min = v
  if v > count_max:
    count_max = v

print( count_max - count_min )
