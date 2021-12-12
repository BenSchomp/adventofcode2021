file = open('day-12.txt', 'r')
caves = {}
for line in file:
  (left, right) = line.strip().split( '-' )
  if not left in caves:
    caves[left] = []
  caves[left].append(right)
  if not right in caves:
    caves[right] = []
  caves[right].append(left)
file.close()

print( caves )

#      start
#      /   \
#  c--A----b--d
#     \   /
#      end

count = 0
def traverse( id, seen ):
  if id[0].islower() and id in seen:
    print( id, seen, '... lower twice' )
    return

  seen.append(id)
  print( id, seen )

  if id == 'end':
    print( ' *****', seen )
    global count
    count += 1
    return

  for cur in caves[id]:
    traverse( cur, seen.copy() )

  return


traverse( 'start', [] )
print( count )
