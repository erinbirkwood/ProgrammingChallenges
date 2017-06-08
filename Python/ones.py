import sys

input = [] #get user input
for line in sys.stdin:
    line = line.replace('\n','')
    input.append(int(line))

while(len(input) > 0):
    num_ones = 1
    temp = 1
    n_val = input.pop(0)

    while(temp != 0):
        if (n_val > temp): #can't be a factor if it's greater
            temp = temp * 10 + 1
            num_ones += 1 #increase # of 1s
        else:
            temp = temp % n_val #check if n_val is a factor
    print num_ones #return number of ones needed




