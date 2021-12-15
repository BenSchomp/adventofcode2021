file = open('day-15.txt', 'r')
grid = []
for line in file:
  line = line.strip()
  row = []
  for c in line:
    row.append(int(c))
  grid.append(row)
file.close()
height = len(grid)
width = len(grid[0])

def display():
  for row in grid:
    print( ''.join(map(str,row)) )

def display_path( path ):
  for y in range(height):
    for x in range(width):
      if (x,y) == path[-1]:
        print( '#', end='')
      elif (x,y) in path:
        print( '+', end='')
      else:
        print( grid[y][x], end='' )
    print()
  print()

min_risk = None
count = 0

def walk( x, y, path, risk ):
  global grid, min_risk, width, height, count

  path.append( (x,y) )
  risk += grid[y][x]
  #display_path(path)

  if min_risk and risk >= min_risk:
    # if this new path is riskier than than best path ... abort
    return

  if x == width-1 and y == height-1:
    if not min_risk or risk < min_risk:
      min_risk = risk
    count += 1
    print( 'made it:', count, risk, min_risk )
    #display_path(path)
    return

  elif (x == width-1 and y == height-2) or (x == width-2 and y == height-1):
    # if you're next to the destination, for lowest path, only choice is to go directly to end
    walk( width-1, height-1, path.copy(), risk )

  else:
    for move in [(1,0), (0,1), (-1,0), (0,-1)]:
      dx = move[0]
      dy = move[1]

      if y == height-1 and dx == -1:
        # once you're on the bottom row, going left only traps you
        continue
      elif x == width and dy == -1:
        # once you're on the right col, going up only traps you
        continue
      elif x == 0 and dy == -1:
        # once you're on the left col, going up only traps you
        continue
      elif y == 0 and dy == -1:
        # once you're on the top row, going left only traps you
        continue

      if 0<=x+dx<width and 0<=y+dy<height and not (x+dx,y+dy) in path:
        # if its in bounds and we've not been there on this path, go there
        walk( x+dx, y+dy, path.copy(), risk )

x = []
walk( 0, 0, x.copy(), grid[0][0]*-1 )
print( min_risk )
