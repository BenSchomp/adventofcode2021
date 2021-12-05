
# ---
class Line:
  def __init__( self, x1, y1, x2, y2 ):
    self.x1 = x1
    self.x2 = x2
    self.y1 = y1
    self.y2 = y2

    self.dx = self.dy = 0
    if y1 < y2:
      self.dy = 1
    elif y1 > y2:
      self.dy = -1

    if x1 < x2:
      self.dx = 1
    elif x1 > x2:
      self.dx = -1

  def __str__( self ):
    return "%d,%d -> %d,%d" % (self.x1, self.y1, self.x2, self.y2 )

  def is_horiz_or_vert( self ):
    return (self.x1 == self.x2) or (self.y1 == self.y2)

  def get_coords( self ):
    return (self.x1, self.y1, self.x2, self.y2)

  def get_deltas( self ):
    return (self.dx, self.dy)

# ---
class Grid:
  def __init__( self, size_x, size_y ):
    self.width = size_x
    self.height = size_y
    self.grid = [([0]*size_x) for i in range(size_y)]
    self.overlap_count = 0

  def __str__( self ):
    out = ''
    for row in self.grid:
      for n in row:
        if n == 0:
          out += '.'
        else:
          out += str(n)
      out += "\n"
    return out

  def add_point( self, x, y ):
    self.grid[y][x] += 1
    if self.grid[y][x] == 2:
      self.overlap_count += 1

  def get_overlap_count( self ):
    return self.overlap_count

  def add_line( self, line ):
    (x1, y1, x2, y2) = line.get_coords()
    (dx, dy) = line.get_deltas()

    x = x1
    y = y1
    while True:
      self.add_point(x, y)
      x += dx
      y += dy

      if x == x2 and y == y2:
        self.add_point(x, y)
        break

# --- main ---
file = open('day-05.txt', 'r')
lines = []
max_x = max_y = 0
for line in file:
  line = line.strip()
  (p1, p2) = line.split( ' -> ' )
  (x1,y1) = map(int, p1.split(','))
  (x2,y2) = map(int, p2.split(','))
  lines.append( Line( x1, y1, x2, y2 ) )

  if max(x1, x2) > max_x:
    max_x = max(x1, x2)
  if max(y1, y2) > max_y:
    max_y = max(y1, y2)
file.close()

# -- part one --
grid = Grid(max_x+1, max_y+1)

for line in lines:
  if line.is_horiz_or_vert():
    grid.add_line(line)

print( grid )
print( "overlaps:", grid.get_overlap_count(), "\n" )

# --- part two ---
grid = Grid(max_x+1, max_y+1)

for line in lines:
  grid.add_line(line)

print( grid )
print( "overlaps:", grid.get_overlap_count(), "\n" )
