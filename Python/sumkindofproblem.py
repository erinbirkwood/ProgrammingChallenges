import sys

input = []
for line in sys.stdin:
    line = line.replace('\n', '')
    input.append(line)

test_cases = int(input.pop(0)) #num cases to follow

while (input): #while still test cases
    line = (input.pop(0)).split()
    set_num = line[0] #k value
    n = int(line[1]) #n value
    #get lists of numbers included in each sum
    s1_lst = range(1, n+1)
    s2_lst = range(1, 2*n+1, 2)
    s3_list = range(2, 2*n+1, 2)
    #add all numbers in list
    s1 = sum(s1_lst)
    s2 = sum(s2_lst)
    s3 = sum(s3_list)
    #get results
    print set_num + " " + str(s1) + " " + str(s2) + " " + str(s3)
