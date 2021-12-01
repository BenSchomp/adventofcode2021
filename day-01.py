
file = open('day-01.txt', 'r')
data = []
for line in file:
  num = int( line.strip() )
  data.append( num )
file.close()


cur = None
count = 0
for d in data:
    if cur is not None and d > cur:
        count += 1
    cur = d

print( count )


prev = None
count = 0
i = 2
while i < len(data):
    cur = data[i] + data[i-1] + data[i-2]
    if prev is not None and cur > prev:
        count += 1

    prev = cur
    i += 1

print( count )
