import sys

input = []
for line in sys.stdin:
    line = line.replace('\n', '')
    input.append(line)

num_buses = int(input.pop(0)) #num test cases

def findPeople(stops): #find total passengers
    people = 1.0 #one person from the last stop
    if (stops > 1.0):
        for i in range(2, stops+1):
            people += 0.5 #add half the amount of people, mult by 2 (reverse operation)
            people = 2.0*people
    return people

while (input):
    num_stops = int(input.pop(0)) #get number of stops
    #find passengers
    print int(findPeople(num_stops))