import sys

input = []
for line in sys.stdin:
    line = line.replace('\n', '')
    input.append(line)

soylent = 400 #num calories in a bottle
num_cases = int(input.pop(0))
while (input):
    cals = int(input.pop(0))
    if cals % soylent == 0: #exact num bottles
        print cals/soylent
    else: #round up
        print cals/soylent + 1
