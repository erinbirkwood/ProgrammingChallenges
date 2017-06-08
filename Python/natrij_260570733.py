import sys

input = [] #get user input
for line in sys.stdin:
    line = line.replace('\n','')
    input.append(line)

curr_time = input.pop(0).split(':')
explode_time = input.pop(0).split(':')

time = [] #find time to curr_time on timer
    
def findHour(numMin, numSec):
    if (explode_time[0] > curr_time[0]):
        time.append(str(int(explode_time[0]) - int(curr_time[0]) - numMin))
    elif(explode_time[0] < curr_time[0]):
        time.append(str(24 - int(curr_time[0]) + int(explode_time[0]) - numMin))
    else:
        if (numMin == 1 or numSec == 1):
            time.append("23")
            if (curr_time[1] == explode_time[1]):
                time[1] = "59"
        else:
            time.append("00")

def findMin(numSec):
    numMin = 0
    if (explode_time[1] < curr_time[1]):
        time.append(str(60 - int(curr_time[1]) + int(explode_time[1]) - numSec))
        numMin = 1 #carry over
    elif (explode_time[1] > curr_time[1]):
        time.append(str(int(explode_time[1]) - int(curr_time[1]) - numSec))
    else: 
        if numSec == 1:
            time.append("59")
            numMin = 1
        else:
            time.append("00")
    findHour(numMin, numSec)

def findSec(): #find the number of seconds remaining
    numSec = 0
    if (explode_time[2] < curr_time[2]):
        time.append(str(60 - int(curr_time[2]) + int(explode_time[2])))
        numSec = 1 #carry over
    elif (explode_time[2] > curr_time[2]): 
        time.append(str(int(explode_time[2]) - int(curr_time[2])))
    else: 
        time.append("00")
    findMin(numSec)

findSec() #call function

for i in range(len(time)):
    if (int(time[i]) > 0 and int(time[i]) < 10 or time[i] == "0"):
        time[i] = "0" + time[i]

check = 0 #check for 00:00:00 case
for i in range(len(time)):
    if (time[i] == "00"):
        check += 1      
if (check == 3):
    print "24:00:00"
else:
    print (time[2] + ":" + time[1] + ":" + time[0])



