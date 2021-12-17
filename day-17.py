# target area: x=20..30, y=-10..-5 // EXAMPLE
target_x = (20, 30)
target_y = (-10, -5)

# target area: x=138..184, y=-125..-71 // REAL
target_x = (138, 184)
target_y = (-125, -71)

hit_count = 0
y_max_overall = 0
overall_ma0 = [0, 0, 0]
for init_dx in range(250):
  for init_dy in range(-250,250):
    x = y = 0
    dx = init_dx
    dy = init_dy
    y_max = 0
    count = 0
    hit = False
    while True:
      #print( "%d. (%d, %d) ... [%d, %d]" % (count, x, y, dx, dy) )
      if x >= target_x[0] and x <= target_x[1] and \
         y >= target_y[0] and y <= target_y[1]:
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

      if y > y_max:
        y_max = y

      if x > target_x[1] or y < target_y[0]:
        break

      count += 1

    if hit and y_max > y_max_overall:
      y_max_overall = y_max
      #print( '! new max:', overall_max )

print( 'part one:', y_max_overall )
print( 'part two:', hit_count )
