import sys

#read input from stdin
input = []
for line in sys.stdin:
    line = line.strip()
    input.append(line)

#find number of cases to follow
num_cases = int(input[0])

for i in range(1, num_cases+1):
    test_num = abs(int(input[i]))
    if (test_num %2 == 0):
        print str(input[i]) + " is even"
    else:
        print str(input[i]) + " is odd"