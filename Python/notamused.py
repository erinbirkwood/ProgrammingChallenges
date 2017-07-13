import sys
import operator

input = []
for line in sys.stdin:
    line = line.replace('\n', '')
    input.append(line)

day_count = 1 #initialize day count
all_bills = {} #keep track of all bills

while (input):
    input.pop(0) #pop "OPEN"
    day_bills = {} #keep track of bills for the day
    temp_bills = {} #keep track of each visit during day
    while (input[0] != 'CLOSE'):
        instruction = (input.pop(0)).split()
        cmd = instruction.pop(0) #get command
        name = instruction.pop(0) #get cust name
        time = float(instruction.pop(0)) #get relevant time
        if cmd == 'ENTER': #time is entering
            temp_bills[name] = time
        else: #cmd == 'EXIT', time is closing
            calc = round(((time - temp_bills[name]) * 0.10), 2) #calculate cost
            if name in day_bills: #have already visited today
                day_bills[name] += calc
            else:
                day_bills[name] = calc
    input.pop(0) #pop "CLOSE"
    sorted_bills = sorted(day_bills.items(), key = operator.itemgetter(0)) #sort by name
    all_bills[day_count] = sorted_bills
    day_count += 1 #prepare for next day

for day in all_bills: #display each bills per day
    print "Day " + str(day)
    for i in range(len(all_bills[day])):
        print all_bills[day][i][0] + " $" + str(all_bills[day][i][1]) + "0"
    if day < (day_count - 1):
        print ""
