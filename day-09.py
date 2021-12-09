file = open('day-09.txt', 'r')
grid = []
for line in file:
  grid.append( list(line.strip()) )
file.close()

height = len(grid)
width = len(grid[0])

def display( m ):
  for row in m:
    for cell in row:
      print( cell, end='')
    print()
  print()

low_points = []

# --- part one ###
risk = 0
y = 0
while y < height:
  x = 0
  while x < width:
    is_low_point = True
    for d in [(-1,0),(1,0),(0,-1),(0,1)]:
      if x+d[0] < 0 or x+d[0] >= width or y+d[1] < 0 or y+d[1] >= height:
        continue
      if grid[y+d[1]][x+d[0]] <= grid[y][x]:
        is_low_point = False
    if is_low_point:
      low_points.append((x,y))
      risk += int(grid[y][x]) + 1
    x += 1
  y += 1

print( risk )

# --- part two ---
def travel( x, y, seen ):
  seen[y][x] = 1
  for d in [(-1,0),(1,0),(0,-1),(0,1)]:
    new_x = x+d[0]
    new_y = y+d[1]
    if new_x < 0 or new_x >= width or new_y < 0 or new_y >= height:
      continue
    if seen[new_y][new_x] == 1 or grid[new_y][new_x] == '9':
      continue
    travel( new_x, new_y, seen )

basin_sizes = []
for lp in low_points:
  seen = []
  for i in range(height):
    seen.append([0]*width)

  travel( lp[0], lp[1], seen )

  basin_size = 0
  for row in seen:
    basin_size += sum(row)
  basin_sizes.append(basin_size)

basin_sizes = sorted(basin_sizes, reverse=True)
print( basin_sizes[0] * basin_sizes[1] * basin_sizes[2] )
