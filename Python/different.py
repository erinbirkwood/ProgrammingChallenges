import sys

input = []
for line in sys.stdin:
    line = line.replace('\n', '')
    input.append(line)

while (input): #while there are pairs of numbers left
    nums = (input.pop(0)).split()
    nums = map(int, nums) #change to integers
    print abs(nums[0] - nums[1])
