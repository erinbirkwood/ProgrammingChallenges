import sys

input = []
for line in sys.stdin:
    line = line.replace('\n', '')
    input.append(line)

num_phrases = int(input.pop(0)) #pop number of phrases
alphabet_string = 'abcdefghijklmnopqrstuvwxyz' #easier than typing out list
alphabet = list(alphabet_string) #get alphabet as list
non_alpha = [' ', '.', ',', '?', '!', "'", '"'] #non alphabet chars

while (input):
    phrase = input.pop(0)
    phrase = phrase.lower() #change to all lowercase
    for char in non_alpha: #remove all non alphabetic characters
        phrase.replace(char, '')
    phrase = list(phrase) #turn into list
    remaining = list(set(alphabet) - set(phrase)) #get difference in letters
    if len(remaining) == 0: #is a pangram
        print "pangram"
    else:
        remaining.sort()
        remaining = "".join(remaining) #get letters left out
        print "missing " + str(remaining)


