import sys
import math

input = []
for line in sys.stdin:
    line = line.replace('\n', '')
    input.append(line)

encode = input.pop(0) #encoded message
if encode == "":
    print ""

else:
    col = 0
    row = 0
    #find best solution for #columns and #rows
    for i in range(1, int(math.sqrt(len(encode)))+1):
        if len(encode) % i == 0:
            col = i
            row = len(encode)/col

    array = []
    counter = 0 #store location in string
    for i in range(row):
        temp = []
        for j in range(col):
            temp.append(encode[counter])
            counter += 1
        array.append(temp) #add portion of message

    decode = ""
    for i in range(col):
        for j in range(row):
            decode += array[j][i]

    print decode
