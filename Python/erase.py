import sys

input = []
for line in sys.stdin:
    line = line.replace('\n', '')
    input.append(line)

def evenCase(before, after): #odd switches
    while before and after: #while still bits
        if before.pop(0) != after.pop(0):
            return "Deletion failed"
    return "Deletion succeeded"

def oddCase(before, after): #even switches
    while before and after: #while still bits
        if before.pop(0) == after.pop(0):
            return "Deletion failed"
    return "Deletion succeeded"

switch = int(input.pop(0)) #number of switches
before = list(input.pop(0)) #before
after = list(input.pop(0)) #after

if switch % 2 == 0: #sequences should be the same
    print evenCase(before, after)
else: #should be reversed
    print oddCase(before, after)