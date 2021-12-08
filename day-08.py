file = open('day-08.txt', 'r')
data = []
for line in file:
  parts = line.strip().split( ' | ' )
  data.append( parts )
file.close()

# --- part one ---
count = 0
for d in data:
  digits = d[1].split()
  for digit in digits:
    l = len(digit)
    if l in [2,3,4,7]:
      count += 1

print( count )

# --- part two ---

def get_diffs3( a, b, c ):
  result = get_diffs(a, b)
  for i in get_diffs(b, a):
    if not i in result:
      result += i
  for i in get_diffs(a, c):
    if not i in result:
      result += i
  for i in get_diffs(c, a):
    if not i in result:
      result += i

  return result

def get_diffs( a, b, ignore=None ):
  result = ''
  for i in b:
    if i != ignore and not i in a and not i in result:
      result += i
  return result


number_map = { 'abcefg':'0', 'cf':'1',     'acdeg':'2', 'acdfg':'3',   'bcdf':'4',
               'abdfg':'5',  'abdefg':'6', 'acf':'7',   'abcdefg':'8', 'abcdfg':'9' }

sum = 0
for d in data:
  left = d[0].split()
  right = d[1].split()

  scrambled = {}
  for l in left:
    key = len(l)
    if not key in scrambled:
      scrambled[key] = [l]
    else:
      scrambled[key].append(l)

  #    --aaa--
  #    |     |
  #   bbb   ccc
  #    |     |
  #    --ddd--
  #    |     |
  #   eee   fff
  #    |     |
  #    --ggg--

  mapping = {}

  # the number 1 contains segments c and f
  mapping['c'] = mapping['f'] = ''.join(scrambled[2][0])
  # the difference between 1 and 7 represents segment a
  mapping['a'] = get_diffs(scrambled[2][0], scrambled[3][0])
  # the difference between 4 and 7 represents segments b and d
  mapping['b'] = mapping['d'] = get_diffs(scrambled[3][0], scrambled[4][0])
  # the difference between 4 and 8 (ignoring segment a) represents segments e and g
  mapping['e'] = mapping['g'] = get_diffs(scrambled[4][0], scrambled[7][0], ignore=mapping['a'])

  # the difference between 0, 6, and 9 (the size 6 numbers) are segments c, d, and e
  six_diffs = get_diffs3(scrambled[6][0], scrambled[6][1], scrambled[6][2])
  for key in mapping.keys():
    for diff in six_diffs:
      if diff in mapping[key]:
        if key in ['c','d','e']:
          mapping[key] = diff
        else:
          mapping[key] = mapping[key].replace(diff,'')
        break

  result = ''
  for r in right:
    cur = ''
    for k, v in mapping.items():
      if v in r:
        cur += k
    result += number_map[''.join(sorted(cur))]
  sum += int(result)

print( sum )
