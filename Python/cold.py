import sys

input = []
for line in sys.stdin:
    line = line.replace('\n', '')
    input.append(line)

num_temps = int(input.pop(0)) #number of temperatures
temps = input.pop(0)
print temps.count("-")