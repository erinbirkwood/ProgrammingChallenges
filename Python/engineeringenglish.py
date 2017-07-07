import sys

input = []
for line in sys.stdin:
    line = line.replace('\n', '')
    input.append(line)

used_words = [] #store words previously seen

while (input):
    phrase = (input.pop(0)).split() #get phrase as list
    for i in range(len(phrase)): #iterate through phrase
        if phrase[i].lower() in used_words: #replace it
            phrase[i] = "."
        else: #print but add to used words
            used_words.append(phrase[i].lower())
    phrase_str = " ".join(phrase) #get new phrase as string
    print phrase_str