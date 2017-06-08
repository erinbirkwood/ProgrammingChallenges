import sys
import math

input = [] #get user input
for line in sys.stdin:
    line = line.replace('\n','')
    input.append(line)

def findNum(root_val, count, directions, tree_height,i):
    if tree_height == 0: #iteration is done, return current node
        return root_val - count
    else:
        if directions[i] == ' ': #return current value
            return root_val - count
        elif directions[i] == 'L': #direction is left
            count = count*2 + 1
            return findNum(root_val, count, directions, tree_height-1, i+1)
        else: #direction is 'R'
            count = count*2 + 2
            return findNum(root_val, count, directions, tree_height-1, i+1)
=====
separate_input = input.pop(0) #get one line of input
separate_input = separate_input.split()
tree_height = float(separate_input[0]) #get height of tree as int
if len(separate_input) == 1: #if no directions are given
    ans = int(math.pow(2.0, tree_height+1)-1) #return with value of root
else:
    directions = separate_input[1] + ' ' #get directions, add extra space
    #main function
    root_val = int(math.pow(2.0, tree_height+1)-1)
    ans = findNum(root_val, 0, directions, tree_height, 0)

print ans
