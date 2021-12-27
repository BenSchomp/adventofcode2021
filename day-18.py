file = open('day-18.txt', 'r')
numbers = []
for line in file:
  line = line.strip()
  numbers.append(line)
file.close()

class Snailfish:
  def __init__( self, init_num ):
    self.num = init_num
    self.left = None
    self.right = None
    self.reduce()

  def __str__( self ):
    return self.num

  def magnitude( self, x ):
    if x.find(',') == -1:
      return int(x)

    temp = Snailfish( x )
    a = temp.magnitude( temp.left )
    b = temp.magnitude( temp.right )
    return int(3 * a) + int(2 * b )

  def get_magnitude( self ):
    return self.magnitude( self.num )

  def add( self, right_side ):
    self.num = '[' + self.num + ',' + right_side.num + ']'
    self.reduce()

  def reduce( self ):
    done = False

    while not done:
      # first check for explodes
      check_for_splits = True

      sep = None
      deep_start = deep_end = None
      depth = i = 0
      while i < len(self.num):
        c = self.num[i]
        if c == '[':
          depth += 1
          if depth == 5:
            deep_start = i

        elif c == ']':
          if deep_start:
            deep_end = i
            to_explode = self.num[deep_start:deep_end+1]
            (explode_left, explode_right) = self.num[deep_start+1:deep_end].split(',')

            found = False
            explode_start = explode_end = None
            LEFT = self.num[:deep_start]
            for j in range( deep_start, 0, -1 ):
              if not found and self.num[j].isnumeric():
                explode_end = j
                found = True
              elif found and not self.num[j].isnumeric():
                explode_start = j+1
                explode_num = int(self.num[explode_start:explode_end+1])
                explode_num += int(explode_left)
                LEFT = self.num[:explode_start] + str(explode_num) + self.num[explode_end+1:deep_start]
                break

            found = False
            explode_start = explode_end = None
            RIGHT = self.num[deep_end+1:]
            for j in range( deep_end+1, len(self.num) ):
              if not found and self.num[j].isnumeric():
                explode_start = j
                found = True
              elif found and not self.num[j].isnumeric():
                explode_end = j
                explode_num = int(self.num[explode_start:explode_end])
                explode_num += int(explode_right)
                RIGHT = self.num[deep_end+1:explode_start] + str(explode_num) + self.num[explode_end:]
                break

            self.num = LEFT + '0' + RIGHT
            check_for_splits = False
            break # reset and go again

          depth -= 1
        elif c == ',' and depth == 1:
          sep = i

        i += 1

      if not check_for_splits:
        continue

      # now check for splits
      i = 0
      num_start = num_end = None
      while i < len(self.num):
        if not num_start and self.num[i].isnumeric():
          num_start = i
        elif num_start and not self.num[i].isnumeric():
          num_end = i
          value = int(self.num[num_start:num_end])

          if value > 9:
            LEFT = self.num[:num_start]
            RIGHT = self.num[num_end:]
            a = int(value/2)
            b = value - int(value/2)
            self.num = '%s[%d,%d]%s' % (LEFT, a, b, RIGHT)
            check_for_splits = False
            break

          else:
            num_start = num_end = None

        i += 1

      if not check_for_splits:
        continue

      # else ...
      done = True

      self.left = self.num[1:sep]
      self.right = self.num[sep+1:-1]

# --- part one ---

a = None
for n in numbers:
  if not a:
    a = Snailfish( n )
  else:
    b = Snailfish( n )
    a.add( b )

print( 'part one:', a.get_magnitude() )

# --- part two ---

max_magnitude = 0
for x in range( len(numbers) ):
  for y in range( len(numbers ) ):
    if x == y:
      continue

    a = Snailfish( numbers[x] )
    b = Snailfish( numbers[y] )
    a.add( b )
    magnitude = a.get_magnitude()
    if magnitude > max_magnitude:
      max_magnitude = magnitude

print( 'part two:', max_magnitude )
