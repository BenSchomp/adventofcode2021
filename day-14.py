file = open('day-14.txt', 'r')
starting_polymer = None
mapping = {}
for line in file:
  line = line.strip()
  if not starting_polymer:
    starting_polymer = line
  elif not len(line):
    continue
  else:
    (left, right) = line.split(' -> ')
    mapping[left] = [0, left[0] + right, right + left[1]]
file.close()

print( starting_polymer )

def expand( polymer, depth ):
  global mapping

  for i in range(len(polymer)-1):
    mapping[polymer[i]+polymer[i+1]][0] += 1

  while depth > 0:
    cur_pairs = {}
    for k, v in mapping.items():
      if v[0] > 0:
        cur_pairs[k] = v[0]

    for k, count in cur_pairs.items():
      v = mapping[k]
      mapping[k][0] -= count
      mapping[v[1]][0] += count
      mapping[v[2]][0] += count

    depth -= 1

  counts = {}
  for k, v in mapping.items():
    if k[0] not in counts: # only count first letter of pairs
      counts[k[0]] = v[0]
    else:
      counts[k[0]] += v[0]
  counts[polymer[-1]] += 1 # add in the second letter of the last pair

  # find count min and max
  count_min = count_max = None
  for k, v in counts.items():
    if not count_min or v < count_min:
      count_min = v
    if not count_max or v > count_max:
      count_max = v

  return count_max - count_min

print( 'part one:', expand( starting_polymer, 10 ) )
# reset
for k, v in mapping.items():
  mapping[k][0] = 0

print( 'part two:', expand( starting_polymer, 40 ) )
