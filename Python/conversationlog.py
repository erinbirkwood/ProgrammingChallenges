import sys
import operator

input = []
for line in sys.stdin:
    line = line.replace('\n', '')
    input.append(line)

all = {} #keep track of all words and frequencies
people = {} #keep track of words people have said

num_lines = int(input.pop(0)) #number of lines

while (input):
    line = (input.pop(0)).split()
    user = line.pop(0) #get username
    temp = {} #temp dictionary
    user_temp = [] #store unique words in sentence
    
    for word in line: #find stats of words in sentence
        if word in temp:
            temp[word] += 1
        else:
            temp[word] = 1
    
    if user not in people: #if user not in user list, add
        people[user] = []

    for key in temp: #find all words said, add stats to overall stats
        if key not in people[user]:
            people[user].append(key)
        if key in all:
            all[key] += temp[key]
        else:
            all[key] = temp[key]

lists = []
for person in people: #find words used by each person
    lists.append(people[person])

all_words = set(lists[0]) #find all unique words in all lists
for i in lists[1:]:
    all_words.intersection_update(i)

if not all_words: #is empty
    print "ALL CLEAR"
else: #not empty
    remaining = {} #get words left and their frequencies
    for word in all_words:
        remaining[word] = all[word]
    #sort remaining by descending frequency, then alphabetical ** tricky
    result = []
    for word, score in sorted(remaining.items(), key = lambda x:(x[1]), reverse=True): #sort by freq
        result.append([score, word])
    #sort result by bubblesort 
    sorted = False
    while (sorted == False):
        sorted = True
        for i in range(len(result)-1):
            if result[i][0] == result[i+1][0]:
                if result[i][1] > result[i+1][1]: #swap needed
                    sorted = False
                    temp = result[i][1]
                    result[i][1] = result[i+1][1]
                    result[i+1][1] = temp
    
    #get results
    for list in result:
        print list[1]
    