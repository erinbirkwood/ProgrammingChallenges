import sys

input = []
for line in sys.stdin:
    line = line.replace('\n', '')
    input.append(line)

num_cases = int(input.pop(0)) #pop the number of test cases

while (input): 
    num_stores = int(input.pop(0)) #pop number of stores
    store_loc = (input.pop(0)).split()
    store_loc = map(int, store_loc) #change all strings to ints
    store_loc.sort() #sort stores by location
    parking_spot = int((max(store_loc) - min(store_loc)/2))
    walking_dist = 0
    for i in range(num_stores-1):
        walking_dist += abs(store_loc[i] - store_loc[i+1])
    print walking_dist*2
    

