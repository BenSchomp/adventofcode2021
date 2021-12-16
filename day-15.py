import copy

file = open('day-15.txt', 'r')
init_grid = []
for line in file:
  line = line.strip()
  row = []
  for c in line:
    row.append(int(c))
  init_grid.append(row)
file.close()
height = len(init_grid)
width = len(init_grid[0])

def display( grid ):
  for row in grid:
    print( ''.join(map(str,row)) )
  print()

def dijkstra( grid ):
  global heigh, width
  unvisited = []
  for y in range(height):
    for x in range(width):
      unvisited.append( (x,y) )

  shortest = {}
  previous = {}

  for p in unvisited:
    shortest[p] = 999999999
  shortest[(0,0)] = 0

  while unvisited:
    cur_min_loc = None
    for p in unvisited:
      if not cur_min_loc or shortest[p] < shortest[cur_min_loc]:
        cur_min_loc = p

    (x,y) = (cur_min_loc[0], cur_min_loc[1])
    for move in [(1,0), (0,1), (-1,0), (0,-1)]:
      (dx, dy) = (move[0], move[1])
      (new_x, new_y) = (x+dx, y+dy)

      if 0<=new_x<width and 0<=new_y<height:
        cur_value = shortest[cur_min_loc] + grid[new_y][new_x]
        if cur_value < shortest[(new_x,new_y)]:
          shortest[(new_x, new_y)] = cur_value
          previous[(new_x, new_y)] = cur_min_loc

    unvisited.remove( cur_min_loc )

  print( shortest[(width-1, height-1)] )

def expanded_grid_value( grid, x, y ):
  global height, width
  (x_mult, y_mult) = ( int(x/width), int(y/height) )

  value = grid[y%height][x%width]
  value += x_mult + y_mult

  if value > 9:
    value -= 9

  return value

def dijkstra_two( grid ):
  global height, width

  unvisited = []
  for y in range(height*5):
    for x in range(width*5):
      unvisited.append( (x,y) )

  shortest = {}
  previous = {}

  for p in unvisited:
    shortest[p] = 999999999
  shortest[(0,0)] = 0

  while unvisited:
    cur_min_loc = None
    for p in unvisited:
      if not cur_min_loc or shortest[p] < shortest[cur_min_loc]:
        cur_min_loc = p

    (x,y) = (cur_min_loc[0], cur_min_loc[1])

    if x == (width*5)-1 and y == (height*5)-1:
      print( shortest[((width*5)-1, (height*5)-1)] )
      #return

    for move in [(1,0), (0,1), (-1,0), (0,-1)]:
      (dx, dy) = (move[0], move[1])
      (new_x, new_y) = (x+dx, y+dy)

      if 0<=new_x<(width*5) and 0<=new_y<(height*5):
        cur_value = shortest[cur_min_loc] + expanded_grid_value(grid, new_x, new_y)
        if cur_value < shortest[(new_x,new_y)]:
          shortest[(new_x, new_y)] = cur_value
          previous[(new_x, new_y)] = cur_min_loc

    unvisited.remove( cur_min_loc )

  print( shortest[((width*5)-1, (height*5)-1)] )

expanded_grid_value( init_grid, 48, 49 )

dijkstra( init_grid )
dijkstra_two( init_grid ) # this still takes too long - use priority queue for better performance
