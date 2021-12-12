file = open('day-12.txt', 'r')
caves = {}
for line in file:
  (left, right) = line.strip().split( '-' )
  if not left in caves:
    caves[left] = []
  if right != 'start': # can never return to start
    caves[left].append(right)
  if not right in caves:
    caves[right] = []
  if left != 'start': # can never return to start
    caves[right].append(left)
file.close()

def traverse( id, seen ):
  if id[0].islower() and id in seen:
    if seen[0] == None: # part one
      return
    elif seen[0] == True: # we've already seen a double-lower
      return
    seen[0] = True # this is the double-lower, mark it and continue on ...

  seen.append(id)

  if id == 'end':
    # found a path!
    global count
    count += 1
    #print( ','.join(seen[1:]) )
    return

  # else traverse to all neighboring caves
  for cur in caves[id]:
    traverse( cur, seen.copy() )

# --- part one ---
count = 0
traverse( 'start', [None] )
print(count)

# --- part two ---
count = 0
traverse( 'start', [False] )
print(count)
