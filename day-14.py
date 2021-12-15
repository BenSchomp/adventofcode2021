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
    mapping[left] = left[0] + right + left[1]
file.close()

print( starting_polymer )
print( mapping )

def expand( polymer, depth ):
  #print( '    '*depth, '-', polymer, '...', depth )
  global mapping

  if depth <= 0 or len(polymer) < 2:
    # base case
    #print( '    '*(5-depth), '-', polymer )
    return polymer

  elif polymer in mapping:
    # expand via lookup
    #print( '    '*depth, '#', polymer, mapping[polymer] )
    # RIGHT HERE
    #if we have more mappings, return expand( mapping[polymer], depth-expanded_depth )
    asdf = False
    next = mapping[polymer]
    while next in mapping and depth > 0:
      asdf = True
      depth -= 1
      print( polymer, next, depth, mapping[next] )
      next = mapping[next]

    #if x in mapping:
      #print( polymer, mapping[polymer], x, mapping[x] )
      #exit()
    return expand( next, depth-1 )

    #return expand( mapping[polymer], depth-1 )

  else:
    # divide and conquer
    l = len(polymer)
    left  = polymer[:int(l/2)]
    right = polymer[int(l/2):]
    mid   = str(left[-1]+right[0])

    x = expand( left, depth )
    y = expand( mid, depth )
    z = expand( right, depth )

    result = x + y[1:-1] + z
    #print( '    '*depth, '+', polymer, left, mid, right, x, y, z )

    if len(result) == len(polymer)*2-1 and not polymer in mapping:
      mapping[polymer] = result

    return result

d = 7
result = expand( starting_polymer, d )
print( result )
if d == 3 and result != 'NBBBCNCCNBBNBNBBCHBHHBCHB':
  print( '!! MISMATCH !!' )
  exit()
elif d == 4 and result != 'NBBNBNBBCCNBCNCCNBBNBBNBBBNBBNBBCBHCBHHNHCBBCBHCB':
  print( '!! MISMATCH !!' )
  exit()


counts = {}
for letter in result:
  if not letter in counts:
    counts[letter] = 1
  else:
    counts[letter] += 1
print( counts )

count_min = count_max = None
for k, v in counts.items():
  if not count_min or v < count_min:
    count_min = v
  if not count_max or v > count_max:
    count_max = v

print( count_max - count_min )
print( mapping )
