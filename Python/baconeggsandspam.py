import sys
import operator

input = []
for line in sys.stdin:
    line = line.replace('\n', '')
    input.append(line)

while (input[0] != '0'): #0 at end of test cases
    menu = {} #store menu items and people who ordered
    num_people = int(input.pop(0))
    for i in range(num_people):
        order = (input.pop(0)).split()
        person = order.pop(0) #get name of person ordering
        for item in order: 
            if item in menu: #add person's name
                menu[item].append(person)
            else:
                menu[item] = [person]
    
    #sort menu items alphabetically
    sorted_menu = sorted(menu.items(), key = operator.itemgetter(0))

    for i in range(len(sorted_menu)):
        item = sorted_menu[i][0] #get menu item
        people = sorted_menu[i][1] #get people who ordered
        people.sort() #sort people alphabetically
        people_str = " ".join(people)
        print item + " " + people_str
    
    if len(input) > 1: #if there are more orders, print new line
        print ""
    
