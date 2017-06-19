import sys

input = []
for line in sys.stdin:
    line = line.replace('\n', '')
    input.append(line)

num_cases = int(input.pop(0)) #test cases

while (input):
    num_places = int(input.pop(0)) #number of places visited
    places = [] #store places
    for i in range(num_places):
        place = input.pop(0)
        if place not in places:
            places.append(place)
    print len(places) #number of unique places
