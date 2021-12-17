# target area: x=20..30, y=-10..-5 // EXAMPLE
target_x = (20, 30)
target_y = (-10, -5)

# target area: x=138..184, y=-125..-71 // REAL
target_x = (138, 184)
target_y = (-125, -71)

hit_count = 0
overall_max = [0, 0, 0]
for init_dx in range(250):
  for init_dy in range(-250,250):
    x = y = 0
    dx = init_dx
    dy = init_dy
    y_max = [0, 0, 0]
    count = 0
    hit = False
    while True:
      #print( "%d. (%d, %d) ... [%d, %d]" % (count, x, y, dx, dy) )
      if x >= target_x[0] and x <= target_x[1] and \
         y >= target_y[0] and y <= target_y[1]:
        #print( 'hit ... ', init_dx, init_dy )
        hit = True
        hit_count += 1
        break

      x += dx
      y += dy

      if dx > 0:
        dx -= 1
      elif dx < 0:
        dx += 1
      dy -= 1

      if y > y_max[0]:
        (y_max[0], y_max[1], y_max[2]) = (y, init_dx, init_dy)

      if x > target_x[1] or y < target_y[0]:
        break

      count += 1

    if hit and y_max[0] > overall_max[0]:
      overall_max = y_max
      #print( '! new max:', overall_max )

print( 'part one:', overall_max[0] )
print( 'part two:', hit_count )
