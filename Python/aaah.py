import sys

input = []
for line in sys.stdin:
    line = line.replace('\n', '')
    input.append(line)

jon = input.pop(0)
doctor = input.pop(0)
if len(jon) >= len(doctor): #compare lengths of aaahs
    print "go"
else:
    print "no"