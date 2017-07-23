import sys

input = []
for line in sys.stdin:
    line = line.replace('\n', '')
    input.append(line)

info = (input.pop(0)).split() #get first line - r, n
info = map(int, info)
#get r and n
r = info[0]
n = info[1]

if r == n: #all rooms are booked
    print "too late"
else:
    rooms = map(int, input) #change the remaining rooms into room numbers
    #find the first available room
    if len(rooms) == 0: #all rooms available
        print 1
    else:
        min_room = min(rooms)
        free_room = min_room #start with smallest room
        while free_room in rooms: #if this room is taken, increase
            if free_room >= r: #then reset
                free_room = 1
            else:
                free_room += 1
        print free_room
