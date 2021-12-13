file = open('day-13.txt', 'r')
points = []
folds = []
max_x = max_y = -1
grid_parse = True
for line in file:
  line = line.strip()
  if not len(line):
    grid_parse = False
  elif grid_parse:
    (x,y) = map(int, line.split( ',' ))
    points.append( (x,y) )
    if x > max_x:
      max_x = x
    if y > max_y:
      max_y = y
  else:
    fold = line.split()
    fold = fold[2].split('=')
    folds.append( (fold[0],fold[1]) )
file.close()

def display_count():
  count = 0
  for row in grid:
    count += sum(row)
  print( count )

def display():
  for row in grid:
    for c in row:
      if c == 1:
        print( '#', end='' )
      else:
        print( '.', end='' )
    print()
  print()

# --- seed grid from input data ---
grid = []
for i in range(max_y+1):
  grid.append( [0]*(max_x+1) )
for p in points:
  grid[p[1]][p[0]] = 1

# --- main loop ---
part_one = True
for fold in folds:
  val = int(fold[1])
  height = len(grid)
  width = len(grid[0])
  if fold[0] == 'y':
    # horizontal folds
    for dy in range( 1, height-val ):
      for x in range( width ):
        if grid[val+dy][x] == 1:
          grid[val-dy][x] = 1

    # trip at fold and below
    while len(grid) > val:
      del grid[-1]

  else:
    # verical folds
    for y in range(height):
      for dx in range( 1, width-val ):
        if grid[y][val+dx] == 1:
          grid[y][val-dx] = 1

    # trim at fold and right
    for y in range(height):
      for x in range(width-val):
        del grid[y][-1]

  if part_one:
    display_count()
    part_one = False

# done
display()
