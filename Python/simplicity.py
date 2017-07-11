import sys
import operator

input = []
for line in sys.stdin:
    line = line.replace('\n', '')
    input.append(line)

word = list(input.pop(0)) #get word as list

letters = {} #keep track of letters and frequencies
for letter in word:
    if letter in letters: #have previously seen letter
        letters[letter] += 1
    else: #add letter
        letters[letter] = 1

#sort letters by frequency (highest --> lowest)
sorted_letters = sorted(letters.items(), key = operator.itemgetter(1), reverse=True)
if len(sorted_letters) <= 2: #don't need to remove any letters
    print 0
else:
    remove = 0 #count letters to remove
    for i in range(2, len(sorted_letters)):
        remove += sorted_letters[i][1]
    print remove
        