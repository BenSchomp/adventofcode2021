file = open('day-10.txt', 'r')
data = []
for line in file:
  data.append( line.strip() )
file.close()

openers = ['(','[','{','<']
closers = [')',']','}','>']
scores = [3, 57, 1197, 25137]

part_one = 0
part_two = []
for line in data:
  s = []
  corrupted = False
  for c in line:
    if c in openers:
      s.append(c)
    else:
      cur = s.pop(-1)
      i = closers.index(c)
      if cur != openers[i]:
        part_one += scores[i]
        corrupted = True
        break

  if not corrupted:
    sum = 0
    for c in reversed(s):
      sum = (sum * 5) + openers.index(c) + 1
    part_two.append(sum)

print( part_one )
print( sorted(part_two)[int(len(part_two)/2)] )
