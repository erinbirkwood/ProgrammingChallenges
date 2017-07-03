import sys

input = []
for line in sys.stdin:
    line = line.replace('\n', '')
    input.append(line)

info = (input.pop(0)).split() #list of trip info
#get important info
participants = int(info[0])
budget = int(info[1])
num_hotels = int(info[2])
num_weeks = int(info[3])

cheapest_trip = 999999 #initalize to large number

while (input): #get hotel info
    cost_person = int(input.pop(0)) #get cost per person
    num_beds = (input.pop(0)).split() #get num beds each week
    num_beds = map(int, num_beds) #change to ints for ease
    for beds in num_beds: #search for possible trips
        if beds >= participants:
            cost = cost_person*participants
            if (cost <= budget) and (cost < cheapest_trip): #best trip
                cheapest_trip = cost

if cheapest_trip == 999999: #no possible trip was found
    print "stay home"
else:
    print cheapest_trip
