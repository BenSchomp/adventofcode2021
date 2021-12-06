
data = [3,4,3,1,2]
data = [1,3,1,5,5,1,1,1,5,1,1,1,3,1,1,4,3,1,1,2,2,4,2,1,3,3,2,4,4,4,1,3,1,1,4,3,1,5,5,1,1,3,4,2,1,5,3,4,5,5,2,5,5,1,5,5,2,1,5,1,1,2,1,1,1,4,4,1,3,3,1,5,4,4,3,4,3,3,1,1,3,4,1,5,5,2,5,2,2,4,1,2,5,2,1,2,5,4,1,1,1,1,1,4,1,1,3,1,5,2,5,1,3,1,5,3,3,2,2,1,5,1,1,1,2,1,1,2,1,1,2,1,5,3,5,2,5,2,2,2,1,1,1,5,5,2,2,1,1,3,4,1,1,3,1,3,5,1,4,1,4,1,3,1,4,1,1,1,1,2,1,4,5,4,5,5,2,1,3,1,4,2,5,1,1,3,5,2,1,2,2,5,1,2,2,4,5,2,1,1,1,1,2,2,3,1,5,5,5,3,2,4,2,4,1,5,3,1,4,4,2,4,2,2,4,4,4,4,1,3,4,3,2,1,3,5,3,1,5,5,4,1,5,1,2,4,2,5,4,1,3,3,1,4,1,3,3,3,1,3,1,1,1,1,4,1,2,3,1,3,3,5,2,3,1,1,1,5,5,4,1,2,3,1,3,1,1,4,1,3,2,2,1,1,1,3,4,3,1,3]
g_school = []

class Fish:
  def __init__( self, init_timer ):
    self.timer = init_timer

  def __str__( self ):
    return 'x'

  def get_timer( self ):
    return self.timer

  def next_day( self ):
    self.timer -= 1

    if self.timer < 0:
      self.timer = 6

      g_school.append( Fish(9) )

for d in data:
  g_school.append( Fish(d) )

day = 1
while day <= 80:
  for f in g_school:
    f.next_day()
  day += 1
print( len(g_school) )

# --- part two ---
age_counts = [0]*9
for d in data:
  age_counts[d] += 1

day = 1
while day <= 256:
  new_spawns = age_counts[0]
  for i in range(8):
    age_counts[i] = age_counts[i+1]
  age_counts[8] = new_spawns
  age_counts[6] += new_spawns
  day += 1

print( sum(age_counts) )
