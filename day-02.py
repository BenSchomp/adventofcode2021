
file = open('day-02.txt', 'r')
data = []
for line in file:
  line = line.strip()
  (dir, dist) = line.split( ' ' )
  data.append( (dir,int(dist)) )
file.close()

x = y = 0
for (dir,dist) in data:
    print( dir, dist )
    if dir == 'forward':
        x += dist
    elif dir == 'up':
        y -= dist
    elif dir == 'down':
        y += dist

print( x * y )

x = y = aim = 0
for (dir,dist) in data:
    print( dir, dist )
    if dir == 'forward':
        x += dist
        y += (aim * dist)
    elif dir == 'up':
        aim -= dist
    elif dir == 'down':
        aim += dist

print( x * y )
