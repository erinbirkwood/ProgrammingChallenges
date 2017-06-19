import sys
import math

input = []
for line in sys.stdin:
    line = line.replace('\n', '')
    input.append(line)

cuts = float(input.pop(0))
vert_cuts = int(math.ceil(cuts/2)) #vertical cuts
hori_cuts = int(math.floor(cuts/2)) #horizontal cuts

num_pieces = vert_cuts + 1 #start with num pieces from cutting vertically
num_pieces += (hori_cuts*(vert_cuts+1)) #for each horizontal cut, add the #vertical pieces in one line

print num_pieces