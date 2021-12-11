file = open('day-11.txt', 'r')
grid = []
for line in file:
  row = []
  for l in line.strip():
    row.append(int(l))
  grid.append(row)
file.close()
SIZE = 10

def display():
  for row in grid:
    print( ''.join(map(str,row)) )
  print()

flashes = 0
steps = 0
while True:
  neighbors = []
  # everyone gets a +1
  for y in range(SIZE):
    for x in range(SIZE):
      grid[y][x] += 1
      if grid[y][x] == 10:
        flashes += 1
        # store which neighbors to +1 later
        for dx in [-1,0,1]:
          for dy in [-1,0,1]:
            if SIZE > x+dx >= 0 and SIZE > y+dy >= 0:
              neighbors.append( (x+dx,y+dy) )

  # process the nieghbor list
  while len(neighbors) > 0:
    p = neighbors.pop()
    (x, y) = p
    grid[y][x] += 1
    if grid[y][x] == 10:
      flashes += 1
      # propagate additional neighbor +1's
      for dx in [-1,0,1]:
        for dy in [-1,0,1]:
          if SIZE > x+dx >= 0 and SIZE > y+dy >= 0:
            neighbors.append( (x+dx,y+dy) )

  # reset flashed octopuses and check for a simultaneous
  simul_flash = True
  for y in range(SIZE):
    for x in range(SIZE):
      if grid[y][x] > 9:
        grid[y][x] = 0
      if grid[y][x] > 0:
        simul_flash = False

  steps += 1
  if simul_flash:
    print( 'part two:', steps )
    break

  if steps == 100:
    print( 'part one:', flashes )
