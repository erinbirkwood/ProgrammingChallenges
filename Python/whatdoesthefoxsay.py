import sys

input = []
for line in sys.stdin:
    line = line.replace('\n', '')
    input.append(line)

num_cases = int(input.pop(0)) #num test cases

while (input): #while still cases
    noise = (input.pop(0)).split()
    sounds = {} #dictionary of animal sounds
    animal = input.pop(0)
    while (input) and (animal != "what does the fox say?"): #this ends the test case
        animal = animal.split() #animal sound
        sounds[animal[2]] = animal[0] #store sound and animal
        animal = input.pop(0)
    
    fox_sounds = [] 
    for sound in noise:
        if sound not in sounds: #store unrecognized sounds
            fox_sounds.append(sound)
    fox_says = ' '.join(fox_sounds) #turn into string
    print fox_says
