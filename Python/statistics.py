import sys

input = []
for line in sys.stdin:
    line = line.replace('\n', '')
    input.append(line)

case = 1 #keep track of case number
while (input):
    data = (input.pop(0)).split(' ')
    data = map(int, data) #change data to ints
    num_vals = data.pop(0) #pop number of values
    #get statistics
    min_val = min(data)
    max_val = max(data)
    range = max_val - min_val
    print "Case " + str(case) + ": " + str(min_val) + " " + str(max_val) + " " + str(range)
    case += 1