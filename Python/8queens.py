import sys
import math

input = []
for line in sys.stdin:
    line = line.replace('\n', '')
    input.append(line)

def check_column(column):
    for i in range(8):
        if (column[i].count('*') != 1): 
            return False
    return True

def check(c1, c2): 
    rise = abs(float(c2[1] - c1[1]))
    run = abs(float(c2[0] - c1[0]))
    
    if (float(rise/run) == 1.0):
        return False
    else:
        return True

def check_diagonal(list):
    i = 0
    while (i<8):
        j = i+1
        while (j<8):
            if (check(list[i], list[j]) == False): 
                return False 
            j += 1
        i += 1
    return True


answer = "valid"
for i in range(8): #check rows
    if (input[i].count('*') != 1):
        answer = "invalid"
        break
if answer == "valid":
    column = ['' for i in range(8)]
    for i in range(8):
        for j in range(8):
            column[i] = column[i] + input[j][i]
    temp = check_column(column)
    if (temp == False): 
        answer = "invalid"
    if answer == "valid":
        coordinates = []
        for i in range(8): 
            coordinates.append([i+1, input[i].index('*')+1])
        if check_diagonal(coordinates) == False:
            answer = "invalid"
            
print answer


