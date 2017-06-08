import sys

input = []
for line in sys.stdin:
    line = line.replace('\n', '')
    input.append(line)

input = input[0].split()

fizz = int(input.pop(0)) #pop x (fizz)
buzz = int(input.pop(0)) #pop y (buzz)
n = int(input.pop(0))

for i in range(1, n+1): #iterate through all numbers from 1 --> N
    if (i%fizz == 0) and (i%buzz == 0):
        print "FizzBuzz"
    elif (i%fizz == 0):
        print "Fizz"
    elif (i%buzz == 0):
        print "Buzz"
    else:
        print i