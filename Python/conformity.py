import sys
import operator

input = []
for line in sys.stdin:
    line = line.replace('\n', '')
    input.append(line)

num_frosh = int(input.pop(0))

combos = {} #keep track of unique course combos + frequency

while (input):
    #sort courses and then convert to single string
    combo_list = (input.pop(0)).split()
    combo_list.sort()
    combo = ''.join(combo_list)
    if combo not in combos: #add to possible combos
        combos[combo] = 1
    else:
        combos[combo] += 1 #increase num students

#get number of students taking most popular combo(s)
max = 0 #track max students
popular_frosh = 0 #track num students taking most popular combo
for combo in combos:
    if combos[combo] > max: #a new max was found
        max = combos[combo]
        popular_frosh = max
    elif combos[combo] == max: #same max, add to popular frosh
        popular_frosh += max
    #if lower, ignore

print popular_frosh

