import sys
import math

input = []
for line in sys.stdin:
    line = line.replace('\n', '')
    input.append(line)

data = (input.pop(0)).split()
r = float(data[0])
c = float(data[1])

crust = ((r - c)**2 / r**2) * 100.0 #find total crust area
print crust