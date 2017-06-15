import sys
import math

input = []
for line in sys.stdin:
    line = line.replace('\n', '')
    input.append(line)

area = float(input.pop(0)) #get area
side = math.sqrt(area) #find length of each side
fence = side*4
print fence