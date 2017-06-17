import sys
import math

input = []
for line in sys.stdin:
    line = line.replace('\n', '')
    input.append(line)

input.pop() #get rid of final zero

while (input):
    data = (input.pop(0)).split()
    data = map(float, data) #change to float for ease
    x1 = data[0]
    y1 = data[1]
    x2 = data[2]
    y2 = data[3]
    p = data[4]
    inv_p = 1.0/p #inverse of p

    #perform calculations
    x_res = abs(x1 - x2)
    y_res = abs(y1 - y2)
    xy_pow = math.pow(x_res, p) + math.pow(y_res, p)
    result = math.pow(xy_pow, inv_p)
    print result


