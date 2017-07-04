import sys

input = []
for line in sys.stdin:
    line = line.replace('\n', '')
    input.append(line)

while (input[0] != "0 0"): #0 0 is end of cases
    stats = (input.pop(0)).split()
    sweet = int(stats[0])
    sour = int(stats[1])
    if (sweet + sour == 13): #check first - must never speak again
        print "Never speak again."
    elif sweet > sour: #only acceptable case
        print "To the convention."
    elif sweet == sour:
        print "Undecided."
    else: #sweet < sour
        print "Left beehind."