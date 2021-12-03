
file = open('day-03.txt', 'r')
data = []
for line in file:
  line = line.strip()
  data.append( line )
file.close()

SIZE = len(data[0])
NUM_LINES = len(data)

ones = [0]*SIZE
for line in data:
  i = 0
  for digit in line:
    if digit == '1':
      ones[i] += 1
    i += 1

gamma = ['0']*SIZE
epsilon = ['1']*SIZE
i = 0
for digit in ones:
  if ones[i] > NUM_LINES / 2:
    gamma[i] = '1'
    epsilon[i] = '0'
  i += 1

gamma = int(''.join(gamma), 2 )
epsilon = int(''.join(epsilon), 2 )
print( gamma * epsilon )

# part two
def part_two( data, keep_most_common = True ):
    d = list(data)
    i = 0
    NUM_LINES = 0
    while i < SIZE:
      count = 0
      for cur in d:
        if cur[i] == '1':
          count += 1

      most_common = False
      if count >= len(d) / 2:
        most_common = True

      if keep_most_common != most_common:
        look_for = '1'
      else:
        look_for = '0'

      j = 0
      while j < len(d):
        if d[j][i] == look_for:
          j += 1
        else:
          d.pop(j)
          if len(d) == 1:
            d = int(''.join(d), 2)
            return d

      i += 1

oxygen_generator_rating = part_two( data, True )
co2_scrubber_rating =part_two( data, False )
print( oxygen_generator_rating * co2_scrubber_rating )
