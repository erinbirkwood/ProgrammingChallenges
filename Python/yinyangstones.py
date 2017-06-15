import sys

input = []
for line in sys.stdin:
    line = line.replace('\n', '')
    input.append(line)

stones = input.pop(0)
w = stones.count('W')
b = stones.count('B')

if w == b: #need to have same number of each colour!
    print 1
else:
    print 0